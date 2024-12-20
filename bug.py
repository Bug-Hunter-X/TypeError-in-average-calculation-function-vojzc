def calculate_average(numbers):
    if not numbers:  # Handle empty list case
        return 0
    return sum(numbers) / len(numbers)

# Example usage with a list containing strings
my_list = [1, 2, 'a', 4, 5]
average = calculate_average(my_list)
print(f"The average is: {average}")

