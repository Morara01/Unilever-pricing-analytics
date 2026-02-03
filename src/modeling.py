import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import r2_score, mean_absolute_error, classification_report
from sklearn.cluster import KMeans
from pathlib import Path


def run_models(df: pd.DataFrame):
    """
    Runs price prediction and premium classification models
    """

    print("Running Linear & Logistic Regression models...")

    
    # Feature selection
    
    features = ["Brand_Strength_Score", "Target_margin", "Base_Cost"]

    X = df[features]
    y_price = df["Recommended_selling_price"]
    y_premium = df["Is_Premium"]

    # Linear Regression (Price)
   
    X_train, X_test, y_train, y_test = train_test_split(
        X, y_price, test_size=0.25, random_state=42
    )

    lin_model = LinearRegression()
    lin_model.fit(X_train, y_train)

    y_pred = lin_model.predict(X_test)

    print("\nLinear Regression Results")
    print("R² Score:", round(r2_score(y_test, y_pred), 3))
    print("MAE (£):", round(mean_absolute_error(y_test, y_pred), 2))

    
    # Logistic Regression (Premium)
   
    X_train, X_test, y_train, y_test = train_test_split(
        X, y_premium, test_size=0.25, random_state=42
    )

    log_model = LogisticRegression(max_iter=1000)
    log_model.fit(X_train, y_train)

    premium_probs = log_model.predict_proba(X_test)[:, 1]
    y_pred_class = log_model.predict(X_test)

    print("\nLogistic Regression Results")
    print(classification_report(y_test, y_pred_class))

    
    # Attach probabilities back
    
    results_df = df.loc[X_test.index, [
    "Region",
    "Category",
    "Recommended_selling_price",
    "Brand_Strength_Score",
    "Target_margin",
    "Base_Cost"
    ]].copy()
    results_df["Actual_Is_Premium"] = y_test.values
    results_df["Premium_Probability"] = premium_probs

    # probability based segmentation
    def classify_probability(prob):
        if prob >= 0.75:
            return "Strong Premium"
        elif prob >= 0.5:
            return "Borderline Premium"
        else:
            return "Standard / Value"
    results_df["Premium_Segment"] = results_df["Premium_Probability"].apply(classify_probability)

    print("\nPremium Probability Segmentation (Sample):")
    print(
        results_df[
            ["Premium_Probability", "Premium_Segment"]
        ].head(10)
    )

    print("\nPremium Segment Distribution:")
    print(results_df["Premium_Segment"].value_counts())

    # Clustering (Strategic segmentation)
    kmeans = KMeans(n_clusters=3, random_state=42)
    df["Cluster"] = kmeans.fit_predict(
        df[["Brand_Strength_Score", "Base_Cost"]]
    )
    print("\nCluster Centers (Interpretation Reference):")
    cluster_centers = pd.DataFrame(
        kmeans.cluster_centers_,
        columns=["Brand_Strength_Score", "Base_Cost"]
    )
    print(cluster_centers)

    cluster_summary = (
        df.groupby("Cluster")
        .agg(
            Avg_Brand_Strength=("Brand_Strength_Score", "mean"),
            Avg_Base_Cost=("Base_Cost", "mean"),
            Avg_Price=("Recommended_selling_price", "mean"),
            Product_Count=("Cluster", "count")
        )
        .reset_index()
    )
    print("\nCluster Summary (Strategic Segments):")
    print(cluster_summary)

    # Cluster naming for interpretability
    def label_cluster(row):
        if row["Avg_Brand_Strength"] > 7:
            return "Premium Core Brands"
        elif row["Avg_Base_Cost"] > 4:
            return "High-Cost / Low-Brand Risk"
        else:
            return "Value & Volume Products"
    cluster_summary["Cluster_Label"] = cluster_summary.apply(label_cluster, axis=1)
    print("\nCluster Business Labels:")
    print(cluster_summary[["Cluster", "Cluster_Label"]])

    print("Sample Premium Probabilities:")
    print(results_df.head())

    BASE_DIR = Path(__file__).resolve().parents[1]
    PROCESSED_DIR = BASE_DIR / "data" / "processed"
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    MODEL_OUTPUT_PATH = PROCESSED_DIR / "model_outputs.xlsx"

    results_df.to_excel(MODEL_OUTPUT_PATH, index=False)
    print(f"Model outputs saved to {MODEL_OUTPUT_PATH}")

    return results_df
