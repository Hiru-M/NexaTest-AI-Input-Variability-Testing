import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from src.input_handler import InputHandler


class EvaluationEngine:
    def __init__(self, embedding_model):
        self.embedding_model = embedding_model

    def embed(self, texts: list[str]) -> np.ndarray:
        return np.array(self.embedding_model.encode(texts))

    def semantic_similarity(self, embeddings: np.ndarray) -> float:
        matrix = cosine_similarity(embeddings)
        upper_triangle = matrix[np.triu_indices(len(matrix), k=1)]
        return float(upper_triangle.mean())

    def consistency_score(self, embeddings: np.ndarray) -> float:
        return 1.0 - float(np.std(embeddings))

    def evaluate(self, responses: list[str]) -> dict:
        embeddings = self.embedding_model.encode(responses)

        similarity_matrix = cosine_similarity(embeddings)
        avg_similarity = float(
            similarity_matrix[np.triu_indices(len(similarity_matrix), k=1)].mean()
        )

        consistency = 1.0 - float(np.std(embeddings))

        return {
            "average_similarity": round(avg_similarity, 3),
            "consistency_score": round(consistency, 3)
        }