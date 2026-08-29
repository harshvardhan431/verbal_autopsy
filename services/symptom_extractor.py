
# ==================================================
# SYMPTOM EXTRACTOR
# Converts natural language into structured symptoms
# ==================================================


SYMPTOM_ALIASES = {

    "fever": [
        "fever",
        "high temperature",
        "temperature"
    ],

    "cough": [
        "cough",
        "coughing"
    ],

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
        "bloody stool",
        "blood in feces"
    ],

    "vomiting": [
        "vomiting",
        "vomit",
        "throwing up"
    ],

    "blood_in_vomit": [
        "blood in vomit",
        "vomiting blood",
        "vomited blood"
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
        "bad headache",
        "extreme headache"
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
        "lost consciousness",
        "loss of consciousness"
    ],

    "paralysis": [
        "paralysis",
        "paralyzed",
        "paralysed"
    ],

    "skin_rash": [
        "skin rash",
        "rash",
        "rashes"
    ],

    "yellow_eyes_jaundice": [
        "yellow eyes",
        "yellow skin",
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
        "car accident",
        "vehicle accident"
    ],

    "fall_injury": [
        "fall injury",
        "injury from fall",
        "fell down",
        "fall"
    ],

    "poisoning": [
        "poisoning",
        "poison",
        "poisoned"
    ],

    "died_suddenly": [
        "died suddenly",
        "sudden death",
        "death was sudden"
    ],

    "pregnant_at_death": [
        "pregnant",
        "pregnancy",
        "was pregnant"
    ],

    "excessive_bleeding_delivery": [
        "excessive bleeding",
        "heavy bleeding during delivery",
        "bleeding during delivery",
        "postpartum bleeding"
    ]
}


# ==================================================
# NEGATION DETECTION
# ==================================================

NEGATION_WORDS = [
    "no",
    "not",
    "without",
    "never",
    "didn't have",
    "did not have"
]


def is_negated(text, position):

    """
    Check whether a symptom mention is preceded
    by a simple negation phrase.
    """

    start = max(0, position - 40)

    previous_text = text[start:position]

    for word in NEGATION_WORDS:

        if word in previous_text:
            return True

    return False


# ==================================================
# EXTRACT SYMPTOMS
# ==================================================

def extract_symptoms(text):

    text = text.lower()

    symptoms = {}

    for symptom, aliases in SYMPTOM_ALIASES.items():

        symptoms[symptom] = "no"

        for alias in aliases:

            position = text.find(alias)

            if position != -1:

                if is_negated(text, position):

                    symptoms[symptom] = "no"

                else:

                    symptoms[symptom] = "yes"

                break

    return symptoms


# ==================================================
# TEST
# ==================================================

if __name__ == "__main__":

    test_cases = [

        "The patient had fever, cough and difficulty breathing.",

        "The patient had severe headache and convulsions.",

        "The patient had fever but no cough.",

        "The patient had vomiting and abdominal pain.",

        "The patient had no fever but had chest pain."
    ]


    for text in test_cases:

        print("\n" + "=" * 60)

        print("INPUT:")
        print(text)

        print("\nEXTRACTED SYMPTOMS:")

        symptoms = extract_symptoms(text)

        for symptom, value in symptoms.items():

            if value == "yes":

               print(f"{symptom}: {value}")

