import streamlit as st
from src.main import run_analysis
from src.db.sqlite_store import SQLiteStore


st.set_page_config(
    page_title="Prompt Variation Sensitivity Analyzer",
    layout="wide"
)

# -----------------------------
# Header
# -----------------------------
st.title("🧠 Prompt Variation Sensitivity Analyzer")
st.write(
    "Analyze how small changes in prompt phrasing affect AI-generated outputs."
)

# -----------------------------
# Sidebar Controls
# -----------------------------
st.sidebar.header("Settings")

mock_mode = st.sidebar.toggle(
    "Mock Mode (Testing only)",
    value=False
)

st.sidebar.info(
    "Mock mode uses simulated responses.\n"
    "Turn OFF only for a single real Gemini test."
)
st.sidebar.divider()
st.sidebar.subheader("📁 Analysis History")

db = SQLiteStore("prompt_analysis.db")
history = db.get_recent_runs(limit=5)

selected_run = None

if history:
    for run in history:
        label = f"{run['created_at'][:16]} | sim={run['similarity']:.2f}"
        if st.sidebar.button(label):
            selected_run = run
else:
    st.sidebar.caption("No previous runs found.")

if selected_run:
    st.subheader("🕘 Selected Past Analysis")

    st.markdown("**Prompt:**")
    st.code(selected_run["prompt"])

    st.metric(
        "Average Semantic Similarity",
        round(selected_run["similarity"], 3)
    )

    st.info(
        "This is a previously saved analysis.\n"
        "Metrics are shown from history; analysis is not re-run."
    )

    st.divider()

# -----------------------------
# Prompt Input
# -----------------------------

st.subheader("✏️ Enter Prompt")

prompt = st.text_area(
    "Base Prompt",
    height=120,
    placeholder="Explain artificial intelligence in simple terms..."
)

run_button = st.button("▶ Run Analysis")

# -----------------------------
# Run Analysis
# -----------------------------
if run_button:
    if not prompt.strip():
        st.error("Please enter a prompt before running the analysis.")
    else:
        with st.spinner("Running analysis..."):
            results = run_analysis(prompt, mock_llm=mock_mode)

        # -----------------------------
        # Metrics Section
        # -----------------------------
        st.subheader("📊 Evaluation Metrics")

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                label="Average Semantic Similarity",
                value=results["metrics"]["average_similarity"]
            )

        with col2:
            st.metric(
                label="Consistency Score",
                value=results["metrics"]["consistency_score"]
            )

        # -----------------------------
        # Feedback Section
        # -----------------------------
        st.subheader("📝 Automatic Feedback")

        st.success(results["feedback"]["summary"])

        if results["feedback"]["recommendations"]:
            st.write("**Recommendations:**")
            for rec in results["feedback"]["recommendations"]:
                st.write(f"- {rec}")

        # -----------------------------
        # Variations & Responses
        # -----------------------------
        st.subheader("🔁 Prompt Variations & Responses")

        for idx, (variation, response) in enumerate(
            zip(results["variations"], results["responses"]),
            start=1
        ):
            with st.expander(f"Variation {idx}"):
                st.markdown("**Prompt Variation:**")
                st.code(variation)

                st.markdown("**Model Response:**")
                st.write(response)
