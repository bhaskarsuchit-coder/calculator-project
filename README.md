# Simple Calculator

A command-line calculator built in Python. It supports basic arithmetic operations along with a few additional features, including input validation and error handling for invalid or undefined operations.

## Features

- Add
- Subtract
- Multiply
- Divide
- Exponent
- Modulo
- Custom operation: `sum_over_difference`  
  Calculates `(a + b) / (a - b)`
- Input validation (keeps asking until a valid number is entered)
- Handles division by zero, modulo by zero, and equal-value edge cases without crashing

## How to Run

1. Make sure Python 3 is installed.
2. Clone this repository.
3. Open the project folder in your terminal.
4. Run the program:

```bash
python calculator.py
```

## Usage

When you run the program, you'll see the following menu:

```
Calculator Operations

1. Add
2. Subtract
3. Multiply
4. Divide
5. Exponent
6. Modulo
7. Sum Over Difference
8. Quit
```

Choose an operation, enter two numbers when prompted, and the program will display the result. Select **8** to exit the application.

## Example

```text
Choose an operation (1-8): 1

Enter the first number: 5
Enter the second number: 3

Result: 8.0
```

## Technologies Used

- Python 3

## Concepts Practiced

- Functions
- Conditional Statements
- Loops
- Input Validation
- Exception Handling
- Arithmetic Operations
