#Author: Scott Minalga
#Date:   2/21/2023

# Prompt for person's name
sName = input("Name of person that we are calculating the grades for:  ")

# Prompt for test scores
iGrade_1 = int(input("Please enter Test 1 score: "))
iGrade_2 = int(input("Please enter Test 2 score: "))
iGrade_3 = int(input("Please enter Test 3 score: "))
iGrade_4 = int(input("Please enter Test 4 score: "))

# Prompt to drop lowest grade
bDrop_Lowest = input(f"Do you wish to drop the lowest grade? Enter Y or N: ")

# Check for negative test scores
if iGrade_1 < 0 or iGrade_2 < 0 or iGrade_3 < 0 or iGrade_4 < 0:
    print("Test scores must be greater than 0.")
    raise SystemExit

# Check if user entered correct value to drop lowest grade
if bDrop_Lowest != "Y" and bDrop_Lowest != "N":
    print("Enter Y or N to Drop the Lowest Grade.")
    raise SystemExit

# Calculate average
if bDrop_Lowest == "Y":
    if iGrade_1 <= iGrade_2 and iGrade_1 <= iGrade_3 and iGrade_1 <= iGrade_4:
        fLowest = iGrade_1
    elif iGrade_2 <= iGrade_3 and iGrade_2 <= iGrade_4:
        fLowest = iGrade_2
    elif iGrade_3 <= iGrade_4:
        fLowest = iGrade_3
    else:
        fLowest = iGrade_4
    fAverage = (iGrade_1 + iGrade_2 + iGrade_3 + iGrade_4 - fLowest) / 3.0
else:
    fAverage = (iGrade_1 + iGrade_2 + iGrade_3 + iGrade_4) / 4.0

# Determine letter grade
if fAverage >= 97.0:
    sGrade = "A+"
elif fAverage >= 94.0:
    sGrade = "A"
elif fAverage >= 90.0:
    sGrade = "A-"
elif fAverage >= 87.0:
    sGrade = "B+"
elif fAverage >= 84.0:
    sGrade = "B"
elif fAverage >= 80.0:
    sGrade = "B-"
elif fAverage >= 77.0:
    sGrade = "C+"
elif fAverage >= 74.0:
    sGrade = "C"
elif fAverage >= 70.0:
    sGrade = "C-"
elif fAverage >= 67.0:
    sGrade = "D+"
elif fAverage >= 64.0:
    sGrade = "D"
elif fAverage >= 60.0:
    sGrade = "D-"
else:
    sGrade = "F"

# Output results
print(f"""{sName} test average is: {fAverage:.1f}
Letter grade for the test is: {sGrade}""")
