#Bubble Sort
arr=[67,23,45,78,43]
print(f"Array before sorting: {arr}")

def bubble_sort(arr):
    n= len(arr)
    for i in range(n):
        swapped=False
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swapped=True
        if not swapped:
            break

bubble_sort(arr)
print(f"Array after sorting: {arr}")