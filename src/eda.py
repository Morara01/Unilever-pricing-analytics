import pandas as pd

def run_eda(df):
    print("\n Running Exploratory Data Analysis (EDA)...\n")

    
    # 1️ Pricing distribution
   
    print("Pricing distribution summary:")
    print(df["Recommended_selling_price"].describe(), "\n")

    
    # 2️ Outlier detection (IQR)
   
    Q1 = df["Recommended_selling_price"].quantile(0.25)
    Q3 = df["Recommended_selling_price"].quantile(0.75)
    IQR = Q3 - Q1

    outliers = df[
        (df["Recommended_selling_price"] < Q1 - 1.5 * IQR) |
        (df["Recommended_selling_price"] > Q3 + 1.5 * IQR)
    ]

    print(f"Outliers detected: {len(outliers)} products")

    
    # 3️ Average price comparisons
   
    print("\nAverage price by region:")
    print(
        df.groupby("Region")["Recommended_selling_price"]
        .mean()
        .sort_values(ascending=False),
        "\n"
    )

    if "Category" in df.columns:
        print("Average price by category:")
        print(
            df.groupby("Category")["Recommended_selling_price"]
            .mean()
            .sort_values(ascending=False),
            "\n"
        )

    print("Average price by brand strength:")
    print(
        df.groupby("Brand_Strength_Score")["Recommended_selling_price"]
        .mean()
        .head(),
        "\n"
    )

   
    # 4️ Margin misalignment
   
    if "Target_margin" in df.columns:
        df["Price_to_Margin_Ratio"] = (
            df["Recommended_selling_price"] / df["Target_margin"]
        )

        misaligned = df[
            (df["Price_to_Margin_Ratio"] < 0.9) |
            (df["Price_to_Margin_Ratio"] > 1.1)
        ]

        print(f"Products misaligned with margin expectations: {len(misaligned)}")

    print("\n EDA completed successfully\n")

    return df
