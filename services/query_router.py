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
    extract_age_group,
    extract_attack_animal,
    extract_state
)

from services.insurance_policy import get_policy_info

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
    # Fill in wound/attack fields expected by the model
    # (defaults if not mentioned in the text)
    # ----------------------------------------------

    attack_animal = extract_attack_animal(question)

    symptoms["attack_animal"] = attack_animal
    if symptoms.get("animal_attack") != "yes" and attack_animal != "none":
        symptoms["animal_attack"] = "yes"

    symptoms.setdefault("wound_location", "none")
    symptoms.setdefault("body_recovered", "yes")
    symptoms.setdefault("witness_present", "no")


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


    # ----------------------------------------------
    # If the predicted cause is an animal attack (or animal attack symptoms present),
    # look up the state's compensation policy
    # ----------------------------------------------

    ANIMAL_ATTACK_CAUSES = {
        "animal_attack", "animal attack",
        "snake_bite", "snake bite",
        "lion_attack", "leopard_attack", "tiger_attack",
        "elephant_attack", "dog_bite", "other_animal_attack",
    }

    pred_norm = str(prediction).lower().replace(" ", "_").strip()

    is_animal_attack = (
        pred_norm in ANIMAL_ATTACK_CAUSES
        or str(prediction).lower() in ANIMAL_ATTACK_CAUSES
        or symptoms.get("animal_attack") == "yes"
        or attack_animal != "none"
        or symptoms.get("puncture_wound") == "yes"
        or symptoms.get("bite_mark") == "yes"
        or symptoms.get("claw_mark") == "yes"
    )

    if is_animal_attack:

        state = extract_state(question)

        # Infer specific animal from prediction if not already extracted
        effective_animal = attack_animal
        if effective_animal in ["none", "other", None]:
            if "snake" in pred_norm:
                effective_animal = "snake"
            elif "tiger" in pred_norm:
                effective_animal = "tiger"
            elif "lion" in pred_norm:
                effective_animal = "lion"
            elif "leopard" in pred_norm:
                effective_animal = "leopard"
            elif "elephant" in pred_norm:
                effective_animal = "elephant"
            elif "dog" in pred_norm:
                effective_animal = "dog"
            else:
                effective_animal = "other"

        if state is None:
            response += (
                "\n\nThis looks like it may be an animal-attack case. "
                "Please mention the state so I can check the applicable "
                "wildlife-attack compensation policy."
            )
        else:
            policy = get_policy_info(state, effective_animal)

            response += f"\n\nWildlife-attack compensation ({policy['state'] if policy.get('state') else state}):\n"

            if policy["found"]:
                response += (
                    f"- Scheme: {policy['scheme_name']}\n"
                    f"- Department: {policy['department']}\n"
                    f"- Compensation ({effective_animal}): {policy['compensation']}\n"
                    f"- Notes: {policy['notes']}\n"
                )
                if policy["source_url"]:
                    response += f"- Source: {policy['source_url']}\n"
            else:
                response += f"- {policy['notes']}\n"

            response += (
                "\nThis is reference information only, not a confirmation "
                "of eligibility. The claim must still be verified by the "
                "forest department / relevant authority."
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
        "Ask about the dataset or describe "
        "the patient's symptoms."
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