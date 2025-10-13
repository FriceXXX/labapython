from src.calc import solve

def main():
    while True:
        expression = input('Enter expression: ')
        if expression == 'exit':
            exit()

        try:
            print('>>', solve(expression))
        except Exception as e:
            print(f'Error: {e}')

if __name__ == "__main__":
    main()
