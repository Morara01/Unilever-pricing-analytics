import pandas as pd
from sklearn.cluster import KMeans

def assign_tier(score):
    if score <= 3:
        return "Value"
    elif score <= 7:
        return "Standard"
    return "Premium"


def engineer_features(df: pd.DataFrame) -> pd.DataFrame:
    """Apply feature engineering to merged pricing data."""

    df = df.copy()

    # 1️ Price Tier
    df["Price_Tier"] = df["Brand_Strength_Score"].astype(int).apply(assign_tier)

    # 2️ Recommended Price (guard in case column not present)
    if "Recommended_selling_price" not in df.columns:
        df["Recommended_selling_price"] = df["Base_Cost"] * (1 + df["Target_margin"])

    # 3️ Price-to-Margin Ratio
    df["Price_to_Margin_Ratio"] = df["Recommended_selling_price"] / df["Target_margin"]

    # 4️ Binary Premium Flag
    df["Is_Premium"] = (df["Price_Tier"] == "Premium").astype(int)

    # 5️ Clustering (Strategic segmentation)
    kmeans = KMeans(n_clusters=3, random_state=42)
    df["Cluster"] = kmeans.fit_predict(
        df[["Brand_Strength_Score", "Base_Cost"]]
    )

    return df
