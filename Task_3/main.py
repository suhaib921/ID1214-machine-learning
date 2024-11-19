from inference_engine import ChildDiseaseExpert
from knowledge_base import Symptom

def main():
    print("Welcome to the Children's Disease Expert System.")
    print("Please answer the following questions with 'yes' or 'no'.")
    
    # Instantiate the expert system
    engine = ChildDiseaseExpert()
    engine.reset()

    # Symptom questions with input validation
    symptoms = {}
    questions = {
        'fever': "Does the child have a fever? ",
        'rash': "Does the child have a rash? ",
        'swollen_lymph_nodes': "Does the child have swollen lymph nodes? ",
        'conjunctivitis': "Does the child have conjunctivitis (red eyes)? ",
        'cough': "Does the child have a cough? ",
        'difficulty_breathing': "Does the child have difficulty breathing? ",
        'sore_throat': "Does the child have a sore throat? ",
        'red_tonsils': "Does the child have red or inflamed tonsils? ",
        'pregnant': "Is the patient pregnant (if applicable)? ",
    }

    for symptom, question in questions.items():
        while True:
            response = input(question).strip().lower()
            if response in ['yes', 'no']:
                symptoms[symptom] = response == 'yes'
                break
            print("Please answer with 'yes' or 'no'.")

    # Declare symptoms in the engine
    for symptom, present in symptoms.items():
        if present:
            engine.declare(Symptom(name=symptom))
    
    # Run the engine
    engine.run()

if __name__ == "__main__":
    main()
