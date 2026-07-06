def recommend_drug(mutation):
    recommendations = {
        "FLT3-ITD": "Midostaurin or Gilteritinib",
        "IDH1": "Ivosidenib",
        "IDH2": "Enasidenib",
        "NPM1": "Standard chemotherapy with monitoring",
        "TP53": "Consider clinical trial or advanced therapy options"
    }

    return recommendations.get(mutation, "No specific targeted therapy found. Physician review required.")


if name == "__main__":
    mutation = "FLT3-ITD"
    drug = recommend_drug(mutation)
    print("Detected Mutation:", mutation)
    print("Recommended Therapy:", drug)
