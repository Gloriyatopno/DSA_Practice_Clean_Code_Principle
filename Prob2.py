#Sum 
Num = input("Enter a list of numbers separated by commas: ").split(",")
total = 0
for i in Num:
    total += int(i)

print("The sum of the numbers in the list is:", total)