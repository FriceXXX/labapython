def solve(expression):
    if ")" in expression:
        solve(expression.split(')')[0])

    # expression = expression.replace("(", " ")
    # expression = expression.replace(")", " ")
    # expression = expression.replace("  ", " ")
    answer = rpn_calculator(expression)
    return answer

def rpn_calculator(expression):
    stack = []
    operators = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y,
        '**': lambda x, y: x ** y
    }

    for token in expression.split():
        if token.replace('.', '').replace('-', '').isdigit():
            stack.append(float(token))
        elif token in operators:
            if len(stack) < 2:
                raise ValueError("Недостаточно операндов")

            b = stack.pop()
            a = stack.pop()

            if token == '/' and b == 0:
                raise ZeroDivisionError("Деление на ноль")

            result = operators[token](a, b)
            stack.append(result)
        else:
            raise ValueError(f"Неизвестный токен: {token}")

    if len(stack) != 1:
        raise ValueError("Некорректное выражение")

    return stack[0]

