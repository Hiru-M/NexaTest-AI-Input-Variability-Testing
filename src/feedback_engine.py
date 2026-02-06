from src.input_handler import InputHandler

class FeedbackEngine:
    def generate(self, similarity: float) -> dict:
        feedback = {
            "summary": "",
            "recommendations": []
        }

        if similarity > 0.85:
            feedback["summary"] = "Prompt is robust to phrasing changes."
        else:
            feedback["summary"] = "Prompt is sensitive to phrasing variations."
            feedback["recommendations"].append(
                "Simplify wording and avoid ambiguous instructions."
            )

        return feedback
