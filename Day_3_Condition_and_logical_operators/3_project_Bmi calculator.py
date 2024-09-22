# BMI 2.0

height = int(input("What is your height in cm? "))
weight = int(input("What is your weight in kg? "))

BMI = (weight/height**2)*10000
BMI = (float(round(BMI, 2))) # <------------------IMPORTANT

if BMI < 18.5:
  print(f"Your BMI is {BMI}, Under weight")
elif BMI>18.5 and BMI<=25:
  print(f"Your BMI is {BMI}, Normal weight")
elif BMI>25 and BMI<=30:
  print(f"Your BMI is {BMI}, Over weight")     
elif BMI>30 and BMI<=35:
  print(f"Your BMI is {BMI}, Obese")
elif BMI>35:
  print(f"Your BMI is {BMI}, Clinically obese")
else:
  print("Error")




# ______________________________________________________
#   Highlights of this session

# Previous Project modification
# If and else
# nested if
# operators(Comparison)
