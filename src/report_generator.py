from variant_interpreter import interpret_variant


def generate_report(patient_name, mutation):
    result = interpret_variant(mutation)

    report = f"""
GeneDose AI Clinical Report

Patient: {patient_name}

Mutation:
{mutation}

Risk:
{result['risk']}

Recommended Therapy:
{', '.join(result['therapy'])}

Interpretation:
{result['description']}

This report is intended to support, not replace, clinical judgment.
"""

    return report


print(generate_report("Patient 001", "FLT3-ITD"))
