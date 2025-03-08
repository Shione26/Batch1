# Prog08: Create a program that ask user to input 10 numbers. Print how many are odd numbers.

number_count = 0
odd_count = 0

for i in range(10):
    number = int(input(f"Enter number {number_count + 1}: "))
    number_count += 1

    if number % 2 == 1:
        odd_count += 1

print(odd_count)
