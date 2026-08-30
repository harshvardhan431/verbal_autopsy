
import os
import sys

# ==================================================
# PROJECT ROOT
# ==================================================

PROJECT_ROOT = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)


# ==================================================
# IMPORT SERVICES
# ==================================================

from services.question_analyzer import analyze_question
from services.symptom_extractor import (
    extract_symptoms,
    extract_age_group
)

from services.dataset_query import (
    count_condition,
    most_common,
    value_counts,
    percentage_condition,
)

from models.text_model.predict import predict_cause


# ==================================================
# DATASET QUESTIONS
# ==================================================

def handle_dataset_question(intent, columns, value):

    if intent == "COUNT":

        if not columns:
            return "Please specify what you want me to count."

        column = columns[0]

        count = count_condition(column, value)

        return f"There are {count} records where {column} = {value}."


    if intent == "PERCENTAGE":

        if not columns:
            return "Please specify the condition."

        column = columns[0]

        percentage = percentage_condition(
            column,
            value
        )

        return f"{percentage}% of records have {column} = {value}."


    if intent == "MOST_COMMON":

        column = (
            columns[0]
            if columns
            else "cause_of_death"
        )

        result = most_common(column)

        return f"The most common {column} is: {result}."


    if intent == "DISTRIBUTION":

        column = (
            columns[0]
            if columns
            else "cause_of_death"
        )

        distribution = value_counts(column)

        return distribution.to_string()


    return "I could not understand the dataset question."


# ==================================================
# PREDICTION
# ==================================================

def handle_prediction(question):

    # ----------------------------------------------
    # Extract symptoms from natural language
    # ----------------------------------------------

    symptoms = extract_symptoms(question)

    age_group = extract_age_group(question)
    if age_group is None:
        return "Please provide the patient's age or age group."

    symptoms["age_group"] = age_group


    # ----------------------------------------------
    # Check whether symptoms were found
    # ----------------------------------------------

    detected_symptoms = [
        symptom
        for symptom, value in symptoms.items()
        if value == "yes"
    ]

    if not detected_symptoms:

        return (
            "I could not identify any symptoms. "
            "Please describe the patient's symptoms."
        )


    # ----------------------------------------------
    # Add age group
    # ----------------------------------------------

    # Temporary default.
    # We will build proper age extraction later.
    
    # ----------------------------------------------
    # Predict
    # ----------------------------------------------

    prediction, probabilities = predict_cause(
        symptoms
    )


    # ----------------------------------------------
    # Build response
    # ----------------------------------------------

    response = (
        f"Detected symptoms: "
        f"{', '.join(detected_symptoms)}\n\n"
        f"age group:{age_group}\n\n"
    )

    response += (
        f"Model-predicted cause: "
        f"{prediction}\n\n"
    )

    response += "Top predictions:\n"

    for cause, probability in probabilities[:3]:

        response += (
            f"- {cause}: "
            f"{probability:.2%}\n"
        )


    response += (
        "\nThis is a model prediction for "
        "decision support, not a medical diagnosis."
    )

    return response


# ==================================================
# MAIN ROUTER
# ==================================================

def route_question(question):

    # ----------------------------------------------
    # Analyze question
    # ----------------------------------------------

    analysis = analyze_question(question)

    intent = analysis["intent"]
    columns = analysis["columns"]
    value = analysis["value"]


    # ----------------------------------------------
    # Prediction
    # ----------------------------------------------

    if intent == "PREDICTION":

        return handle_prediction(question)


    # ----------------------------------------------
    # Dataset question
    # ----------------------------------------------

    if intent in [
        "COUNT",
        "PERCENTAGE",
        "MOST_COMMON",
        "DISTRIBUTION",
    ]:

        return handle_dataset_question(
            intent,
            columns,
            value
        )


    # ----------------------------------------------
    # Unknown
    # ----------------------------------------------

    return (
        "I couldn't understand your question. "
        "Please upload an image to get more information."
    )


# ==================================================
# TEST
# ==================================================

if __name__ == "__main__":

    questions = [

        "How many people had fever?",

        "What percentage of people had cough?",

        "What is the most common cause of death?",

        "The patient had fever, cough and difficulty breathing.",

        "The patient had severe headache and convulsions.",

        "The patient had fever but no cough.",

        "what is the most common disease?",
       " A 15 year old patient had fever, cough and difficulty breathing."
    ]


    for question in questions:

        print("\n" + "=" * 60)

        print("QUESTION:")
        print(question)

        print("\nANSWER:")

        answer = route_question(question)

        print(answer)
