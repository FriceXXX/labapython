from src.operations import OPERATORS
from src.exception import CalcError

def solve(expression):
    expression = expression.replace("(", "( ")
    expression = expression.replace(")", " )")
    expression = expression.replace("  ", " ")
    answer = rpn_calculator(expression)
    return round(answer, 2)

def rpn_calculator(expression):
    stack = []

    tokens = expression.split()
    i = 0

    while i < len(tokens):
        token = tokens[i]

        if token == '(' or token == '-(':
            neg = False
            if token == '-(':
                neg = True
            bracket_count = 1
            j = i + 1
            token = '('
            while j < len(tokens) and bracket_count > 0:
                if tokens[j] == '(' or tokens[j] == '-(':
                    bracket_count += 1
                elif tokens[j] == ')':
                    bracket_count -= 1
                j += 1

            inner_expression = ' '.join(tokens[i + 1:j - 1])

            try:
                result = rpn_calculator(inner_expression)
                if neg:
                    result = -result
                stack.append(result)
            except Exception as e:
                raise CalcError(f"Ошибка в выражении внутри скобок: {e}")

            i = j
            continue

        elif token == ')':
            raise CalcError("Ошибка: Несогласованные скобки")

        elif token.replace('.', '').replace('-', '').isdigit():
            stack.append(float(token))

        elif token in OPERATORS:
            if len(stack) < 2:
                raise CalcError("Ошибка: Недостаточно операндов для операции")

            try:
                b = stack.pop()
                a = stack.pop()

                if token == '/' and b == 0:
                    raise CalcError("Ошибка: Деление на ноль")

                result = OPERATORS[token](a, b)
                stack.append(result)
            except Exception as e:
                raise CalcError(f"Ошибка при выполнении операции: {e}")
        else:
            raise CalcError(f"Ошибка: Неизвестный токен '{token}'")

        i += 1

    if len(stack) == 0:
        raise CalcError("Ошибка: Пустое выражение")
    elif len(stack) > 1:
        raise CalcError(f"Ошибка: В выражении остались неиспользованные числа: {stack}")

    return stack[0]

