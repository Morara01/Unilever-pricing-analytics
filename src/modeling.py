import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import r2_score, mean_absolute_error, classification_report


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
    
    results_df = X_test.copy()
    results_df["Actual_Is_Premium"] = y_test.values
    results_df["Premium_Probability"] = premium_probs

    print("Sample Premium Probabilities:")
    print(results_df.head())

    return results_df
