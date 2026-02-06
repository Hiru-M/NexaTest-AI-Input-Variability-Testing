from src.main import run_analysis

if __name__ == "__main__":
    result = run_analysis("Explain AI simply", mock_llm=True)
    print(result)
