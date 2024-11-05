import tkinter as tk
from tkinter import messagebox
from inference_engine import diagnose

# Initialize main window
root = tk.Tk()
root.title("Medical Diagnosis Expert System")
root.geometry("400x500")

# List of symptoms that are to be RENDERED TO USER
symptoms = {
    'fever': tk.BooleanVar(),
    'cough': tk.BooleanVar(),
    'body_ache': tk.BooleanVar(),
    'sore_throat': tk.BooleanVar(),
    'runny_nose': tk.BooleanVar(),
    'headache': tk.BooleanVar(),
    'fatigue': tk.BooleanVar(),
    'loss_of_taste_or_smell': tk.BooleanVar(),
    'itchy_eyes': tk.BooleanVar(),
    'sneezing': tk.BooleanVar(),
    'facial_pain': tk.BooleanVar(),
    'chest_discomfort': tk.BooleanVar(),
    'shortness_of_breath': tk.BooleanVar()
}

def get_diagnosis():
    # Prepare symptoms dictionary based on user selections
    selected_symptoms = {symptom: var.get() for symptom, var in symptoms.items()}
    possible_diagnoses = diagnose(selected_symptoms)
    
    # Display diagnosis results
    if possible_diagnoses:
        result_text = "Possible diagnoses:\n" + "\n".join(f"- {diagnosis}" for diagnosis in possible_diagnoses)
    else:
        result_text = "No matching diagnosis found."
    
    messagebox.showinfo("Diagnosis Result", result_text)

# Title Label
title_label = tk.Label(root, text="Select your symptoms", font=("Arial", 16))
title_label.pack(pady=10)

# Create and pack checkboxes for each symptom
for symptom, var in symptoms.items():
    checkbox = tk.Checkbutton(root, text=symptom.replace('_', ' ').title(), variable=var)
    checkbox.pack(anchor='w', padx=20)

# Diagnosis Button
diagnose_button = tk.Button(root, text="Get Diagnosis", command=get_diagnosis, bg="blue", fg="white")
diagnose_button.pack(pady=20)

# Run the GUI main loop
root.mainloop()