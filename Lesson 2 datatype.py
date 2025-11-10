Name = "priyanshu yadav"
Age = 21
Height = 1.78
is_student = True

print(f'Name:{Name}')
print(f'Age:{Age}')
print(f'Height: {Height} meters')
print(f'is_student: {is_student}')

a = float(input("Enter first number: "))
b = float(input("Enter second number:"))

print("Sum:", a+b)
print("Average", (a+b)/2)
print("Largest:", max(a,b)) 

name = str(input("Enter your name:"))
age = int(input("Enter your age: "))
country = str(input("Enter your country :"))
height = float(input("Enter your height: "))
is_learn_ml = input("Are you learning ML? (yes/no): ").lower() == "yes"

print(f"Hi {name}")
print(f"you 'r {age} years old, from {country}.")
print(f"Your height is {height} meters.")
print(f'Learing ML: {is_learn_ml}')