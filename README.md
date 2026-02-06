# Prompt Variation Sensitivity Analyzer

An internal evaluation tool to analyze how variations in prompt phrasing affect AI-generated outputs.

The system generates controlled prompt variations, evaluates output consistency using semantic embeddings, and provides automatic feedback. A lightweight UI is included for visualization and experimentation.

---

## Features

- Prompt variation generation
- Gemini 2.5 Flash integration
- Semantic similarity & consistency evaluation
- Automatic feedback generation
- History tracking using SQLite
- Streamlit-based UI dashboard
- Testing / mock mode for safe development

---

## Architecture Overview

Prompt Input  
→ Variation Engine  
→ LLM Gateway (Gemini)  
→ Evaluation Engine  
→ Feedback Generator  
→ SQLite Store + UI Dashboard

---

## Setup Instructions

### 1. Clone the Repository
```bash
git clone <repo-url>
cd ai-prompt-variation-analyzer

2. Create Virtual Environment
python -m venv venv
venv\Scripts\activate      # Windows

3. Install Dependencies
pip install -r requirements.txt

4. Configure Environment Variables
GEMINI_API_KEY=your_api_key_here

5. Running the Application
Run UI Dashboard -streamlit run ui/app.py
