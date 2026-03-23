import art
print(art.logo)
def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2
def calculator():
    Keys = {"+": add,
            "-": subtract,
            "*": multiply,
            "/": divide}
    f_num = int(input("Enter the first number : "))
    continue_the_program = True
    while continue_the_program:
        for key in Keys:
            print(key)
        operation = input("Enter the mathematical operation (a choice of '+', '-', '*' or '/'): ")
        s_num = int(input("Enter the second number : "))
        result = Keys[operation](f_num, s_num)
        print(f"{f_num} {operation} {s_num} = {result}")
        choice = input(f"Type y to continue with the answer {result} or type n if you want to exit...").lower()
        if choice == "y":
            f_num = result
        else:
            continue_the_program = False
            print("\n" * 100)
            calculator()
calculator()
