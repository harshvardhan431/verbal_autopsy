"""
State-wise wildlife-attack insurance/compensation policy lookup
==================================================================

WHAT THIS IS
------------
Many Indian states run ex-gratia compensation schemes for deaths caused
by wildlife attacks (lion, tiger, leopard, elephant, snake, etc.), but
the scheme name, compensation amount, eligible animals, and the
department responsible for verification differ from state to state -
and change over time.

THIS FILE CURRENTLY CONTAINS DUMMY / RANDOM VALUES ONLY.
------------------------------------------------------
The scheme names and compensation figures below are made up, purely so
you have something non-empty to look at while wiring up the rest of the
app. THEY ARE NOT REAL AND MUST NOT BE SHOWN TO AN ACTUAL CLAIMANT OR
USED TO MAKE A REAL DECISION.

Before this goes anywhere near a real user, replace every value below
with figures sourced from the relevant state forest department /
revenue department notifications.
"""


STATE_POLICIES = {

    # ==================================================
    # ⚠️  DUMMY / EXAMPLE DATA ONLY — NOT REAL FIGURES  ⚠️
    # ==================================================

    "Maharashtra": {
        "scheme_name": "Maharashtra Wildlife Attack Relief Scheme (example)",
        "department": "Maharashtra Forest Department",
        "animals_covered": ["tiger", "leopard", "lion", "elephant", "snake", "dog", "bear", "crocodile", "boar", "other"],
        "compensation": {
            "tiger": "INR 20,00,000 (example figure)",
            "leopard": "INR 15,00,000 (example figure)",
            "lion": "INR 15,00,000 (example figure)",
            "elephant": "INR 10,00,000 (example figure)",
            "snake": "INR 4,00,000 (example figure)",
            "dog": "INR 1,00,000 (example figure)",
            "bear": "INR 5,00,000 (example figure)",
            "crocodile": "INR 5,00,000 (example figure)",
            "boar": "INR 5,00,000 (example figure)",
            "other": "INR 5,00,000 (example figure)",
        },
        "notes": "Example only: claim must include post-mortem report and forest range officer verification.",
        "source_url": "https://example.gov.in/maharashtra-wildlife-scheme",
    },

    "Madhya Pradesh": {
        "scheme_name": "MP Man-Animal Conflict Compensation Scheme (example)",
        "department": "Madhya Pradesh Forest Department",
        "animals_covered": ["tiger", "leopard", "lion", "elephant", "snake", "dog", "bear", "crocodile", "boar", "other"],
        "compensation": {
            "tiger": "INR 8,00,000 (example figure)",
            "leopard": "INR 8,00,000 (example figure)",
            "lion": "INR 8,00,000 (example figure)",
            "elephant": "INR 8,00,000 (example figure)",
            "snake": "INR 4,00,000 (example figure)",
            "dog": "INR 50,000 (example figure)",
            "bear": "INR 4,00,000 (example figure)",
            "crocodile": "INR 4,00,000 (example figure)",
            "boar": "INR 4,00,000 (example figure)",
            "other": "INR 4,00,000 (example figure)",
        },
        "notes": "Example only: claim filed through local Tehsildar with police FIR copy.",
        "source_url": "https://example.gov.in/mp-wildlife-scheme",
    },

    "Karnataka": {
        "scheme_name": "Karnataka Wildlife Conflict Ex-Gratia Scheme (example)",
        "department": "Karnataka Forest Department",
        "animals_covered": ["tiger", "leopard", "lion", "elephant", "snake", "dog", "bear", "crocodile", "boar", "other"],
        "compensation": {
            "tiger": "INR 15,00,000 (example figure)",
            "leopard": "INR 10,00,000 (example figure)",
            "lion": "INR 10,00,000 (example figure)",
            "elephant": "INR 7,50,000 (example figure)",
            "snake": "INR 5,00,000 (example figure)",
            "dog": "INR 50,000 (example figure)",
            "bear": "INR 5,00,000 (example figure)",
            "crocodile": "INR 5,00,000 (example figure)",
            "boar": "INR 5,00,000 (example figure)",
            "other": "INR 5,00,000 (example figure)",
        },
        "notes": "Example only: 30-day filing window from date of incident.",
        "source_url": "https://example.gov.in/karnataka-wildlife-scheme",
    },

    "West Bengal": {
        "scheme_name": "WB Wildlife Attack Relief Fund (example)",
        "department": "West Bengal Forest Department",
        "animals_covered": ["tiger", "leopard", "lion", "elephant", "snake", "dog", "bear", "crocodile", "boar", "other"],
        "compensation": {
            "tiger": "INR 5,00,000 (example figure)",
            "leopard": "INR 4,00,000 (example figure)",
            "lion": "INR 4,00,000 (example figure)",
            "elephant": "INR 5,00,000 (example figure)",
            "snake": "INR 2,00,000 (example figure)",
            "dog": "INR 25,000 (example figure)",
            "bear": "INR 2,00,000 (example figure)",
            "crocodile": "INR 3,00,000 (example figure)",
            "boar": "INR 2,00,000 (example figure)",
            "other": "INR 2,00,000 (example figure)",
        },
        "notes": "Example only: applicable within Sundarbans buffer zone villages.",
        "source_url": "https://example.gov.in/wb-wildlife-scheme",
    },

    "Assam": {
        "scheme_name": "Assam Human-Wildlife Conflict Relief Scheme (example)",
        "department": "Assam Forest Department",
        "animals_covered": ["tiger", "elephant", "rhino", "leopard", "lion", "snake", "dog", "bear", "other"],
        "compensation": {
            "tiger": "INR 6,00,000 (example figure)",
            "elephant": "INR 6,00,000 (example figure)",
            "rhino": "INR 6,00,000 (example figure)",
            "leopard": "INR 5,00,000 (example figure)",
            "lion": "INR 5,00,000 (example figure)",
            "snake": "INR 3,00,000 (example figure)",
            "dog": "INR 25,000 (example figure)",
            "bear": "INR 3,00,000 (example figure)",
            "other": "INR 3,00,000 (example figure)",
        },
        "notes": "Example only: priority processing for cases involving elephants and rhinos.",
        "source_url": "https://example.gov.in/assam-wildlife-scheme",
    },

    "Uttarakhand": {
        "scheme_name": "Uttarakhand Wildlife Attack Compensation Scheme (example)",
        "department": "Uttarakhand Forest Department",
        "animals_covered": ["tiger", "leopard", "lion", "elephant", "snake", "dog", "bear", "boar", "other"],
        "compensation": {
            "tiger": "INR 6,00,000 (example figure)",
            "leopard": "INR 6,00,000 (example figure)",
            "lion": "INR 6,00,000 (example figure)",
            "elephant": "INR 6,00,000 (example figure)",
            "snake": "INR 3,00,000 (example figure)",
            "dog": "INR 25,000 (example figure)",
            "bear": "INR 4,00,000 (example figure)",
            "boar": "INR 3,00,000 (example figure)",
            "other": "INR 3,00,000 (example figure)",
        },
        "notes": "Example only: leopard attacks are the most frequently filed category here.",
        "source_url": "https://example.gov.in/uttarakhand-wildlife-scheme",
    },

    "Rajasthan": {
        "scheme_name": "Rajasthan Wildlife Conflict Relief Scheme (example)",
        "department": "Rajasthan Forest Department",
        "animals_covered": ["tiger", "leopard", "lion", "snake", "dog", "bear", "crocodile", "other"],
        "compensation": {
            "tiger": "INR 5,00,000 (example figure)",
            "leopard": "INR 5,00,000 (example figure)",
            "lion": "INR 5,00,000 (example figure)",
            "snake": "INR 3,00,000 (example figure)",
            "dog": "INR 25,000 (example figure)",
            "bear": "INR 3,00,000 (example figure)",
            "crocodile": "INR 4,00,000 (example figure)",
            "other": "INR 3,00,000 (example figure)",
        },
        "notes": "Example only: Ranthambore and Sariska buffer-zone claims processed with priority.",
        "source_url": "https://example.gov.in/rajasthan-wildlife-scheme",
    },

    "Gujarat": {
        "scheme_name": "Gujarat Wildlife Damage Compensation Scheme (example)",
        "department": "Gujarat Forest Department",
        "animals_covered": ["lion", "leopard", "tiger", "snake", "dog", "bear", "crocodile", "other"],
        "compensation": {
            "lion": "INR 5,00,000 (example figure)",
            "leopard": "INR 5,00,000 (example figure)",
            "tiger": "INR 5,00,000 (example figure)",
            "snake": "INR 4,00,000 (example figure)",
            "dog": "INR 50,000 (example figure)",
            "bear": "INR 3,00,000 (example figure)",
            "crocodile": "INR 4,00,000 (example figure)",
            "other": "INR 4,00,000 (example figure)",
        },
        "notes": "Example only: Gir sanctuary & Greater Gir landscape cases processed under state wildlife guidelines.",
        "source_url": "https://example.gov.in/gujarat-wildlife-scheme",
    },

    "Kerala": {
        "scheme_name": "Kerala Forest Ex-Gratia Relief Scheme (example)",
        "department": "Kerala Forest and Wildlife Department",
        "animals_covered": ["elephant", "tiger", "leopard", "lion", "snake", "dog", "bear", "boar", "other"],
        "compensation": {
            "elephant": "INR 10,00,000 (example figure)",
            "tiger": "INR 10,00,000 (example figure)",
            "leopard": "INR 10,00,000 (example figure)",
            "lion": "INR 8,00,000 (example figure)",
            "snake": "INR 2,00,000 (example figure)",
            "dog": "INR 50,000 (example figure)",
            "bear": "INR 5,00,000 (example figure)",
            "boar": "INR 5,00,000 (example figure)",
            "other": "INR 5,00,000 (example figure)",
        },
        "notes": "Example only: emergency relief provided within 24 hours of incident verification.",
        "source_url": "https://example.gov.in/kerala-wildlife-scheme",
    },

    "Tamil Nadu": {
        "scheme_name": "TN Human-Wildlife Conflict Ex-Gratia Fund (example)",
        "department": "Tamil Nadu Forest Department",
        "animals_covered": ["elephant", "tiger", "leopard", "lion", "snake", "dog", "bear", "boar", "other"],
        "compensation": {
            "elephant": "INR 10,00,000 (example figure)",
            "tiger": "INR 10,00,000 (example figure)",
            "leopard": "INR 10,00,000 (example figure)",
            "lion": "INR 8,00,000 (example figure)",
            "snake": "INR 4,00,000 (example figure)",
            "dog": "INR 50,000 (example figure)",
            "bear": "INR 5,00,000 (example figure)",
            "boar": "INR 4,00,000 (example figure)",
            "other": "INR 5,00,000 (example figure)",
        },
        "notes": "Example only: claims handled via District Forest Officer (DFO).",
        "source_url": "https://example.gov.in/tn-wildlife-scheme",
    },

    "Uttar Pradesh": {
        "scheme_name": "UP Man-Animal Conflict Disaster Relief Scheme (example)",
        "department": "Uttar Pradesh Forest and Disaster Management Department",
        "animals_covered": ["tiger", "leopard", "lion", "elephant", "snake", "dog", "wolf", "other"],
        "compensation": {
            "tiger": "INR 5,00,000 (example figure)",
            "leopard": "INR 5,00,000 (example figure)",
            "lion": "INR 5,00,000 (example figure)",
            "elephant": "INR 5,00,000 (example figure)",
            "snake": "INR 4,00,000 (example figure)",
            "dog": "INR 50,000 (example figure)",
            "wolf": "INR 5,00,000 (example figure)",
            "other": "INR 4,00,000 (example figure)",
        },
        "notes": "Example only: wildlife attacks categorized under state disaster relief.",
        "source_url": "https://example.gov.in/up-wildlife-scheme",
    },

    "Odisha": {
        "scheme_name": "Odisha Wildlife Depredation Compassionate Assistance (example)",
        "department": "Odisha Forest, Environment and Climate Change Department",
        "animals_covered": ["elephant", "tiger", "leopard", "lion", "snake", "dog", "bear", "crocodile", "boar", "other"],
        "compensation": {
            "elephant": "INR 6,00,000 (example figure)",
            "tiger": "INR 6,00,000 (example figure)",
            "leopard": "INR 6,00,000 (example figure)",
            "lion": "INR 5,00,000 (example figure)",
            "snake": "INR 4,00,000 (example figure)",
            "dog": "INR 50,000 (example figure)",
            "bear": "INR 4,00,000 (example figure)",
            "crocodile": "INR 4,00,000 (example figure)",
            "boar": "INR 3,00,000 (example figure)",
            "other": "INR 4,00,000 (example figure)",
        },
        "notes": "Example only: high-priority assistance for snake bites and elephant conflict cases.",
        "source_url": "https://example.gov.in/odisha-wildlife-scheme",
    },

    "Chhattisgarh": {
        "scheme_name": "Chhattisgarh Wildlife Conflict Ex-Gratia Scheme (example)",
        "department": "Chhattisgarh Forest Department",
        "animals_covered": ["elephant", "leopard", "tiger", "lion", "snake", "dog", "bear", "other"],
        "compensation": {
            "elephant": "INR 6,00,000 (example figure)",
            "leopard": "INR 6,00,000 (example figure)",
            "tiger": "INR 6,00,000 (example figure)",
            "lion": "INR 5,00,000 (example figure)",
            "snake": "INR 4,00,000 (example figure)",
            "dog": "INR 25,000 (example figure)",
            "bear": "INR 4,00,000 (example figure)",
            "other": "INR 4,00,000 (example figure)",
        },
        "notes": "Example only: claims verified by local Forest Range Officer.",
        "source_url": "https://example.gov.in/cg-wildlife-scheme",
    },

    "Jharkhand": {
        "scheme_name": "Jharkhand Wildlife Damage Compensation Scheme (example)",
        "department": "Jharkhand Department of Forest, Environment and Climate Change",
        "animals_covered": ["elephant", "leopard", "tiger", "lion", "snake", "dog", "bear", "other"],
        "compensation": {
            "elephant": "INR 4,00,000 (example figure)",
            "leopard": "INR 4,00,000 (example figure)",
            "tiger": "INR 4,00,000 (example figure)",
            "lion": "INR 4,00,000 (example figure)",
            "snake": "INR 4,00,000 (example figure)",
            "dog": "INR 25,000 (example figure)",
            "bear": "INR 3,00,000 (example figure)",
            "other": "INR 3,00,000 (example figure)",
        },
        "notes": "Example only: majorly covers wild elephant migratory corridor incidents.",
        "source_url": "https://example.gov.in/jharkhand-wildlife-scheme",
    },

    "Andhra Pradesh": {
        "scheme_name": "AP Wildlife Conflict Relief Scheme (example)",
        "department": "Andhra Pradesh Forest Department",
        "animals_covered": ["tiger", "leopard", "elephant", "lion", "snake", "dog", "bear", "other"],
        "compensation": {
            "tiger": "INR 5,00,000 (example figure)",
            "leopard": "INR 5,00,000 (example figure)",
            "elephant": "INR 5,00,000 (example figure)",
            "lion": "INR 5,00,000 (example figure)",
            "snake": "INR 4,00,000 (example figure)",
            "dog": "INR 50,000 (example figure)",
            "bear": "INR 3,00,000 (example figure)",
            "other": "INR 4,00,000 (example figure)",
        },
        "notes": "Example only: processed through territorial divisional forest offices.",
        "source_url": "https://example.gov.in/ap-wildlife-scheme",
    },

    "Telangana": {
        "scheme_name": "Telangana Human-Wildlife Conflict Ex-Gratia (example)",
        "department": "Telangana Forest Department",
        "animals_covered": ["tiger", "leopard", "lion", "snake", "dog", "bear", "boar", "other"],
        "compensation": {
            "tiger": "INR 5,00,000 (example figure)",
            "leopard": "INR 5,00,000 (example figure)",
            "lion": "INR 5,00,000 (example figure)",
            "snake": "INR 4,00,000 (example figure)",
            "dog": "INR 50,000 (example figure)",
            "bear": "INR 3,00,000 (example figure)",
            "boar": "INR 3,00,000 (example figure)",
            "other": "INR 4,00,000 (example figure)",
        },
        "notes": "Example only: claims submitted with medical/post-mortem report.",
        "source_url": "https://example.gov.in/telangana-wildlife-scheme",
    },

    "Himachal Pradesh": {
        "scheme_name": "HP Wildlife Relief Scheme (example)",
        "department": "Himachal Pradesh Forest Department",
        "animals_covered": ["leopard", "bear", "snow leopard", "snake", "dog", "other"],
        "compensation": {
            "leopard": "INR 4,00,000 (example figure)",
            "bear": "INR 4,00,000 (example figure)",
            "snow leopard": "INR 4,00,000 (example figure)",
            "snake": "INR 2,00,000 (example figure)",
            "dog": "INR 25,000 (example figure)",
            "other": "INR 3,00,000 (example figure)",
        },
        "notes": "Example only: covers high-altitude wildlife conflict zones.",
        "source_url": "https://example.gov.in/hp-wildlife-scheme",
    },

    "Bihar": {
        "scheme_name": "Bihar Wildlife Depredation Relief Scheme (example)",
        "department": "Bihar Environment, Forest & Climate Change Department",
        "animals_covered": ["tiger", "leopard", "elephant", "snake", "dog", "other"],
        "compensation": {
            "tiger": "INR 5,00,000 (example figure)",
            "leopard": "INR 5,00,000 (example figure)",
            "elephant": "INR 5,00,000 (example figure)",
            "snake": "INR 4,00,000 (example figure)",
            "dog": "INR 25,000 (example figure)",
            "other": "INR 3,00,000 (example figure)",
        },
        "notes": "Example only: Valmiki Tiger Reserve and adjoining areas covered.",
        "source_url": "https://example.gov.in/bihar-wildlife-scheme",
    },

    "Goa": {
        "scheme_name": "Goa Wildlife Damage Compensation Scheme (example)",
        "department": "Goa Forest Department",
        "animals_covered": ["leopard", "tiger", "crocodile", "snake", "dog", "other"],
        "compensation": {
            "leopard": "INR 5,00,000 (example figure)",
            "tiger": "INR 5,00,000 (example figure)",
            "crocodile": "INR 4,00,000 (example figure)",
            "snake": "INR 2,00,000 (example figure)",
            "dog": "INR 25,000 (example figure)",
            "other": "INR 3,00,000 (example figure)",
        },
        "notes": "Example only: claims processed under Goa Forest rules.",
        "source_url": "https://example.gov.in/goa-wildlife-scheme",
    },

    "Punjab": {
        "scheme_name": "Punjab Wildlife Attack Ex-Gratia Scheme (example)",
        "department": "Punjab Department of Forests & Wildlife Preservation",
        "animals_covered": ["leopard", "snake", "dog", "boar", "other"],
        "compensation": {
            "leopard": "INR 5,00,000 (example figure)",
            "snake": "INR 2,00,000 (example figure)",
            "dog": "INR 25,000 (example figure)",
            "boar": "INR 2,00,000 (example figure)",
            "other": "INR 2,00,000 (example figure)",
        },
        "notes": "Example only: verified by local wildlife warden.",
        "source_url": "https://example.gov.in/punjab-wildlife-scheme",
    },

    "Haryana": {
        "scheme_name": "Haryana Wildlife Conflict Compensation (example)",
        "department": "Haryana Forest Department",
        "animals_covered": ["leopard", "snake", "dog", "other"],
        "compensation": {
            "leopard": "INR 5,00,000 (example figure)",
            "snake": "INR 2,00,000 (example figure)",
            "dog": "INR 25,000 (example figure)",
            "other": "INR 2,00,000 (example figure)",
        },
        "notes": "Example only: applicable across all districts.",
        "source_url": "https://example.gov.in/haryana-wildlife-scheme",
    },

    "Jammu And Kashmir": {
        "scheme_name": "J&K Wildlife Attack Ex-Gratia Scheme (example)",
        "department": "J&K Department of Wildlife Protection",
        "animals_covered": ["bear", "leopard", "snake", "dog", "other"],
        "compensation": {
            "bear": "INR 4,00,000 (example figure)",
            "leopard": "INR 4,00,000 (example figure)",
            "snake": "INR 2,00,000 (example figure)",
            "dog": "INR 25,000 (example figure)",
            "other": "INR 3,00,000 (example figure)",
        },
        "notes": "Example only: black bear and leopard conflicts covered in valley and Jammu regions.",
        "source_url": "https://example.gov.in/jk-wildlife-scheme",
    },

    "Delhi": {
        "scheme_name": "Delhi Ex-Gratia Scheme for Animal Conflict (example)",
        "department": "Delhi Forest and Wildlife Department / Revenue Department",
        "animals_covered": ["snake", "dog", "leopard", "other"],
        "compensation": {
            "snake": "INR 2,00,000 (example figure)",
            "dog": "INR 50,000 (example figure)",
            "leopard": "INR 4,00,000 (example figure)",
            "other": "INR 2,00,000 (example figure)",
        },
        "notes": "Example only: claim submitted via District Magistrate office.",
        "source_url": "https://example.gov.in/delhi-wildlife-scheme",
    },
}


