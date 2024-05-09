weight = int(input("What is your weight in kilograms? e.g 55 \n:"))
height = float(input("What is your height in meters? e.g 1.70 \n:"))

weight_int = int(weight)
height_float = float(height)

bmi = weight_int / (height_float ** 2)
bmi_rounded = round(float(bmi), 2)

if bmi_rounded < 18.5:
  print(f"Your BMI is {bmi_rounded}, you are underweight.")
elif bmi_rounded <= 25:
  print(f"Your BMI is {bmi_rounded} you have a normal weight.")
elif bmi_rounded <= 30:
  print(f"Your BMI is {bmi_rounded} you are slightly overweight.")
elif bmi_rounded <= 35:
  print(f"Your BMI is {bmi_rounded} you are obese.")
elif bmi_rounded > 35:
  print(f"Your BMI is {bmi_rounded} you are clinically obese.")
