from src.calc import solve

def main():
    while True:
        expression = input('Введите выражение в обратной польской нотации: ')
        if expression == 'exit' or expression == 'quit' or expression == 'q' or expression == 'выход':
            exit()

        try:
            print('Ответ:  ', solve(expression))
        except Exception as e:
            print(f'Error: {e}')

if __name__ == "__main__":
    main()
