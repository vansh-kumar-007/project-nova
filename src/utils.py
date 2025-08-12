"""
Small utility helpers used across notebooks and scripts.
Keep them tiny and easy to read.
"""
from pathlib import Path
import os
import numpy as np
import random

def ensure_dir(path):
    """
    Create directory (and parents) if it does not exist.
    path may be a string or Path.
    """
    Path(path).mkdir(parents=True, exist_ok=True)

def set_seed(seed=42):
    """
    Set seeds for reproducibility for python's random and numpy.
    Call this at the top of scripts / notebooks when you need reproducible tests.
    """
    random.seed(seed)
    np.random.seed(seed)
    os.environ['PYTHONHASHSEED'] = str(seed)
