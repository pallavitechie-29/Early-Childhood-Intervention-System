import pandas as pd
import numpy as np

np.random.seed(42)

n = 10000

data = {
    "age_group": np.random.choice(
        ["03-05", "06-08", "09-12"], n
    ),
    "app_category": np.random.choice(
        ["Games", "Education", "Social", "Utility"], n
    ),
    "duration_min": np.random.randint(5, 180, n),
    "frequency_last_7d": np.random.randint(1, 30, n),
    "emotion": np.random.choice(
        ["Happy", "Neutral", "Sad"], n
    ),
    "time_of_day": np.random.choice(
        ["Morning", "Afternoon", "Evening", "Night"], n
    )
}

df = pd.DataFrame(data)

df["intervention_required"] = (
    (df["duration_min"] > 90)
    | (df["frequency_last_7d"] > 20)
).astype(int)

df.to_csv(
    "app_usage_dataset_10k.csv",
    index=False
)

print("Dataset Generated")
