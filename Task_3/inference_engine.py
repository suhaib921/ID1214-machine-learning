from experta import *
from knowledge_base import Symptom, Disease  # Importing Fact classes
from explanation_mechanism import explain_diagnosis  # For explanation mechanism

class ChildDiseaseExpert(KnowledgeEngine):
    @Rule(Symptom(name='fever') & Symptom(name='rash') & Symptom(name='swollen_lymph_nodes'))
    def rubella(self):
        # Rubella diagnosis based on fever, rash, and swollen lymph nodes
        matched_symptoms = ['fever', 'rash', 'swollen lymph nodes']
        explain_diagnosis('Rubella', matched_symptoms)
        self.declare(Disease(name='Rubella'))
        print("Recommendations: Rest, stay hydrated, and see a doctor if symptoms persist.")
    
    @Rule(Symptom(name='fever') & Symptom(name='rash') & Symptom(name='conjunctivitis'))
    def measles(self):
        # Measles diagnosis based on fever, rash, and conjunctivitis
        matched_symptoms = ['fever', 'rash', 'conjunctivitis']
        explain_diagnosis('Measles', matched_symptoms)
        self.declare(Disease(name='Measles'))
        print("Recommendations: Isolate the patient and seek medical attention.")

    @Rule(Symptom(name='cough') & Symptom(name='difficulty_breathing'))
    def bronchitis(self):
        # Bronchitis diagnosis based on cough and difficulty breathing
        matched_symptoms = ['cough', 'difficulty breathing']
        explain_diagnosis('Bronchitis', matched_symptoms)
        self.declare(Disease(name='Bronchitis'))
        print("Recommendations: Ensure warm fluids, rest, and consult a doctor if breathing worsens.")

    @Rule(Symptom(name='fever') & Symptom(name='sore_throat') & Symptom(name='red_tonsils'))
    def tonsillitis(self):
        # Tonsillitis diagnosis based on fever, sore throat, and red tonsils
        matched_symptoms = ['fever', 'sore throat', 'red tonsils']
        explain_diagnosis('Tonsillitis', matched_symptoms)
        self.declare(Disease(name='Tonsillitis'))
        print("Recommendations: Gargle warm salt water and consult a doctor for antibiotics.")

    @Rule(Disease(name='Rubella'))
    def rubella_followup(self):
        # Follow-up advice for Rubella diagnosis
        print("Rubella Follow-Up: Ensure MMR vaccination if not already vaccinated.")
        print("Alert: Inform the local health authority if confirmed.")

    @Rule(Disease(name='Rubella') & Symptom(name='pregnant'))
    def rubella_pregnancy_risk(self):
        # Special alert for Rubella diagnosis during pregnancy
        print("Alert: Rubella during pregnancy poses high risks to the unborn child. Immediate medical attention required.")
