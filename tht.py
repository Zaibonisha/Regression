import re

def evaluate_expression(expression):
    def evaluate_helper(expr):
        if re.match(r'^\d+(\.\d+)?$', expr):
            return expr  # Return the input expression as an immutable string

        if expr.count('(') != expr.count(')'):
            raise ValueError("Invalid Expression")

        operators = "+-*/"
        for operator in operators:
            depth = 0
            for i in range(len(expr) - 1, -1, -1):
                if expr[i] == '(':
                    depth -= 1
                elif expr[i] == ')':
                    depth += 1
                elif depth == 0 and expr[i] == operator:
                    left_expr = evaluate_helper(expr[:i])
                    right_expr = evaluate_helper(expr[i + 1:])
                    if operator == '+':
                        return left_expr + right_expr
                    elif operator == '-':
                        return left_expr + operator + right_expr
                    elif operator == '*':
                        return left_expr + operator + right_expr
                    elif operator == '/':
                        if right_expr == "0":
                            raise ValueError("Division by zero")
                        return left_expr + operator + right_expr

        if expr.startswith('(') and expr.endswith(')'):
            return evaluate_helper(expr[1:-1])

        raise ValueError("Invalid Expression")

    try:
        cleaned_expression = re.sub(r'[^0-9+\-*/().]', '', expression)
        result = evaluate_helper(cleaned_expression)
        return result  # Return the result as an immutable string
    except ValueError as e:
        raise e

# Test cases
valid_test_cases = [
    "3 + 12 * 3 / 12",
    "(3 + 3) * 42 / (6 + 12)",
]

invalid_test_cases = [
    "4 (12E)",
    "4 (41)",
    "42+43**271",
]

print("Valid Test Cases:")
for expression in valid_test_cases:
    try:
        result = evaluate_expression(expression)
        print(f"{expression} => {result}")
    except ValueError as e:
        print(e)

print("\nInvalid Test Cases:")
for expression in invalid_test_cases:
    try:
        result = evaluate_expression(expression)
        print(f"{expression} => {result}")
    except ValueError as e:
        print(e)