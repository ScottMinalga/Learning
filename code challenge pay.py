OVERTIME = 40
DOUBLETIME = 60

hours_worked = float(input("How many hours did you work: "))
Pay_Rate = float(input("Pay rate: "))

if hours_worked <= OVERTIME:
    hours_worked * Pay_Rate
elif