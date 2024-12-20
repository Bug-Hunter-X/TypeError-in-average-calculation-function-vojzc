def calculate_average(numbers):
    numeric_numbers = [num for num in numbers if isinstance(num, (int, float))]
    if not numeric_numbers:
        return 0
    return sum(numeric_numbers) / len(numeric_numbers)

# Example usage with a list containing strings
my_list = [1, 2, 'a', 4, 5]
average = calculate_average(my_list)
print(f"The average is: {average}")
