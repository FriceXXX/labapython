def solve(expression):
    expression = expression.replace("(", " ( ")
    expression = expression.replace(")", " ) ")
    expression = expression.replace("  ", " ")
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

    tokens = expression.split()
    i = 0

    while i < len(tokens):
        token = tokens[i]

        if token == '(':
            bracket_count = 1
            j = i + 1
            while j < len(tokens) and bracket_count > 0:
                if tokens[j] == '(':
                    bracket_count += 1
                elif tokens[j] == ')':
                    bracket_count -= 1
                j += 1

            inner_expression = ' '.join(tokens[i + 1:j - 1])

            try:
                result = rpn_calculator(inner_expression)
                stack.append(result)
            except Exception as e:
                return f"Ошибка в выражении внутри скобок: {e}"

            i = j
            continue

        elif token == ')':
            return "Ошибка: Несогласованные скобки"

        elif token.replace('.', '').replace('-', '').isdigit():
            stack.append(float(token))

        elif token in operators:
            if len(stack) < 2:
                return "Ошибка: Недостаточно операндов для операции"

            try:
                b = stack.pop()
                a = stack.pop()

                if token == '/' and b == 0:
                    return "Ошибка: Деление на ноль"

                result = operators[token](a, b)
                stack.append(result)
            except Exception as e:
                return f"Ошибка при выполнении операции: {e}"
        else:
            return f"Ошибка: Неизвестный токен '{token}'"

        i += 1

    if len(stack) == 0:
        return "Ошибка: Пустое выражение"
    elif len(stack) > 1:
        return f"Ошибка: В выражении остались неиспользованные числа: {stack}"

    return stack[0]

