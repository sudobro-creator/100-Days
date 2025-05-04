print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print('You can ride.')
    age = int(input("How are old are you?"))
    if age <= 12:
        print('You have to pay $5.')
    elif age <= 18:
        print("You have to pay $7.") 
    else:
        print("Pay $12.")   
else:
    print('You need to go taller to ride the rollercoaster.')