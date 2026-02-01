from src import data_loader, feature_engineering, modeling, visualization
from src.statistical_analysis import run_statistical_analysis

def run_pipeline():
    print("Starting Unilever Pricing Analytics Pipeline...\n")

    # Step 1: Merge raw data
    print("Step 1 — Merging raw data...")
    merged_df = data_loader.merge_data()
    print(f"Data merged: {merged_df.shape[0]} rows, {merged_df.shape[1]} columns\n")

    # Step 2: Feature engineering
    print("Step 2 — Feature engineering...")
    enriched_df = feature_engineering.engineer_features(merged_df)
    print(f"Features engineered: {enriched_df.shape[0]} rows, {enriched_df.shape[1]} columns\n")
    print(enriched_df.head(), "\n")

    # Step 3: Modeling
    print("Step 3 — Running machine learning models...")
    modeling.run_models(enriched_df)
    print("Machine learning step complete\n")

    # Step 4: Statistical analysis
    print("Step 4 — Statistical Validation (SciPy)...")
    run_statistical_analysis()


    # Step 5: Visualization
    print("Step 5 — Creating executive charts...")
    visualization.plot_price_by_region()
    visualization.plot_price_vs_brand_strength()
    visualization.plot_price_vs_margin()
    visualization.plot_price_distribution()

    print("Charts created and saved in reports/charts\n")

    print("Pipeline finished successfully!")

if __name__ == "__main__":
    run_pipeline()