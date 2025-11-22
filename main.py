# Simple BMI Calculator by Himakshi
print("=== WELCOME TO MY BMI CALCULATOR ===\n")
name = input("Enter your name: ")
weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in cm: "))
bmi = weight / ((height/100) ** 2)
print("\n" + "="*30)
print("Hello", name)
print("Your BMI =", round(bmi, 2))
if bmi < 18.5:
    print("Underweight - Eat more")
elif bmi < 25:
    print("Normal - Great!")
elif bmi < 30:
    print("Overweight - Walk daily")
else:
    print("Obese - Take care")
f = open("data/records.txt", "a")
f.write(name + " | BMI: " + str(round(bmi,2)) + " | 25-Nov-2025\n")
f.close()
print("Record saved!")
input("Press Enter to exit...")
