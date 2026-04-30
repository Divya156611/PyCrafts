def addition(n1,n2):
    return n1+n2
def subtraction(n1,n2):
    return n1-n2
def multiplication(n1,n2):
    return n1*n2
def division(n1,n2):
    return n1/n2
def exponent(n1,n2):
    return n1**n2
op_dict={
    "+":addition,
    "-":subtraction,
    "*":multiplication,
    "/":division,
    "^":exponent
}
def calculator():
    a=float(input("Enter the first number:"))
    for symbol in op_dict:
        print(symbol)
    should_continue=True
    while should_continue:
        operator=input("Pick an operator:")
        b=float(input("Enter the second number:"))
        operation=op_dict[operator]
        output=operation(a,b)
        print(f" {a} {operator} {b} = {output}")
        continue_calculation=input(f"Enter 'y' to continue calculation with {output} or 'n' to start new calculation or'x' for to exit.").lower()
        if continue_calculation=='y':
            a=output
        elif continue_calculation=='n':
            should_continue=False
            calculator()
        else:
            should_continue=False

calculator()


