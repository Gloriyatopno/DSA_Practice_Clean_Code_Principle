#Selection Sort
arr=[23,45,12,67,89]
print(f"Array before sorting: {arr}")

def selection_sort(arr):
    n=len(arr)
    for i in range(n):
        min=i
        for j in range(i+1,n):
            if arr[j]<arr[min]:
                min=j
        arr[i],arr[min]=arr[min],arr[i]

selection_sort(arr)
print(f"Array after sorting: {arr}")