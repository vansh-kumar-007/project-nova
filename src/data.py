"""
Data helpers for Project Nova.

This file contains:
- small helpers to load/save CSVs
- a tiny 'get_sample_data' function you can use immediately to test imports
- a schema validator to check required columns before modeling

All functions are short and documented so they are easy to read.
"""
from pathlib import Path
from typing import Union, List
import pandas as pd
import numpy as np
import random

from .config import DATA_DIR, RANDOM_SEED, REQUIRED_COLUMNS, TARGET_COLUMN

def set_random_seed(seed: int = RANDOM_SEED):
    """Set reproducible seeds for python's random and numpy."""
    import os
    random.seed(seed)
    np.random.seed(seed)
    os.environ['PYTHONHASHSEED'] = str(seed)

def load_csv(path: Union[str, Path]) -> pd.DataFrame:
    """
    Load a CSV into a pandas DataFrame.
    Raises FileNotFoundError if the path doesn't exist.
    """
    path = Path(path).expanduser().resolve()
    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")
    return pd.read_csv(path)

def save_csv(df: pd.DataFrame, path: Union[str, Path], index: bool = False) -> None:
    """
    Save DataFrame to CSV; creates parent folder if needed.
    """
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=index)

def validate_schema(df: pd.DataFrame) -> List[str]:
    """
    Return a list of missing required columns. Empty list => OK.
    This helps to catch mistakes early.
    """
    missing = [c for c in REQUIRED_COLUMNS if c not in df.columns]
    return missing

def get_sample_data(n: int = 5) -> pd.DataFrame:
    """
    Build a tiny sample DataFrame with realistic-looking columns.
    NOTE: this is only for quick smoke tests (imports, notebook flow).
    The real synthetic dataset (thousands of rows) will be generated later.
    """
    set_random_seed()
    rows = []
    for i in range(n):
        rows.append({
            "partner_id": f"P{i+1:04d}",
            "monthly_earnings": round(abs(np.random.normal(30000, 8000)), 2),
            "trips_per_week": int(max(0, np.random.poisson(30))),
            "avg_rating": round(min(5.0, max(1.0, np.random.normal(4.6, 0.3))), 2),
            "cancellation_rate": round(min(1.0, max(0.0, np.random.beta(1, 10))), 3),
            "active_days_per_month": int(max(1, np.random.randint(5, 30))),
            "avg_trip_distance_km": round(max(0.5, np.random.normal(7, 3)), 2),
            "transactions_last_3_months": int(max(0, np.random.poisson(40))),
            "days_since_joining": int(abs(np.random.exponential(400))),
            "late_payment_count": int(np.random.poisson(0.5)),
            "repairs_cost_last_6_months": round(abs(np.random.normal(500, 400)), 2),
            "city": np.random.choice(["Delhi", "Mumbai", "Bengaluru", "Chennai", "Kolkata"]),
            "vehicle_type": np.random.choice(["Bike", "Car", "Auto"]),
            "peak_hour_percentage": round(min(1.0, abs(np.random.normal(0.35, 0.15))), 3),
            "promotions_received_last_6_months": int(np.random.poisson(2)),
            TARGET_COLUMN: round(min(100, max(0, np.random.normal(65, 12))), 2),
        })
    df = pd.DataFrame(rows)
    return df
