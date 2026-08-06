#Find First and Last Position of Element

nums=[10,20,30,40,50,50,60,10,20]
print(f"Array: {nums}")

def search_range(nums, target):
    def find_bound(is_first):
        low, high = 0, len(nums) - 1
        bound = -1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                bound = mid
                if is_first:
                    high = mid - 1  
                else:
                    low = mid + 1  
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return bound

    return [find_bound(True), find_bound(False)]

if __name__ == "__main__":
    target = int(input("Enter the target number to search: "))
    result = search_range(nums, target)
    print(f"First and Last Position of {target}: {result}")



