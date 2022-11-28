import sys

# Функции, для работы с вводом
user_line = input('Строка, перед пользовательским вводом')
type(user_line) # <type 'str'>

for line in sys.stdin:
    ...

# Функции, для работы с выводом
print('Hello, world')
sys.stdout.write('Hello, world')