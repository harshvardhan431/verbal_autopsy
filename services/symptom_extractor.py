import re
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
    ],

    "animal_attack": [
        "animal attack",
        "attacked by an animal",
        "attacked by animal",
        "mauled",
        "wild animal attack",
        "wild animal",
        "wildanimal",
        "animal bite",
        "tiger attack",
        "lion attack",
        "leopard attack",
        "elephant attack"
    ],

    "bite_mark": [
        "bite mark",
        "bite marks",
        "bitten",
        "teeth marks"
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
        "snake bite",
        "snakebite"
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

        if re.search(r"\b" + re.escape(word) + r"\b", previous_text):
            return True

    return False



# ==================================================
# AGE GROUP EXTRACTION
# ==================================================



def extract_age_group(text):

    text = text.lower()

    # ----------------------------------------------
    # Explicit age
    # ----------------------------------------------

    patterns = [
        r"(\d+)\s*(?:years?|yrs?)\s*old",
        r"age\s*(?:was|is)?\s*(\d+)",
        r"(\d+)\s*year"
    ]

    for pattern in patterns:

        match = re.search(pattern, text)

        if match:

            age = int(match.group(1))

            if age < 1:
                return "neonate"

            elif age < 18:
                return "child"

            else:
                return "adult"


    # ----------------------------------------------
    # Age-group words
    # ----------------------------------------------

    if "neonate" in text or "newborn" in text:
        return "neonate"

    if "child" in text or "kid" in text:
        return "child"

    if "adult" in text:
        return "adult"

    # ----------------------------------------------
    # Age not provided
    # ----------------------------------------------

    return None


# ==================================================
# ATTACK ANIMAL EXTRACTION
# ==================================================

ANIMAL_KEYWORDS = {
    "lion": ["lion", "lions", "asiatic lion"],
    "leopard": ["leopard", "leopards", "panther"],
    "tiger": ["tiger", "tigers", "bengal tiger"],
    "elephant": ["elephant", "elephants", "wild elephant"],
    "snake": ["snake", "snakes", "cobra", "viper", "krait", "snake bite", "snakebite"],
    "dog": ["dog", "dogs", "stray dog", "rabid dog"],
    "bear": ["bear", "sloth bear"],
    "crocodile": ["crocodile", "alligator", "mugger"],
    "boar": ["wild boar", "boar"],
    "wolf": ["wolf", "wolves"],
}


def extract_attack_animal(text):

    text = text.lower()

    for animal, keywords in ANIMAL_KEYWORDS.items():
        for keyword in keywords:
            if re.search(r"\b" + re.escape(keyword) + r"\b", text):
                return animal

    if any(k in text for k in ["animal", "mauled", "wild animal", "wildanimal", "wild beast", "carnivore"]):
        return "other"

    return "none"


# ==================================================
# STATE EXTRACTION
# ==================================================

STATE_ALIASES = {
    "Maharashtra": ["maharashtra", "mh"],
    "Madhya Pradesh": ["madhya pradesh", "mp"],
    "Karnataka": ["karnataka", "ka"],
    "West Bengal": ["west bengal", "wb", "bengal"],
    "Assam": ["assam", "as"],
    "Uttarakhand": ["uttarakhand", "uk", "uttaranchal"],
    "Rajasthan": ["rajasthan", "rj"],
    "Gujarat": ["gujarat", "gj"],
    "Kerala": ["kerala", "kl"],
    "Tamil Nadu": ["tamil nadu", "tamilnadu", "tn"],
    "Uttar Pradesh": ["uttar pradesh", "up"],
    "Bihar": ["bihar", "br"],
    "Odisha": ["odisha", "orissa", "od"],
    "Chhattisgarh": ["chhattisgarh", "cg"],
    "Jharkhand": ["jharkhand", "jh"],
    "Andhra Pradesh": ["andhra pradesh", "andhra", "ap"],
    "Telangana": ["telangana", "ts", "tg"],
    "Himachal Pradesh": ["himachal pradesh", "himachal", "hp"],
    "Goa": ["goa", "ga"],
    "Punjab": ["punjab", "pb"],
    "Haryana": ["haryana", "hr"],
    "Jammu And Kashmir": ["jammu and kashmir", "jammu & kashmir", "j&k", "jk", "kashmir"],
    "Delhi": ["delhi", "new delhi", "nct of delhi", "dl"],
    "Ladakh": ["ladakh"],
    "Puducherry": ["puducherry", "pondicherry", "py"],
    "Arunachal Pradesh": ["arunachal pradesh", "arunachal", "ar"],
    "Manipur": ["manipur", "mn"],
    "Meghalaya": ["meghalaya", "ml"],
    "Mizoram": ["mizoram", "mz"],
    "Nagaland": ["nagaland", "nl"],
    "Sikkim": ["sikkim", "sk"],
    "Tripura": ["tripura", "tr"],
}


def extract_state(text):

    text_lower = text.lower()

    for canonical_state, aliases in STATE_ALIASES.items():
        for alias in aliases:
            # Match whole words only to avoid substring matches like 'goa' in 'goat'
            if re.search(r"\b" + re.escape(alias) + r"\b", text_lower):
                return canonical_state

    return None


# ==================================================
# EXTRACT SYMPTOMS
# ==================================================

def extract_symptoms(text):

    text_lower = text.lower()

    symptoms = {}

    for symptom, aliases in SYMPTOM_ALIASES.items():

        symptoms[symptom] = "no"

        for alias in aliases:

            # Use word boundary search to avoid partial substring matching (e.g. 'rash' in 'maharashtra')
            match = re.search(r"\b" + re.escape(alias) + r"\b", text_lower)

            if match:

                position = match.start()

                if is_negated(text_lower, position):

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

        "The patient had no fever but had chest pain.",

        "The patient had claw marks and bite marks, mauled by a lion."
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

        animal = extract_attack_animal(text)

        if animal != "none":
            print(f"attack_animal: {animal}")