GENERIC_FALLBACK_NOTE = (
    "No policy details are on file yet for this state/animal combination. "
    "Contact the relevant state forest department or district administration "
    "to confirm the applicable wildlife-attack compensation scheme."
)


def get_policy_info(state, animal):
    """
    Look up the compensation policy for a given state and attack_animal.

    Returns a dict:
        {
            "found": bool,
            "state": str,
            "animal": str,
            "scheme_name": str or None,
            "department": str or None,
            "compensation": str or None,
            "notes": str,
            "source_url": str or None,
        }

    If the state isn't in STATE_POLICIES, "found" is False
    and a generic fallback note is returned.
    """

    if not state:
        return {
            "found": False,
            "state": None,
            "animal": animal,
            "scheme_name": None,
            "department": None,
            "compensation": None,
            "notes": GENERIC_FALLBACK_NOTE,
            "source_url": None,
        }

    # Case-insensitive lookup map for states
    state_lookup = {k.lower(): k for k in STATE_POLICIES}
    state_clean = state.strip().lower()

    canonical_state_name = state_lookup.get(state_clean)

    if not canonical_state_name:
        # Check if state string matches partially
        for s_lower, s_real in state_lookup.items():
            if s_lower in state_clean or state_clean in s_lower:
                canonical_state_name = s_real
                break

    if not canonical_state_name:
        return {
            "found": False,
            "state": state,
            "animal": animal,
            "scheme_name": None,
            "department": None,
            "compensation": None,
            "notes": f"No specific compensation details on file for state '{state}'. Please contact the {state} Forest Department.",
            "source_url": None,
        }

    policy = STATE_POLICIES[canonical_state_name]

    animal_key = (animal or "other").strip().lower()
    if animal_key == "none":
        animal_key = "other"

    compensation_dict = policy.get("compensation", {})

    # Match exact animal or fallback to 'other'
    compensation_amount = compensation_dict.get(animal_key)
    if not compensation_amount:
        compensation_amount = compensation_dict.get("other", "Check with State Forest Department")

    return {
        "found": True,
        "state": canonical_state_name,
        "animal": animal_key,
        "scheme_name": policy.get("scheme_name"),
        "department": policy.get("department"),
        "compensation": compensation_amount,
        "notes": policy.get("notes"),
        "source_url": policy.get("source_url"),
    }


if __name__ == "__main__":
    print(get_policy_info("Maharashtra", "tiger"))
    print(get_policy_info("MP", "snake"))
    print(get_policy_info("Gujarat", "lion"))
    print(get_policy_info("Kerala", "wild animal"))
    print(get_policy_info("Unknown State", "tiger"))