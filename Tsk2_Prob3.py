#Sort Array in Decending Order using Bubble Sort
arr = [56,23,76,19,34,98]

print("Original Array:", arr)

n = len(arr)

for i in range(n):
    for j in range(0, n - i - 1):
        if arr[j] < arr[j + 1]:  
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

print("Sorted Array (Descending):", arr)