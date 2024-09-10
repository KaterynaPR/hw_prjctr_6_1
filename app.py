def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def main():
    while True:
        choice = input('Input number operation: 1 - you want to add, 2 - to subtract or "q" to quit: ')

        if choice == 'q':
            print('Goodbye!')
            break

        if choice in ['1', '2']:
            num1 = float(input('Input first number: '))
            num2 = float(input('Input 2nd number: '))

            if choice == '1':
                print(f'Result: {num1} + {num2} = {add(num1, num2)}')
            elif choice == '2':
                print(f'Result: {num1} - {num2} = {subtract(num1, num2)}')
        else:
            print('Not correct. Choose 1(to add) or 2(to subtract) ')

if __name__ == "__main__":
    main()