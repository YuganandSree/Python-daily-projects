
# 📌 Python CLI Calculator

A simple command-line calculator built in Python that supports continuous operations using basic arithmetic functions. This project demonstrates function mapping, control flow, and user interaction in a clean and modular way.

---

## 🚀 Features

- Supports basic operations:
  - Addition (+)
  - Subtraction (-)
  - Multiplication (*)
  - Division (/)
- Interactive CLI interface
- Continuous calculations using previous result
- Function-based architecture with operation mapping
- ASCII art logo integration for better user experience

---

## 🧠 How It Works

- Each mathematical operation is implemented as a separate function.
- A dictionary (Keys) maps operator symbols to their respective functions.
- The program workflow:
  1. Takes the first number input
  2. Displays available operations
  3. Prompts the user to select an operation
  4. Takes the second number
  5. Executes the selected operation dynamically
  6. Displays the result
  7. Allows chaining calculations using the previous result

---

## 🏗️ Project Structure

main.py        # Core calculator logic  
art.py         # Contains ASCII logo  

---

## ▶️ Example Run

Enter the first number: 8

+
-
*
/

Enter the mathematical operation: +
Enter the second number: 4

8 + 4 = 12

Type y to continue with 12 or n to exit: y

---

## ⚙️ Key Concepts Used

- Functions & modular design
- Dictionaries as function dispatch tables
- While loops for continuous execution
- User input handling
- String formatting (f-strings)

---

## ⚠️ Known Limitations

- No validation for invalid operator input
- Division by zero is not handled
- Accepts only integer inputs
- Uses recursion for restart, which is not optimal for scaling

---

## 🔧 Future Improvements

- Add input validation and error handling
- Handle division by zero safely
- Support floating-point numbers
- Replace recursion with loop-based restart
- Add unit tests
- Improve CLI UX (colors, better prompts)

---

## 📚 Learning Outcome

This project is part of a hands-on learning journey to master Python fundamentals, focusing on:
- Control flow
- Data structures
- Function design
- CLI-based application development
