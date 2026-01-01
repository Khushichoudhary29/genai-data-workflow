def generate_insights(reviews: list[str]) -> str:
    """
    Generate structured insights from customer reviews using Gemini.
    """
    if not reviews:
        raise ValueError("No reviews provided for insight generation")

    joined_reviews = "\n".join(reviews)

    with open("src/prompts/review_summary.txt", "r") as f:
        prompt_template = f.read()

    prompt = prompt_template.replace("{{REVIEWS}}", joined_reviews[:6000])

    # PSEUDO-CODE: Gemini API integration happens here
    # response = gemini_model.generate(prompt)

    response = "Gemini response placeholder (API integration pending)"

    return response


if __name__ == "__main__":
    # Simple local test (architecture validation)
    sample_reviews = [
        "Battery life is great but camera quality is average.",
        "Excellent performance, heats up sometimes.",
        "Value for money, display is very sharp."
    ]

    print(generate_insights(sample_reviews))
