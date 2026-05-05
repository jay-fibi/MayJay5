"""Simple command-line calculator."""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


OPERATIONS = {
    "1": ("Add", add, "+"),
    "2": ("Subtract", subtract, "-"),
    "3": ("Multiply", multiply, "*"),
    "4": ("Divide", divide, "/"),
}


def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid number. Please try again.")


def main():
    print("Simple Calculator")
    print("-----------------")

    while True:
        print("\nSelect operation:")
        for key, (name, _, _) in OPERATIONS.items():
            print(f"  {key}. {name}")
        print("  5. Exit")

        choice = input("Enter choice (1-5): ").strip()

        if choice == "5":
            print("Goodbye!")
            break

        if choice not in OPERATIONS:
            print("Invalid choice. Please select 1-5.")
            continue

        a = get_number("Enter first number: ")
        b = get_number("Enter second number: ")

        name, func, symbol = OPERATIONS[choice]
        try:
            result = func(a, b)
            print(f"Result: {a} {symbol} {b} = {result}")
        except ValueError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
