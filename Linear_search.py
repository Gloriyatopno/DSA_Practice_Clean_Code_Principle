#Linear Search

arr=[25,60,67,23,45]
target=input("Enter the target number to search: ")
print(f"Array: {arr}")
print(f"Target: {int(target)}")

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return-1

if __name__ == "__main__":
    result = linear_search(arr, int(target))
    if result != -1:
        print(f"Target found at index: {result}")
    else:
        print("Target not found in the array.")