import pandas as pd

df = pd.read_csv("test_results.csv")

# Basic exploration
print("Shape:", df.shape)
print("\nFirst 5 rows:")
print(df.head())
print("\nColumn info:")
print(df.info())
print("\nStatus counts:")
print(df["status"].value_counts())

print("\nFailed tests:")
failed_tests = df[df["status"] == "FAIL"]
print("Failed tests count:", len(failed_tests))
print(failed_tests.head())

print("\nAverage duration by environment:")
avg_duration = df.groupby("environment")["duration_ms"].mean()
print(avg_duration)

print("\nFailures by test name:")
failure_by_test = df[df["status"] == "FAIL"]["test_name"].value_counts()
print(failure_by_test)

print("\nFailure rate by test name (%):")
print(df["test_name"].value_counts())
total_by_test = df["test_name"].value_counts()
print("total_by_test",total_by_test)
failure_rate = (failure_by_test / total_by_test * 100).round(2)
print(failure_rate.sort_values(ascending=False))