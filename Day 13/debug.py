# Calculate the factorial of an integer using recursion
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Calculate the average of a list of integers
def calculate_average(numbers):
    if len(numbers) == 0:
        return 0
    total = sum(numbers)
    average = total / len(numbers)
    return average

# Remove even numbers from a list
def remove_even(my_list):
    my_list = [x for x in my_list if x % 2 != 0]
    return my_list



#Examples
n = 5
print(f"Factorial of {n} is {factorial(n)}")

numbers = [1, 2, 3, 4, 5]
average = calculate_average(numbers)
print(f"Average of the list is {average}")

my_list = [1, 2, 3, 4, 5]
filtered_list = remove_even(my_list)
print("Modified List:", filtered_list)
