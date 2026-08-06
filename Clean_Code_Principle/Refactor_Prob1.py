# Find First and Last Position of an Element using Binary Search

numbers = [10, 10, 20, 20, 30, 40, 50, 50, 60]

print("Array:", numbers)


def find_position(numbers, target, find_first):
    left = 0
    right = len(numbers) - 1
    position = -1

    while left <= right:
        middle = (left + right) // 2

        if numbers[middle] == target:
            position = middle

            if find_first:
                right = middle - 1
            else:
                left = middle + 1

        elif numbers[middle] < target:
            left = middle + 1

        else:
            right = middle - 1

    return position


def search_range(numbers, target):
    first_position = find_position(numbers, target, True)
    last_position = find_position(numbers, target, False)

    return [first_position, last_position]


target_number = int(input("Enter the target number to search: "))

result = search_range(numbers, target_number)

print("First and Last Position of", target_number, ":", result)