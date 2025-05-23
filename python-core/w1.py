def calculate_stats(numbers):
    if not numbers:
        return 0, None
    avg = sum(numbers) / len(numbers)
    maximum = max(numbers)
    return avg, maximum


def main():
    try:
        input_str = input("Enter numbers separated by spaces: ")
        numbers = [float(x) for x in input_str.split()]
        avg, max_val = calculate_stats(numbers)
        print(f"Average: {avg:.2f}, Maximum: {max_val}")
    except ValueError:
        print("Invalid input: Please enter numeric values only.")


if __name__ == "__main__":
    main()
