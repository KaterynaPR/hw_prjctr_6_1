def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def main():
    while True:
        choice = input('Input number operation: 1 - you want to add, 2 - to subtract, 3 - to multiply, 4 - to divide, or "q" to quit: ')

        if choice == 'q':
            print('Goodbye!')
            break

        if choice in ['1', '2', '3', '4']:
            num1 = float(input('Input first number: '))
            num2 = float(input('Input second number: '))

            if choice == '1':
                print(f'Result: {num1} + {num2} = {add(num1, num2)}')
            elif choice == '2':
                print(f'Result: {num1} - {num2} = {subtract(num1, num2)}')
            elif choice == '3':
                print(f'Result: {num1} * {num2} = {multiply(num1, num2)}')
            elif choice == '4':
                print(f'Result: {num1} / {num2} = {divide(num1, num2)}')
        else:
            print('Not correct. Choose 1(to add), 2(to subtract), 3(to multiply), 4(to divide)')

if __name__ == "__main__":
    main()