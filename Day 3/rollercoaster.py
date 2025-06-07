print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print('You can ride.')
    age = int(input("How are old are you?"))
    if age <= 12:
        bill = 5
        print('Child Ticket is $5.')
    elif age <= 18:
        bill = 7
        print("Teen Ticket is $7.") 
    elif age >= 45 and age<= 55:
        print("You get a free ride!")
    else:
        bill = 12
        print("Adult Ticket is $12.")
    
    photo_bill = input('Do you want to have a picture? Type y for Yes and n for No. ')
    if photo_bill == 'y':
        bill += 3
        
    print(f'Your final bill is ${bill}.')
else:
    print('You need to go taller to ride the rollercoaster.')