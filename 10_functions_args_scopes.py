"""
Общий формат определения функции
def <func_name>(<args>):
    <func_body>
"""

def get_lines(text: str) -> list:
    """Splits text by lines and return the lines without \n"""
    return text.split('\n')

"""
Виды аргументов функций
"""

##
## Функция с аргументом char по-умолчанию равным '!'
##
def print_formatted(string: str, char: str = '!') -> str:
    return f'{char}{string}{char}'
print_formatted("Строка")

##
## Именованные аргументы
##
def custom_power(num: float, pwr: float):
    return num ** pwr + 1

custom_power(pwr=4, num=5)

##
## Сбор аргументов в коллекцию
##
def custom_print(*args) -> None:
    print('!!!', *args)

custom_print(1, 2, 3, 4)

##
## Сбор аргументов в словарь
##
def swap(**kwargs) -> dict:
    return {v: k for k, v in kwargs.items()}

swapped_kwargs = swap(a=1, b=3)

##
## Обобщенное определение функции
##
from typing import Callable

def decorator(func: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)

    return wrapper


##
## Явное указание позиционных и 
## именованных аргументов
##

def strict_sep_args(x, y, *, width, height=10):
    """
    Функция, в которой 
    x, y - только позиционные, 
    width, height - только именованные аргументы """
    ...

def sep_args(x, y, /, width, height=10):
    """
    Функция, в которой 
    x, y - только позиционные, 
    width, height - могут быть и позиционными, и именованными"""
    ...

## =====================================
## ======== Область видимости ==========
## =====================================

x = 10

def func_dont_change_global_x(y: int):
    x = y + 10
    print(x)

print(x)
func_dont_change_global_x(5)
print(x)

########################################

def func_change_global_x():
    global x
    x = 50
    print(x)

print(x)
func_change_global_x()
print(x)

# Присваиваем определение функции переменной
# и можем с ней работать как с обычной переменной или функцией
func_alias = func_change_global_x

func_alias()