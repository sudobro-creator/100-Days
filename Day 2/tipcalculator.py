print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
tip_percent = tip / 100 * bill + bill
total_bill = (tip_percent / people)
total_bill_round = round(total_bill, 2)
print(f"Each person should pay: {total_bill_round}")