# prompt user for inputs and validate input
fDeposit = -1
while fDeposit <= 0:
    try:
        fDeposit = float(input("What is the Original Deposit (positive value): "))
    except ValueError:
        print("Input must be a positive numeric value")
fInterestRate = -1
while fInterestRate <= 0:
    try:
        fInterestRate = float(input("What is the Interest Rate (positive value): "))
    except ValueError:
        print("Input must be a positive numeric value")
iMonths = -1
while iMonths <= 0:
    try:
        iMonths = int(input("What is the Number of Months (positive value): "))
    except ValueError:
        print("Input must be a positive numeric value")
        continue
    if iMonths <= 0:
        print("Input must be a positive numeric value")
fGoal = -1
while fGoal < 0:
    try:
        fGoal = float(input("What is the Goal Amount (can enter 0 but not negative: "))
    except ValueError:
        print("Input must be a positive numeric value")
        continue
    if fGoal < 0:
        print("Input must be a positive numeric value")

# convert interest rate to monthly rate
fMonthlyRate = fInterestRate / 1200

# compute interest and account balance for each month
fAccountBalance = fDeposit
for i in range(1, iMonths+1):
    fAccountBalance *= 1 + fMonthlyRate
    print("Month {0}: ${1:,.2f}".format(i, fAccountBalance))

# determine how many months to reach goal
iMonthsToGoal = 0
while fAccountBalance < fGoal:
    fAccountBalance *= 1 + fMonthlyRate
    iMonthsToGoal += 1

# output result
print("It will take {0:,} months to reach your savings goal of ${1:,.2f}.".format(iMonthsToGoal, fGoal))
