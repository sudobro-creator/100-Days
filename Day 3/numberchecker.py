first_no = int(input("Enter first number: "))
second_no = int(input("Enter first number: "))
calculation = first_no % second_no
print(calculation)

if calculation != 0:
    print(f"{calculation} is odd.")
else:
    print(f"{calculation} is even.")