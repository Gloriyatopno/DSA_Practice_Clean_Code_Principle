# Display Even Numbers, Odd Numbers, and the Sum of Even Numbers

even_numbers = []
odd_numbers = []
sum_of_even_numbers = 0

for number in range(1, 51):
    if number % 2 == 0:
        even_numbers.append(number)
        sum_of_even_numbers += number
    else:
        odd_numbers.append(number)

print("----- Even Numbers (1 to 50) -----")
print(even_numbers)

print("\n----- Odd Numbers (1 to 50) -----")
print(odd_numbers)

print("\n----- Summary -----")
print("Sum of Even Numbers:", sum_of_even_numbers)