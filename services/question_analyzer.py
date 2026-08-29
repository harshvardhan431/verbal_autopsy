
import re


# ==================================================
# DATASET FEATURES
# ==================================================

SYMPTOM_COLUMNS = [
    "fever",
    "cough",
    "difficulty_breathing",
    "fast_breathing",
    "chest_pain",
    "diarrhea",
    "blood_in_stool",
    "vomiting",
    "blood_in_vomit",
    "abdominal_pain",
    "protruding_abdomen",
    "severe_headache",
    "stiff_neck",
    "convulsions",
    "unconscious",
    "paralysis",
    "skin_rash",
    "yellow_eyes_jaundice",
    "swollen_legs_feet",
    "weight_loss",
    "night_sweats",
    "road_traffic_accident",
    "fall_injury",
    "poisoning",
    "died_suddenly",
    "pregnant_at_death",
    "excessive_bleeding_delivery",
]


# ==================================================
# WORD → COLUMN MAPPING
# ==================================================

COLUMN_ALIASES = {
    "fever": ["fever", "temperature"],
    "cough": ["cough", "coughing"],
    "difficulty_breathing": [
        "difficulty breathing",
        "breathing difficulty",
        "shortness of breath",
        "breathlessness",
    ],
    "fast_breathing": [
        "fast breathing",
        "rapid breathing",
    ],
    "chest_pain": ["chest pain"],
    "diarrhea": ["diarrhea", "diarrhoea"],
    "blood_in_stool": [
        "blood in stool",
        "bloody stool",
    ],
    "vomiting": ["vomiting", "vomit"],
    "blood_in_vomit": [
        "blood in vomit",
        "vomiting blood",
    ],
    "abdominal_pain": [
        "abdominal pain",
        "stomach pain",
        "belly pain",
    ],
    "protruding_abdomen": [
        "protruding abdomen",
        "swollen abdomen",
        "distended abdomen",
    ],
    "severe_headache": [
        "severe headache",
        "bad headache",
    ],
    "stiff_neck": ["stiff neck"],
    "convulsions": [
        "convulsions",
        "seizure",
        "seizures",
    ],
    "unconscious": [
        "unconscious",
        "lost consciousness",
    ],
    "paralysis": ["paralysis", "paralyzed", "paralysed"],
    "skin_rash": ["skin rash", "rash"],
    "yellow_eyes_jaundice": [
        "yellow eyes",
        "jaundice",
    ],
    "swollen_legs_feet": [
        "swollen legs",
        "swollen feet",
        "swollen legs and feet",
    ],
    "weight_loss": ["weight loss"],
    "night_sweats": ["night sweats"],
    "road_traffic_accident": [
        "road traffic accident",
        "traffic accident",
        "car accident",
        "road accident",
    ],
    "fall_injury": [
        "fall",
        "fall injury",
    ],
    "poisoning": ["poisoning", "poison"],
    "died_suddenly": [
        "died suddenly",
        "sudden death",
    ],
    "pregnant_at_death": [
        "pregnant",
        "pregnancy",
    ],
    "excessive_bleeding_delivery": [
        "excessive bleeding",
        "bleeding during delivery",
        "postpartum bleeding",
    ],
}


# ==================================================
# INTENT DETECTION
# ==================================================

def detect_intent(question):

    q = question.lower().strip()

    # Prediction questions
    prediction_words = [
        "predict",
        "prediction",
        "likely cause",
        "possible cause",
        "cause of death",
        "what caused",
        "what could be",
    ]

    if any(word in q for word in prediction_words):
        return "PREDICTION"

    # Count questions
    count_words = [
        "how many",
        "number of",
        "count",
        "how much",
    ]

    if any(word in q for word in count_words):
        return "COUNT"

    # Percentage questions
    percentage_words = [
        "percentage",
        "percent",
        "%",
        "proportion",
    ]

    if any(word in q for word in percentage_words):
        return "PERCENTAGE"

    # Most common questions
    common_words = [
        "most common",
        "most frequent",
        "highest",
        "commonest",
    ]

    if any(word in q for word in common_words):
        return "MOST_COMMON"

    # Distribution questions
    distribution_words = [
        "distribution",
        "breakdown",
        "frequency",
        "frequencies",
    ]

    if any(word in q for word in distribution_words):
        return "DISTRIBUTION"

    return "UNKNOWN"


# ==================================================
# EXTRACT COLUMN / SYMPTOM
# ==================================================

def extract_columns(question):

    q = question.lower()

    found_columns = []

    for column, aliases in COLUMN_ALIASES.items():

        for alias in aliases:

            if alias in q:
                found_columns.append(column)
                break

    return list(dict.fromkeys(found_columns))


# ==================================================
# EXTRACT YES / NO VALUES
# ==================================================

def extract_value(question):

    q = question.lower()

    negative_words = [
        "without",
        "didn't have",
        "did not have",
        "no ",
        "not have",
        "absent",
    ]

    if any(word in q for word in negative_words):
        return "no"

    return "yes"


# ==================================================
# ANALYZE QUESTION
# ==================================================

def analyze_question(question):

    intent = detect_intent(question)

    columns = extract_columns(question)

    value = extract_value(question)

    return {
        "question": question,
        "intent": intent,
        "columns": columns,
        "value": value,
    }


# ==================================================
# TEST
# ==================================================

if __name__ == "__main__":

    questions = [
        "How many people had fever?",
        "What percentage of people had cough?",
        "What is the most common cause of death?",
        "Show the frequency of vomiting.",
        "The patient had fever and cough. What is the likely cause?",
        "How many people did not have fever?",
    ]

    for question in questions:

        result = analyze_question(question)

        print("\nQuestion:")
        print(question)

        print("Analysis:")
        print(result)

