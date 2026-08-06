#Binary Search
arr=[10,20,30,40,50]
target=int(input("Enter the target number to search: "))
print(f"Array: {arr}")
print(f"Target: {target}")

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

if __name__ == "__main__":
    result = binary_search(arr, target)
    if result != -1:
        print(f"Target found at index: {result}")
    else:
        print("Target not found in the array.")
