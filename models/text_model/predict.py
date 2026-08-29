import os
import joblib
import pandas as pd


# ==================================================
# 1. LOAD TRAINED MODEL
# ==================================================

MODEL_PATH = os.path.join(
    os.path.dirname(__file__),
    "saved_model",
    "verbal_autopsy_model.pkl"
)

model = joblib.load(MODEL_PATH)


# ==================================================
# 2. PREDICTION FUNCTION
# ==================================================

def predict_cause(patient_data):

    # Convert dictionary → DataFrame
    patient_df = pd.DataFrame([patient_data])

    # Predict cause
    prediction = model.predict(patient_df)[0]

    # Get probability for each class
    probabilities = model.predict_proba(patient_df)[0]

    # Get class names
    classes = model.classes_

    # Combine cause + probability
    results = list(zip(classes, probabilities))

    # Sort highest probability first
    results.sort(
        key=lambda x: x[1],
        reverse=True
    )

    return prediction, results


# ==================================================
# 3. TEST PREDICTION this is the manual test case
# ==================================================

if __name__ == "__main__":

    patient = {
        "fever": "yes",
        "cough": "yes",
        "difficulty_breathing": "yes",
        "fast_breathing": "yes",
        "chest_pain": "no",

        "diarrhea": "no",
        "blood_in_stool": "no",
        "vomiting": "no",
        "blood_in_vomit": "no",
        "abdominal_pain": "no",
        "protruding_abdomen": "no",

        "severe_headache": "no",
        "stiff_neck": "no",
        "convulsions": "no",
        "unconscious": "no",
        "paralysis": "no",

        "skin_rash": "no",
        "yellow_eyes_jaundice": "no",
        "swollen_legs_feet": "no",
        "weight_loss": "no",
        "night_sweats": "no",

        "road_traffic_accident": "no",
        "fall_injury": "no",
        "poisoning": "no",
        "died_suddenly": "no",

        "pregnant_at_death": "no",
        "excessive_bleeding_delivery": "no",

        "age_group": "adult"
    }


    # ==================================================
    # RUN PREDICTION
    # ==================================================

    prediction, probabilities = predict_cause(patient)


    print("\n" + "=" * 50)
    print("VERBAL AUTOPSY PREDICTION")
    print("=" * 50)

    print(f"\nPredicted Cause: {prediction}")

    print("\nProbabilities:")

    for cause, probability in probabilities:
        print(f"{cause:<35} {probability:.2%}")

    print("=" * 50)

