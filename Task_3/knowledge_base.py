from experta import Fact

# Fact definitions
class Symptom(Fact):
    """Represents a symptom."""
    pass

class Disease(Fact):
    """Represents a disease."""
    pass

# Rules stored as structured data
rules = [
    {
        'disease': 'Rubella',
        'conditions': ['fever', 'rash', 'swollen_lymph_nodes'],
        'recommendation': "Rest, stay hydrated, and see a doctor if symptoms persist."
    },
    {
        'disease': 'Measles',
        'conditions': ['fever', 'rash', 'conjunctivitis'],
        'recommendation': "Isolate the patient and seek medical attention."
    },
    {
        'disease': 'Bronchitis',
        'conditions': ['cough', 'difficulty_breathing'],
        'recommendation': "Ensure warm fluids, rest, and consult a doctor if breathing worsens."
    },
    {
        'disease': 'Tonsillitis',
        'conditions': ['fever', 'sore_throat', 'red_tonsils'],
        'recommendation': "Gargle warm salt water and consult a doctor for antibiotics."
    }
]
