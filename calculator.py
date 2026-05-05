"""Simple command-line calculator."""

import math


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


def power(a, b):
    return a ** b


def sqrt(a):
    if a < 0:
        raise ValueError("Cannot take square root of a negative number")
    return math.sqrt(a)


# Each entry: (name, function, symbol, arity)
OPERATIONS = {
    "1": ("Add", add, "+", 2),
    "2": ("Subtract", subtract, "-", 2),
    "3": ("Multiply", multiply, "*", 2),
    "4": ("Divide", divide, "/", 2),
    "5": ("Power", power, "^", 2),
    "6": ("Square Root", sqrt, "sqrt", 1),
}
EXIT_CHOICE = "7"


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
        for key, (name, _, _, _) in OPERATIONS.items():
            print(f"  {key}. {name}")
        print(f"  {EXIT_CHOICE}. Exit")

        choice = input(f"Enter choice (1-{EXIT_CHOICE}): ").strip()

        if choice == EXIT_CHOICE:
            print("Goodbye!")
            break

        if choice not in OPERATIONS:
            print(f"Invalid choice. Please select 1-{EXIT_CHOICE}.")
            continue

        name, func, symbol, arity = OPERATIONS[choice]

        try:
            if arity == 1:
                a = get_number("Enter number: ")
                result = func(a)
                print(f"Result: {symbol}({a}) = {result}")
            else:
                a = get_number("Enter first number: ")
                b = get_number("Enter second number: ")
                result = func(a, b)
                print(f"Result: {a} {symbol} {b} = {result}")
        except ValueError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
