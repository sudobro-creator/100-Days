print('Welcome to BMI Calculator.')
weight = int(input('Enter your weight in kg: '))
height = int(input('Enter your height in cm: '))

bmi = weight / (height ** 2)


if bmi < 18.5:
    print('underweight')
elif bmi > 18.5 and bmi < 24.9:
    print('normal weight')
else:
    print('overweight.')