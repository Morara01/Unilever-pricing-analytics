import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Paths

BASE_DIR = Path(__file__).resolve().parents[1]
DATA_PATH = BASE_DIR / "data" / "processed" / "unilever_enriched_python.xlsx"
CHARTS = BASE_DIR / "reports" / "charts"
CHARTS.mkdir(exist_ok=True)


# 1️ Average Price by Region

def plot_price_by_region():
    df = pd.read_excel(DATA_PATH)

    summary = (
        df.groupby("Region")["Recommended_selling_price"]
        .mean()
        .reset_index()
    )

    plt.figure(figsize=(8, 5))
    bars = plt.bar(summary["Region"], summary["Recommended_selling_price"])

    for bar in bars:
        h = bar.get_height()
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            h,
            f"£{h:.2f}",
            ha="center",
            va="bottom"
        )

    plt.title("Average Recommended Price by Region")
    plt.ylabel("Price (£)")
    plt.grid(axis="y", linestyle="--", alpha=0.6)
    plt.tight_layout()
    plt.savefig(CHARTS / "avg_price_by_region.png")
    plt.close()


# 2️ Target Margin vs Avg Price

def plot_price_vs_margin():
    df = pd.read_excel(DATA_PATH)

    summary = (
        df.groupby("Region")
        .agg(
            Avg_Price=("Recommended_selling_price", "mean"),
            Target_margin=("Target_margin", "mean")
        )
        .reset_index()
    )

    plt.figure(figsize=(8, 5))

    plt.plot(
        summary["Region"],
        summary["Avg_Price"],
        marker="o",
        label="Average Price (£)"
    )

    plt.plot(
        summary["Region"],
        summary["Avg_Price"] * summary["Target_margin"],
        marker="o",
        linestyle="--",
        label="Implied Margin Value (£)"
    )

    plt.title("Average Price vs Finance Target Margin")
    plt.xlabel("Region")
    plt.ylabel("£")
    plt.legend()
    plt.grid(alpha=0.4)
    plt.tight_layout()
    plt.savefig(CHARTS / "price_vs_margin.png")
    plt.close()


# 3️ Price Distribution (EDA)

def plot_price_distribution():
    df = pd.read_excel(DATA_PATH)

    plt.figure(figsize=(8, 5))
    plt.hist(
        df["Recommended_selling_price"],
        bins=30
    )

    plt.title("Distribution of Recommended Prices")
    plt.xlabel("Price (£)")
    plt.ylabel("Number of Products")
    plt.grid(alpha=0.4)
    plt.tight_layout()
    plt.savefig(CHARTS / "price_distribution.png")
    plt.close()


# 4️ Price vs Brand Strength

def plot_price_vs_brand_strength():
    df = pd.read_excel(DATA_PATH)

    plt.figure(figsize=(8, 5))
    plt.scatter(
        df["Brand_Strength_Score"],
        df["Recommended_selling_price"],
        alpha=0.6
    )

    plt.title("Price vs Brand Strength")
    plt.xlabel("Brand Strength Score")
    plt.ylabel("Recommended Price (£)")
    plt.grid(alpha=0.4)
    plt.tight_layout()
    plt.savefig(CHARTS / "price_vs_brand_strength.png")
    plt.close()


# Main runner

if __name__ == "__main__":
    plot_price_by_region()
    plot_price_vs_margin()
    plot_price_distribution()
    plot_price_vs_brand_strength()

    print("All charts created successfully")
