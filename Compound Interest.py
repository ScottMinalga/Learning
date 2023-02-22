#First lets start with getting the varibles and info we will need
fPrincipal = float(input("Enter the starting principal: "))
fRate = float(input("Enter the annual interest rate: "))
fTimes = float(input("How many times per year is the interest compounded? "))
fYears = float(input("For how many years will the account earn interest? "))

#Need to load the formula into the varible
fFINAL = fPrincipal * (((1 + (fRate/fYears) / 100) ** (fYears*fTimes)))

#Print the result
print(f"At the end of {int(fTimes)}, years you will have ${fFINAL:.2f}")





