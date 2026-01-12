import pandas as pd

def load_data(file_path: str) -> pd.DataFrame:
    """
    Load raw dataset from CSV file.
    """
    try:
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        raise RuntimeError(f"Failed to load data: {e}")

if __name__ == "__main__":
    data = load_data("data/amazon_review.csv")
    print(data.head())
    
    print(data.columns)
    print(data.head(3))
