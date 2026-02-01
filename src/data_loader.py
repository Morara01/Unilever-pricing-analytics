from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent
RAW_DATA = BASE_DIR / "data" / "raw"

def load_raw_data():
    products = pd.read_excel(RAW_DATA / "unilever_products7.xlsx")
    finance = pd.read_excel(RAW_DATA / "Finance_targets7.xlsx")
    return products, finance


def merge_data():
    products, finance = load_raw_data()

    merged_df = products.merge(
        finance,
        on="Region",
        how="left"
    )

    return merged_df