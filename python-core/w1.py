def calculate_stats(numbers):
    """
    Calculate the average and maximum of a list of numbers.
    Returns (average, maximum) as a tuple.
    If the list is empty, average is 0 and maximum is None.
    """
    if not numbers:
        return 0, None
    avg = sum(numbers) / len(numbers)
    maximum = max(numbers)
    return avg, maximum


def main():
    try:
        # Prompt user for input: numbers separated by spaces
        input_str = input("Enter numbers separated by spaces: ")
        # Convert input strings to floats
        numbers = [float(x) for x in input_str.split()]

        # Calculate average and maximum using the function
        avg, max_val = calculate_stats(numbers)

        # Output results with formatted string
        print(f"Average: {avg:.2f}, Maximum: {max_val}")
    except ValueError:
        # Handle non-numeric input
        print("Invalid input: Please enter numeric values only.")


if __name__ == "__main__":
    main()
