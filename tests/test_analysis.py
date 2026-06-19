import pandas as pd
import pytest

@pytest.fixture
def df():
    return pd.read_csv("test_results.csv")

def test_data_loaded_correctly(df):
    assert len(df) == 1000

def test_no_missing_values(df):
    assert df.isnull().sum().sum() == 0

def test_status_values_valid(df):
    valid_statuses = {"PASS", "FAIL", "SKIP"}
    assert set(df["status"].unique()).issubset(valid_statuses)

def test_duration_is_positive(df):
    assert (df["duration_ms"] > 0).all()