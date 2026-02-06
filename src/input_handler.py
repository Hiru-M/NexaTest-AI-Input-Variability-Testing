class InputHandler:
    def validate_prompt(self, prompt: str) -> str:
        if not prompt or not isinstance(prompt, str):
            raise ValueError("Prompt must be a non-empty string")

        prompt = prompt.strip()

        if len(prompt) < 10:
            raise ValueError("Prompt too short for analysis")

        return prompt
