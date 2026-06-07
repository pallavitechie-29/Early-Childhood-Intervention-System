import joblib

model = joblib.load(
    "../models/intervention_model.pkl"
)

def predict_intervention(data):

    result = model.predict(data)

    return result
