from experta import *
from knowledge_base import Symptom, Disease  # Importing Fact classes
from explanation_mechanism import explain_diagnosis  # For explanation mechanism

class ChildDiseaseExpert(KnowledgeEngine):
    @Rule(Symptom(name='fever') & Symptom(name='rash') & Symptom(name='swollen_lymph_nodes'), salience=10)
    def rubella(self):
        matched_symptoms = ['fever', 'rash', 'swollen lymph nodes']
        explain_diagnosis('Rubella', matched_symptoms)
        self.declare(Disease(name='Rubella'))
        print("Recommendations: Rest, stay hydrated, and see a doctor if symptoms persist.")

    @Rule(Symptom(name='fever') & Symptom(name='rash') & Symptom(name='conjunctivitis'), salience=9)
    def measles(self):
        matched_symptoms = ['fever', 'rash', 'conjunctivitis']
        explain_diagnosis('Measles', matched_symptoms)
        self.declare(Disease(name='Measles'))
        print("Recommendations: Isolate the patient and seek medical attention.")

    @Rule(Symptom(name='cough') & Symptom(name='difficulty_breathing'), salience=8)
    def bronchitis(self):
        matched_symptoms = ['cough', 'difficulty breathing']
        explain_diagnosis('Bronchitis', matched_symptoms)
        self.declare(Disease(name='Bronchitis'))
        print("Recommendations: Ensure warm fluids, rest, and consult a doctor if breathing worsens.")

    @Rule(Symptom(name='fever') & Symptom(name='sore_throat') & Symptom(name='red_tonsils'), salience=7)
    def tonsillitis(self):
        matched_symptoms = ['fever', 'sore throat', 'red tonsils']
        explain_diagnosis('Tonsillitis', matched_symptoms)
        self.declare(Disease(name='Tonsillitis'))
        print("Recommendations: Gargle warm salt water and consult a doctor for antibiotics.")

    @Rule(Disease(name='Rubella'), salience=6)
    def rubella_followup(self):
        print("Evaluating rule: Rubella Follow-Up")
        print("Rubella Follow-Up: Ensure MMR vaccination if not already vaccinated.")
        print("Alert: Inform the local health authority if confirmed.")

    @Rule(Disease(name='Rubella') & Symptom(name='pregnant'), salience=5)
    def rubella_pregnancy_risk(self):
        print("Evaluating rule: Rubella Pregnancy Risk")
        print("Alert: Rubella during pregnancy poses high risks to the unborn child. Immediate medical attention required.")

    @Rule(NOT(Symptom(name=W())), salience=-1)
    def no_diagnosis(self):
        print("Default rule triggered: No diagnosis.")
        print("Recommendations: Please consult a healthcare professional for further evaluation.")
