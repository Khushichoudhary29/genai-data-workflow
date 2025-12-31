import pandas as pd

def preprocess_text(df: pd.DataFrame, text_column: str) -> pd.Series:
    """
    Select and clean text data for GenAI processing.
    """
    if text_column not in df.columns:
        raise ValueError(f"Column '{text_column}' not found in dataset")

    text_data = (
        df[text_column]
        .dropna()
        .astype(str)
        .str.strip()
    )

    return text_data


if __name__ == "__main__":
    from ingest import load_data

    df = load_data("data/amazon_review.csv")
    cleaned_text = preprocess_text(df, text_column="reviewText")

    # Sanity check (can remove later)
    print(cleaned_text.head())
