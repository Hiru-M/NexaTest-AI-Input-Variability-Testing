import os
from src.input_handler import InputHandler
from src.variation_engine import PromptVariationEngine
from src.llm_gateway import LLMGateway
from src.evaluation_engine import EvaluationEngine
from src.feedback_engine import FeedbackEngine
from src.db.sqlite_store import SQLiteStore
from src.utils.embeddings import EmbeddingModel


def run_analysis(prompt: str, mock_llm: bool = True):
    input_handler = InputHandler()
    validated_prompt = input_handler.validate_prompt(prompt)

    variations = PromptVariationEngine(5).generate(validated_prompt)

    llm = LLMGateway(
        model="gemini-2.5-flash",
        mock=mock_llm
    )

    responses = [llm.generate(p) for p in variations]

    embedding_model = EmbeddingModel()
    evaluator = EvaluationEngine(embedding_model)

    metrics = evaluator.evaluate(responses)

    similarity = metrics["average_similarity"]
    consistency = metrics["consistency_score"]

    feedback = FeedbackEngine().generate(similarity)

    db = SQLiteStore("prompt_analysis.db")
    db.save_run(prompt, similarity)

    return {
        "variations": variations,
        "responses": responses,
        "metrics": metrics,
        "feedback": feedback
    }
