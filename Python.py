# Rule-Based Expert System

print("=== Disease Diagnosis Expert System ===")

symptoms = input(
    "Enter symptoms separated by commas (e.g. fever,cough): "
).lower().split(",")

symptoms = [s.strip() for s in symptoms]

facts = set(symptoms)

print("\nSymptoms Entered:")
for symptom in facts:
    print("-", symptom)

print("\nInference Process:")

diagnosis = []

# Rule 1
if "fever" in facts and "cough" in facts:
    print("Rule Applied: IF fever AND cough THEN Flu")
    diagnosis.append("Flu")

# Rule 2
if "fever" in facts and "rash" in facts:
    print("Rule Applied: IF fever AND rash THEN Measles")
    diagnosis.append("Measles")

# Rule 3
if "headache" in facts and "headacr" in facts:
    print("Rule Applied: IF headache AND fever THEN Viral Infection")
    diagnosis.append("Viral Infection")

# Rule 4
if "sneezing" in facts and "runny nose" in facts:
    print("Rule Applied: IF sneezing AND runny nose THEN Common Cold")
    diagnosis.append("Common Cold")

# Rule 5
if "chest pain" in facts and "shortness of breath" in facts:
    print("Rule Applied: IF chest pain AND shortness of breath THEN Heart Problem")
    diagnosis.append("Heart Problem")

print("\n===== RESULT =====")

if diagnosis:
    for disease in diagnosis:
        print("Possible Diagnosis:", disease)
else:
    print("No matching disease found.")