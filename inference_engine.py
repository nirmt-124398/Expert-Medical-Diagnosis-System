# inference_engine.py

from knowledge_base import knowledge_base

def diagnose(symptoms):
    # Count the total number of symptoms the user has selected
    user_symptom_count = sum(symptoms.values())
    
    possible_diagnoses = []
    
    for entry in knowledge_base:
        disease = entry['diagnosis']
        disease_symptoms = entry['symptoms']
        
        # Count matching symptoms between user input and disease symptoms
        match_count = sum(
            1 for symptom, present in symptoms.items()
            if present and disease_symptoms.get(symptom) == present
        )
        
        # Calculate similarity score relative to both the disease and user input
        total_disease_symptoms = sum(disease_symptoms.values())
        similarity_score = match_count / max(total_disease_symptoms, user_symptom_count)
        
        # Use a higher threshold, e.g., 70% to 80% match requirement
        if similarity_score >= 0.7:
            possible_diagnoses.append(disease)
    
    return possible_diagnoses