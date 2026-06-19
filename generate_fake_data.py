import csv
import random
from datetime import datetime, timedelta

random.seed(42)

test_names = ["test_login", "test_signup", "test_checkout", "test_search", 
              "test_payment", "test_profile_update", "test_logout", "test_cart_add"]
statuses = ["PASS", "FAIL", "SKIP"]
environments = ["dev", "qa", "staging", "prod"]

rows = []
start_date = datetime(2025, 1, 1)

for i in range(1000):
    row = {
        "test_id": f"TC-{1000+i}",
        "test_name": random.choice(test_names),
        "status": random.choices(statuses, weights=[70, 20, 10])[0],
        "environment": random.choice(environments),
        "duration_ms": random.randint(50, 5000),
        "date": (start_date + timedelta(days=random.randint(0, 180))).strftime("%Y-%m-%d")
    }
    rows.append(row)

with open("test_results.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=rows[0].keys())
    writer.writeheader()
    writer.writerows(rows)

print("Created test_results.csv with 1000 rows")