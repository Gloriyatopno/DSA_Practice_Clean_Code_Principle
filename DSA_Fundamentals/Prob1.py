#Find Largest Num
Num = input("Enter a list of numbers separated by commas: ").split(",")
largest = Num[0]
for i in Num:
    if i > largest:
        largest = i
print("The largest number in the list is:", largest)