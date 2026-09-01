
import re


# ==================================================
# SYMPTOM ALIASES
# ==================================================

COLUMN_ALIASES = {
    "fever": ["fever", "high temperature", "temperature"],

    "cough": ["cough", "coughing"],

    "difficulty_breathing": [
        "difficulty breathing",
        "breathing difficulty",
        "shortness of breath",
        "breathlessness"
    ],

    "fast_breathing": [
        "fast breathing",
        "rapid breathing"
    ],

    "chest_pain": [
        "chest pain",
        "pain in chest"
    ],

    "diarrhea": [
        "diarrhea",
        "diarrhoea",
        "loose motion",
        "loose motions"
    ],

    "blood_in_stool": [
        "blood in stool",
        "bloody stool"
    ],

    "vomiting": [
        "vomiting",
        "vomit",
        "throwing up"
    ],

    "blood_in_vomit": [
        "blood in vomit",
        "vomiting blood"
    ],

    "abdominal_pain": [
        "abdominal pain",
        "stomach pain",
        "belly pain"
    ],

    "protruding_abdomen": [
        "protruding abdomen",
        "swollen abdomen",
        "distended abdomen"
    ],

    "severe_headache": [
        "severe headache",
        "bad headache"
    ],

    "stiff_neck": [
        "stiff neck",
        "neck stiffness"
    ],

    "convulsions": [
        "convulsions",
        "seizure",
        "seizures"
    ],

    "unconscious": [
        "unconscious",
        "lost consciousness"
    ],

    "paralysis": [
        "paralysis",
        "paralyzed",
        "paralysed"
    ],

    "skin_rash": [
        "skin rash",
        "rash"
    ],

    "yellow_eyes_jaundice": [
        "yellow eyes",
        "jaundice"
    ],

    "swollen_legs_feet": [
        "swollen legs",
        "swollen feet",
        "swollen legs and feet"
    ],

    "weight_loss": [
        "weight loss",
        "lost weight"
    ],

    "night_sweats": [
        "night sweats",
        "sweating at night"
    ],

    "road_traffic_accident": [
        "road traffic accident",
        "traffic accident",
        "road accident",
        "car accident"
    ],

    "fall_injury": [
        "fall injury",
        "injury from fall",
        "fell down"
    ],

    "poisoning": [
        "poisoning",
        "poison",
        "poisoned"
    ],

    "died_suddenly": [
        "died suddenly",
        "sudden death"
    ],

    "pregnant_at_death": [
        "pregnant",
        "pregnancy"
    ],

    "excessive_bleeding_delivery": [
        "excessive bleeding",
        "bleeding during delivery",
        "postpartum bleeding"
    ],

    "animal_attack": [
        "animal attack",
        "attacked by an animal",
        "attacked by animal",
        "wild animal attack",
        "wild animal",
        "wildanimal",
        "mauled",
        "animal bite",
        "animal"
    ],

    "bite_mark": [
        "bite mark",
        "bite marks",
        "bitten",
        "teeth marks",
        "dog bite",
        "snake bite"
    ],

    "claw_mark": [
        "claw mark",
        "claw marks",
        "scratch marks",
        "clawed"
    ],

    "puncture_wound": [
        "puncture wound",
        "puncture wounds",
        "fang marks",
        "snake bite"
    ],

    "attack_animal": [
        "tiger",
        "lion",
        "leopard",
        "elephant",
        "snake",
        "cobra",
        "viper",
        "krait",
        "dog",
        "bear",
        "crocodile",
        "wolf",
        "boar"
    ],
}


# ==================================================
# INTENT DETECTION
# ==================================================

def detect_intent(question):

    q = question.lower().strip()


    # ----------------------------------------------
    # Dataset questions FIRST
    # ----------------------------------------------

    if any(word in q for word in [
        "how many",
        "number of",
        "count"
    ]):
        return "COUNT"


    if any(word in q for word in [
        "percentage",
        "percent",
        "%",
        "proportion"
    ]):
        return "PERCENTAGE"


    if any(word in q for word in [
        "most common",
        "most frequent",
        "commonest"
    ]):
        return "MOST_COMMON"


    if any(word in q for word in [
        "distribution",
        "breakdown",
        "frequency",
        "frequencies"
    ]):
        return "DISTRIBUTION"


    # ----------------------------------------------
    # Explicit prediction questions
    # ----------------------------------------------

    if any(word in q for word in [
        "predict",
        "prediction",
        "likely cause",
        "possible cause",
        "what caused",
        "what could be the cause",
        "what is the cause"
    ]):
        return "PREDICTION"


    # ----------------------------------------------
    # Any recognised symptom → treat as prediction
    # ----------------------------------------------

    for aliases in COLUMN_ALIASES.values():

        for alias in aliases:

            if alias in q:
                return "PREDICTION"


    return "UNKNOWN"


# ==================================================
# EXTRACT COLUMNS
# ==================================================

def extract_columns(question):

    q = question.lower()

    found_columns = []

    for column, aliases in COLUMN_ALIASES.items():

        for alias in aliases:

            # Word/phrase matching
            if re.search(
                r"\b" + re.escape(alias) + r"\b",
                q
            ):
                found_columns.append(column)
                break

    return list(dict.fromkeys(found_columns))


# ==================================================
# EXTRACT YES / NO
# ==================================================

def extract_value(question):

    q = question.lower()

    negative_patterns = [
        "without",
        "didn't have",
        "did not have",
        "no ",
        "not have",
        "absent"
    ]

    if any(pattern in q for pattern in negative_patterns):
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
        "value": value
    }


# ==================================================
# TEST
# ==================================================

if __name__ == "__main__":

    questions = [

        "How many people had fever?",

        "What percentage of people had cough?",

        "What is the most common cause of death?",

        "What is the distribution of causes of death?",

        "The patient had fever, cough and difficulty breathing.",

        "The patient had severe headache and convulsions.",

        "The patient had fever but no cough.",

        "A patient has chest pain.",

        "What is the likely cause of fever and cough?"
    ]


    for question in questions:

        print("\n" + "=" * 60)

        print("QUESTION:")
        print(question)

        print("\nANALYSIS:")

        print(analyze_question(question))

