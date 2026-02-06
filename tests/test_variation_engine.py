from src.variation_engine import PromptVariationEngine

def test_variation_count():
    engine = PromptVariationEngine(3)
    variations = engine.generate("Explain AI simply")
    assert len(variations) == 3
