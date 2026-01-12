import subprocess

def generate_insights(reviews):
    prompt = f"""
You are a data analyst.
Analyze the following product reviews and summarize:
1. Common positive themes
2. Common complaints
3. Overall sentiment

Reviews:
{reviews}
"""

    result = subprocess.run(
    ["ollama", "run", "llama3"],
    input=prompt,
    text=True,
    encoding="utf-8",
    errors="ignore",
    capture_output=True
)


    return result.stdout


if __name__ == "__main__":
    sample_reviews = """
    Battery life is excellent and lasts all day.
    Camera quality is poor in low light.
    Fast performance and smooth display.
    Overheats while gaming.
    """

    print(generate_insights(sample_reviews))
