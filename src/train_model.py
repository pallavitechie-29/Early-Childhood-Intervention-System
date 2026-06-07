import pandas as pd
import joblib

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

from preprocessing import preprocess

df = pd.read_csv(
    "../data/app_usage_dataset_10k.csv"
)

df = preprocess(df)

X = df.drop(
    "intervention_required",
    axis=1
)

y = df["intervention_required"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = RandomForestClassifier(
    n_estimators=200,
    random_state=42
)

model.fit(X_train, y_train)

pred = model.predict(X_test)

print(
    classification_report(
        y_test,
        pred
    )
)

joblib.dump(
    model,
    "../models/intervention_model.pkl"
)
