# Calculate the Factorial of a Number

number = int(input("Enter a positive number: "))

if number < 0:
    print("Factorial does not exist for negative numbers.")
else:
    factorial = 1

    for value in range(1, number + 1):
        factorial *= value

    print(f"The factorial of {number} is: {factorial}")