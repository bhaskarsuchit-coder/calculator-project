"""Simple command-line calculator."""



def add(a: float, b: float) -> float:
    return a + b


def subtract(a: float, b: float) -> float:
    return a - b


def multiply(a: float, b: float) -> float:
    return a * b


def divide(a: float, b: float) -> float:
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b


def exponent(a: float, b: float) -> float:
    return a ** b


def modulo(a: float, b: float) -> float:
    if b == 0:
        raise ZeroDivisionError("Cannot modulo by zero")
    return a % b

def new_maths(a: float, b: float) -> float:
    if a == b:
        raise ZeroDivisionError("Cannot perform new operation with equal values")
    return (a + b) /(a - b)



def parse_number(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid number. Please enter a valid numeric value.")


def choose_operation() -> str:
    options = {
        "1": "Add",
        "2": "Subtract",
        "3": "Multiply",
        "4": "Divide",
        "5": "Exponent",
        "6": "Modulo",
        "7": "New_Operation",
        "8": "Quit"
    }

    print("\nCalculator operations:")
    for key, name in options.items():
        print(f"  {key}. {name}")

    while True:
        choice = input("Choose an operation (1-8): ").strip()
        if choice in options:
            return choice
        print("Invalid choice. Enter a number from 1 to 8.")


def main() -> None:
    print("Simple Calculator")
    print("Type values when prompted and choose an operation from the menu.")

    while True:
        choice = choose_operation()
        if choice == "8":
            print("Goodbye!")
            break

        a = parse_number("Enter the first number: ")
        b = parse_number("Enter the second number: ")

        try:
            if choice == "1":
                result = add(a, b)
            elif choice == "2":
                result = subtract(a, b)
            elif choice == "3":
                result = multiply(a, b)
            elif choice == "4":
                result = divide(a, b)
            elif choice == "5":
                result = exponent(a, b)
            elif choice == "6":
                result = modulo(a, b)
            elif choice == "7":
                result = new_maths(a, b)
            else:
                print("Unexpected operation.")
                continue

            print(f"Result: {result}\n")
        except ZeroDivisionError as exc:
            print(f"Error: {exc}\n")


if __name__ == "__main__":
    main()
