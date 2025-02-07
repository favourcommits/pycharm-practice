weight=float(input("Enter weight in kg: "))
height=float(input("Enter height in metres: "))

# Calculation of bmi
bmi=weight/(height**2)
print("Your BMI is",bmi)

if bmi < 18.5:
    classification='Underweight'
elif bmi < 25:
    classification = 'Normal weight'
elif bmi < 30:
    classification = 'overweight'
else:
    classification = 'Obesity'
print(F"Your BMI is {bmi:2f}, which is considered {classification}")

