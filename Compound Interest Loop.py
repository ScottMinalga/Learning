# Prompt user for deposit amount, interest rate, number of months, and savings goal
while True:
    try:
        deposit = float(input("Enter the deposit amount: "))
        interest_rate = float(input("Enter the annual interest rate as a percentage: "))
        months = int(input("Enter the number of months: "))
        goal = float(input("Enter the savings goal: "))
        if deposit <= 0 or interest_rate <= 0 or months <= 0:
            print("Error: Deposit, interest rate, and number of months must be positive and non-zero values.")
            continue
        if goal < 0:
            print("Error: Savings goal must be a non-negative value.")
            continue
        break
    except ValueError:
        print("Error: Please enter a numeric value for deposit, interest rate, months, and goal.")

# Convert interest rate to a monthly rate
monthly_rate = interest_rate / 1200

# Compute the compounded balance for each month up to the given number of months
balance = deposit
for i in range(months):
    interest = balance * monthly_rate
    balance += interest
    print("Month {:2d}: ${:,.2f}".format(i+1, balance))

# Compute the number of months it will take to reach the savings goal
months_to_goal = 0
while balance < goal:
    interest = balance * monthly_rate
    balance += interest
    months_to_goal += 1
print("It will take {} months to reach your savings goal of ${:,.2f}.".format(months_to_goal, goal))
