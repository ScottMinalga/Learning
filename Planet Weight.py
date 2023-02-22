# Start of my variables
sNAME = input("What is your name? ")
# Changed my input into a float.
nEARTH = (float(input("How much do you weigh? ")))

# I did all the math and put it into another variable to make the print cleaner to read
nMERCURY = nEARTH * .38
nVENUS = nEARTH * .91
nMOON = nEARTH * .165
nMARS = nEARTH * .38
nJUPITER = nEARTH * 2.34
nSATURN = nEARTH * .93
nURANUS = nEARTH * .92
nNEPTUNE = nEARTH * 1.12
nPLUTO = nEARTH * .066

# I used f strings and the format function and add 10 spaces with 2 decimal points.
print(sNAME, "here are your weights on our Solar System's planets:")
print('{:10}'.format("Weight on Mercury:"), format(nMERCURY, ".2f"))
print('{:10}'.format("Weight on Venus:"), format(nVENUS, ".2f"))
print("Weight on our Moon:", format(nMOON, "10.2f"))
print("Weight on Mars:", nMARS)
print("Weight on Jupiter:", nJUPITER)
print("Weight on Saturn:", nSATURN)
print("Weight on Uranus:", nURANUS)
print("Weight on Neptune:", nNEPTUNE)
print("Weight on Pluto:", nPLUTO)





