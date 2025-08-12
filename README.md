# Project Nova — Day 1: Setup & Plan

## Project overview
Build an alternative credit scoring model ("Nova Score") for platform partners using platform activity (earnings, trips, ratings, transactions, etc.). The model should be accurate, explainable, and include fairness analysis and mitigation.

## High-level goals
1. Create synthetic dataset representative of platform partners.
2. Train baseline models (Linear, RandomForest, XGBoost) to predict Nova Score.
3. Evaluate models for accuracy and fairness; apply mitigation strategies.
4. Produce a short report + slides demonstrating results and fairness analysis.

## Acceptance criteria (minimum)
- Working Jupyter notebooks for data generation, EDA, modeling, and fairness.
- At least one fairness metric computed and at least one mitigation applied.
- Short presentation (6–8 slides) and README explaining how to run everything.

## Starter feature list (we will generate synthetic data using these)
- partner_id (unique)
- monthly_earnings
- trips_per_week
- avg_rating (1.0 - 5.0)
- cancellation_rate (0-1)
- active_days_per_month
- avg_trip_distance_km
- transactions_last_3_months
- days_since_joining
- late_payment_count (last 12 months)
- repairs_cost_last_6_months
- city (categorical)
- vehicle_type (categorical)
- peak_hour_percentage (0-1)
- promotions_received_last_6_months

## Target
- Nova_Score (continuous 0-100) — initially simulated as a weighted function of features plus noise.

## Today (Day 1) checklist
- [ ] Repo skeleton (done)
- [ ] Conda env (done)
- [ ] Jupyter notebook created (done)
- [ ] Notebook populated with this plan (YOU DO THIS)
- [ ] Export conda env file (optional, recommended)

## Next steps after this notebook
1. Create `src/` helper files (data loaders & utils).
2. Generate first synthetic dataset (5–10k rows).
3. Start EDA and feature engineering.
