Executive Summary
Unilever Europe – Large-Scale Pricing Strategy & Margin Optimization Analysis (5,000 SKUs)
Prepared by: George Morara
Role Perspective: Pricing Data Analyst
Scope: UK, France, Germany, Spain
Dataset Size: ~5,000 product records
Time Horizon: Current pricing cycle with forward-looking recommendations

1. Strategic Context
Unilever operates a high-complexity, multi-market product portfolio where pricing decisions directly influence margin realization, brand positioning, and competitive advantage. As portfolio size scales into the thousands of SKUs, manual or heuristic-based pricing becomes structurally inefficient, increasing the risk of:
* Margin leakage
* Inconsistent regional pricing logic
* Misclassification of premium vs value products
* Over- or under-pricing relative to brand equity

This analysis was commissioned to quantitatively assess and optimize pricing strategy across ~5,000 products, integrating commercial, brand, and finance perspectives into a single decision framework.

2. Objectives
The project was designed to answer five executive-level questions:

2.1. Are current prices aligned with regional margin targets?
2.2 Do brand strength signals justify premium pricing across markets?
2.3 Where does pricing dispersion indicate risk or inefficiency?
2.4 Can we predict optimal pricing using historical patterns?
2.5 How can pricing decisions be made probabilistically rather than subjectively?

3. Data & Methodology Overview
Data Sources
* Product Master Data: Base cost, brand strength score, category, region (~5,000 SKUs)
* Finance Targets: Region-specific margin expectations (Excel input)
* Derived Metrics: Recommended selling price, price tiers, efficiency ratios

Analytical Pipeline
1. Data ingestion & validation
2. Feature engineering (pricing logic, tiers, efficiency ratios)
3. Exploratory data analysis (EDA)
4. Statistical testing (significance & confidence)
5. Machine learning (regression & classification)
6. Executive visualization & reporting

4. Key Findings (High-Impact)
4.1 Regional Pricing Performance

Average Recommended Price by Region
* UK: Highest average prices; strong brand leverage but margin slightly under-realized
* Germany: Most balanced market; pricing closely tracks finance expectations
* France: Systematic under-pricing detected relative to margin targets
* Spain: Volume-led pricing strategy; lowest prices but margin pressure evident

Insight: Pricing logic is not uniformly applied across regions. Market maturity and brand perception are influencing decisions more than margin discipline in some territories.

4.2 Margin Alignment Analysis

A comparison between actual recommended prices and finance-implied target prices reveals:
* ~18–22% of SKUs fall outside acceptable margin bands
* France and Spain account for the highest concentration of under-margin products
* Germany demonstrates the lowest pricing volatility

Commercial Risk: Left uncorrected, these deviations compound into material annual margin leakage at scale.

4.3 Price Distribution & Risk Exposure

Price distribution analysis across all 5,000 SKUs shows:
* A heavy right-skew driven by premium products
* A long tail of low-priced SKUs with thin margins
* Outliers indicating inconsistent pricing logic, particularly within the same brand tiers

Strategic Implication: Outliers represent immediate candidates for price correction or portfolio rationalization.

4.4 Brand Strength vs Price Justification

Scatter analysis confirms a strong positive relationship between brand strength score and price:
* High brand strength reliably supports premium pricing
* However, ~9% of products are priced as premium without sufficient brand justification
* Conversely, several strong brands are undervalued in price

Actionable Insight: Brand equity is not being fully monetized in certain segments, while others are exposed to brand dilution risk.

5. Statistical Validation
To ensure insights are not anecdotal:

* T-tests confirm statistically significant price differences between UK and Germany (p < 0.05)
* Regression analysis shows brand strength and base cost explain the majority of price variance
* Noise variables contribute minimally, reinforcing model reliability

6. Machine Learning & Predictive Pricing
6.1 Price Prediction (Linear Regression)

* Model predicts recommended prices with low error margins
* Enables scenario analysis:
    * Cost increases
    * Margin target changes
    * Brand repositioning
Use Case: Pricing teams can simulate future decisions before market execution.

6.2 Probability-Based Premium Classification (Logistic Regression)

Each product is assigned a probability of being truly “Premium”, rather than a binary label.
Probability Band	Interpretation	Action
≥ 75%	Strong Premium	Defend / increase price
50–75%	Borderline Premium	Test & monitor
< 50%	Standard / Value	Reposition or reprice

Strategic Advantage: Moves pricing from opinion-based to probability-driven decision-making.

7. Strategic Recommendations
Immediate (0–3 months)
* Correct under-priced SKUs in France & Spain
* Reprice undervalued strong brands in the UK
* Review premium outliers lacking brand justification

Medium Term (3–9 months)
* Adopt probability-based premium classification in pricing governance
* Integrate pricing model into product launch workflows
* Monitor price-to-margin ratios monthly

Long Term (12+ months)
* Scale model to promotional pricing & elasticity analysis
* Integrate competitor pricing feeds
* Automate executive reporting dashboards

8. Business Impact
If applied portfolio-wide, this framework enables:
* Margin recovery at scale
* Consistent, defensible pricing decisions
* Reduced reliance on manual judgment
* Faster response to market and cost changes

9. Conclusion
This 5,000-SKU analysis proves that pricing is not just a finance or marketing problem — it is a data problem.
By integrating:
* Clean data pipelines
* Statistical validation
* Machine learning
* Executive-grade visualization