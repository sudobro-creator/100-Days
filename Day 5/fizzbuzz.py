print("This is the FizzBuzz Game.")
print("The game will print numbers from 1 to 100.")
print("If the number is divisible by 3, it will print" "Fizz")
print("If the number is divisible by 5, it will print" "Buzz")
print("If the number is divisible by both 3 and 5, it will print" "FizzBuzz")
print("If the number is not divisible by either, it will print the number itself.")


for number in range(1,101):
    if number % 3 == 0 :
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    elif number % 3 and number % 5 == 0:
        print("FizzBuzz")
    else:
        print(number)