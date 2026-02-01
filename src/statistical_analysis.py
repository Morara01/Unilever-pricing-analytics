import pandas as pd
from pathlib import Path
from scipy import stats

BASE_DIR = Path(__file__).resolve().parents[1]
DATA_PATH = BASE_DIR / "data" / "processed" / "unilever_enriched_python.xlsx"


def brand_strength_price_correlation():
    df = pd.read_excel(DATA_PATH)

    corr, p_value = stats.pearsonr(
        df["Brand_Strength_Score"],
        df["Recommended_selling_price"]
    )

    print("\n Brand Strength vs Price Correlation")
    print(f"Correlation: {corr:.3f}")
    print(f"P-value: {p_value:.5f}")

    return corr, p_value

def regional_price_ttest(region_a="UK", region_b="Germany"):
    df = pd.read_excel(DATA_PATH)

    prices_a = df[df["Region"] == region_a]["Recommended_selling_price"]
    prices_b = df[df["Region"] == region_b]["Recommended_selling_price"]

    t_stat, p_value = stats.ttest_ind(
        prices_a,
        prices_b,
        equal_var=False
    )

    print(f"\n T-Test: {region_a} vs {region_b}")
    print(f"T-statistic: {t_stat:.3f}")
    print(f"P-value: {p_value:.5f}")

    return t_stat, p_value

def scipy_price_regression():
    df = pd.read_excel(DATA_PATH)

    slope, intercept, r_value, p_value, std_err = stats.linregress(
        df["Brand_Strength_Score"],
        df["Recommended_selling_price"]
    )

    print("\n SciPy Linear Regression (Baseline)")
    print(f"Price = {intercept:.2f} + {slope:.2f} * Brand_Strength")
    print(f"R²: {r_value**2:.3f}")
    print(f"P-value: {p_value:.5f}")

    return {
        "slope": slope,
        "intercept": intercept,
        "r_squared": r_value**2,
        "p_value": p_value
    }

def run_statistical_analysis():
    brand_strength_price_correlation()
    regional_price_ttest("UK", "Germany")
    scipy_price_regression()


if __name__ == "__main__":
    run_statistical_analysis()
