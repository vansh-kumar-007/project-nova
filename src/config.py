"""
Project-wide configuration constants.
Keep simple and readable for beginners.
"""
from pathlib import Path

# Project root (parent folder of src/)
PROJECT_ROOT = Path(__file__).resolve().parents[1]

# Where we keep CSVs and other data artifacts
DATA_DIR = PROJECT_ROOT / "data"

# Reproducible seed for random operations
RANDOM_SEED = 42

# Columns we expect in the feature dataset (target is not included here)
REQUIRED_COLUMNS = [
    "partner_id",
    "monthly_earnings",
    "trips_per_week",
    "avg_rating",
    "cancellation_rate",
    "active_days_per_month",
    "avg_trip_distance_km",
    "transactions_last_3_months",
    "days_since_joining",
    "late_payment_count",
    "repairs_cost_last_6_months",
    "city",
    "vehicle_type",
    "peak_hour_percentage",
    "promotions_received_last_6_months",
]

# Name of the model target column (the Nova Score)
TARGET_COLUMN = "Nova_Score"
