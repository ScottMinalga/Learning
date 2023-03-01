# take our inputs as floats and as inches,pounds
sName = input("Name of the person that we are calculating the BMI for: ")
iHeight = int(input("Supply Height in Inches: "))
iWeight = int(input("Supply Weight in Pounds: "))

# Convert inches and pounds to meters and kilograms
fHEIGHT_METER = iHeight / 39.36
fWEIGHT_KG = iWeight / 2.2

# need to do the math to get your BMI with meters and kg formula
fRESULT = fWEIGHT_KG / fHEIGHT_METER ** 2

# use if elif else to work our way down the tree until we get to our result range
if fRESULT < 18.50:
    print(f"{sName} BMI is: {fRESULT:.2f}")
    print(f"BMI finding is the subject is: Underweight")
elif fRESULT <= 24.90:
    print(f"{sName} BMI is: {fRESULT:.2f}")
    print(f"BMI finding is the subject is: Normal")
elif fRESULT <= 29.90:
    print(f"{sName} BMI is: {fRESULT:.2f}")
    print(f"BMI finding is the subject is: Overweight")
elif fRESULT >= 29.91:
    print(f"{sName} BMI is: {fRESULT:.2f}")
    print(f"BMI finding is the subject is: Obese")