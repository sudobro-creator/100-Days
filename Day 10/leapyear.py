def is_leap_year(year):
    # Write your code here.
    if int(year) % 4 == 0:
        print("Leap")
    elif int(year) % 400 == 0:
        print("Leap")
    elif int(year) % 100:
        print("Not Leap")

restart = True
while restart:
    is_leap_year(year=input("Enter the year: "))

    should_continue = input("Do you want to try again? Type y for yes and n for no: ")
    if should_continue == "no":
        restart = False