def explain_diagnosis(disease_name, symptoms_matched):
    """
    Explains the diagnosis based on matched symptoms.
    :param disease_name: Name of the diagnosed disease
    :param symptoms_matched: List of symptoms that matched the rule
    """
    explanation = f"The system diagnosed {disease_name} based on the following symptoms: {', '.join(symptoms_matched)}."
    print(explanation)
    return explanation
