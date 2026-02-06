import random
from src.input_handler import InputHandler


class PromptVariationEngine:
    def __init__(self, variation_count: int):
        self.variation_count = variation_count

    def generate(self, base_prompt: str) -> list[str]:
        variations = [base_prompt]

        strategies = [
            self._synonym_variation,
            self._structural_variation,
            self._instruction_variation
        ]

        for _ in range(self.variation_count - 1):
            strategy = random.choice(strategies)
            variations.append(strategy(base_prompt))

        return variations

    def _synonym_variation(self, prompt: str) -> str:
        return prompt.replace("explain", "describe", 1)

    def _structural_variation(self, prompt: str) -> str:
        return f"In simple terms, {prompt}"

    def _instruction_variation(self, prompt: str) -> str:
        return f"Please answer clearly: {prompt}"
