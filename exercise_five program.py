# Hello! this program checks if the first and last number of a list are the same.

# pseudocode

def first_last_same(numberList):
    print("Given list:", numberList)
    
    # Check if the first and last number are the same using the equality operator
    return numberList[0] == numberList[-1]

# Test cases
numbers_x = [10, 20, 30, 40, 10]
print("Therefore, the Result is", first_last_same(numbers_x))

numbers_y = [75, 65, 35, 75, 30]
print("Therefore, the Result is", first_last_same(numbers_y))
