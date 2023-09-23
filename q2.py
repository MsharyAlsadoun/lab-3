def largest_number(numbers):
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num

    return largest


numbers = [5, 2, 9, 1, 7, 4]
largestNum = largest_number(numbers)

if largestNum is not None:
    print("largest number is:", largestNum)
else:
    print("The list is empty.")