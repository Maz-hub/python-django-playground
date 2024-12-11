
import sys #import module that would exit the program if something went wrong

try:
    x = int(input('x: '))
    y = int(input('y: '))
except ValueError:
    print('Error: Please input a number.')
    # Exit the program
    sys.exit(1)

try:
    result = x / y
except ZeroDivisionError:
    print('Error: Cannot devide by 0.')
    # Exit the program
    sys.exit(1)

print(f'{x} / {y} = {result}')

