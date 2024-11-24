from knowledge_base import rules, Symptom, Disease
from explanation_mechanism import explain_diagnosis
from itertools import combinations

class ChildDiseaseExpert:
    def __init__(self):
        self.possible_diagnoses = []

    def evaluate_two_symptom_matches(self, symptoms):
        """
        Evaluate rules for possible matches with two symptoms at a time.
        """
        for rule in rules:
            # Check all two-symptom combinations
            for combo in combinations(rule['conditions'], 2):
                if all(symptom in symptoms for symptom in combo):
                    # Match found
                    self.possible_diagnoses.append({
                        'disease': rule['disease'],
                        'matched_symptoms': combo,
                        'recommendation': rule['recommendation']
                    })

    def print_possible_diagnoses(self):
        """
        Print the possible diagnoses based on the matches.
        """
        if self.possible_diagnoses:
            print("\nPossible diagnoses based on two symptoms:")
            for diagnosis in self.possible_diagnoses:
                print(f"\nDisease: {diagnosis['disease']}")
                print(f"Matched Symptoms: {', '.join(diagnosis['matched_symptoms'])}")
                print(f"Recommendation: {diagnosis['recommendation']}")
        else:
            print("\nNo possible diagnoses based on the provided symptoms.")
