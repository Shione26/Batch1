# Prog01: Create a program that ask user to input 2 numbers. Print the bigger number

num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))

if num1 > num2:
    print(num1, "is the larger number")
elif num1 < num2:
    print(num2, "is the larger number")

