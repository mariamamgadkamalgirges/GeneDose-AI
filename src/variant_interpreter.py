AML_MUTATIONS = {
    "FLT3-ITD": {
        "risk": "High",
        "therapy": ["Midostaurin", "Gilteritinib"],
        "description": "Associated with poor prognosis."
    },
    "NPM1": {
        "risk": "Favorable",
        "therapy": ["Standard Chemotherapy"],
        "description": "Generally associated with better prognosis."
    },
    "IDH1": {
        "risk": "Intermediate",
        "therapy": ["Ivosidenib"],
        "description": "Targetable mutation."
    },
    "IDH2": {
        "risk": "Intermediate",
        "therapy": ["Enasidenib"],
        "description": "Targetable mutation."
    }
}


def interpret_variant(mutation):
    return AML_MUTATIONS.get(
        mutation,
        {
            "risk": "Unknown",
            "therapy": [],
            "description": "No interpretation available."
        },
    )
