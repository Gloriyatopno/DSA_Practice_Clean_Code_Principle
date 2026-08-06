#Count Occurrences of an Element using Linear Search
arr = [23,45,67,23,67,89,23,12,45,67]

print("Array:", arr)

target = int(input("Enter the element to search: "))

count = 0

for i in range(len(arr)):
    if arr[i] == target:
        count += 1

if count > 0:
    print(target, "occurs", count, "times.")
else:
    print("Element not found.")