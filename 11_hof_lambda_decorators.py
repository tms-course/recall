##
## Функции высшего порядка и вытекающие
##
from typing import Callable
from numbers import Number

def is_even(num: int):
    return num % 2 == 0

# Функция принимает другую функцию в качестве аргумента
def custom_filter(func: Callable, lst: list) -> list:
    return [item for item in lst if func(item)]

print(custom_filter(is_even, [1, 2, 3, 4]))

# Функция возвращает другую функцию
def create_adder(x: int) -> Callable: 
    def adder(y: int) -> int: 
        return x + y 
    
    return adder 
    
add_15 = create_adder(15) 
    
print(add_15(10))

##
## lambda-функции
##
pow = lambda x: x ** 2
print(pow(3))

##
## Встроенные функции высшего порядка
##
from functools import reduce

print(*filter(is_even, [1, 2, 3, 4]))
print(*map(lambda x: x ** 2, [1, 2, 3, 4]))
print(reduce(lambda a, x: a + x, [1, 2, 3, 4], 0))


##
## Декораторы
##

# Пример декоратора без аргументов
def decorator(func: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        print('!!')
        func(*args, **kwargs)
        print('!!')
    
    return wrapper

# Пример декоратора с аргументами используя функцию
def content_provider(filepath: str) -> Callable:
    def decorator(func: Callable) -> Callable:
        def wrapper(*args, **kwargs):
            with open(filepath, 'r') as f:
                text = f.read()

                func(text, **kwargs)
        
        return wrapper
    return decorator

@content_provider(filepath='./input.json')
def count_lines(text: str):
    return text.count('\n') + 1

# Пример декоратора без аргументов используя класс
class Power:
	def __init__(self, func):
		self._func = func

	def __call__(self, a, b):
		retval = self._func(a, b)
		return retval ** 2


@Power
def multiply_together(a, b):
	return a * b

# Пример параметризованного класса-декоратора 
class Star:
    def __init__(self, n):
        self.n = n

    def __call__(self, fn):
        def wrapper(*args, **kwargs):
            print(self.n*'*')
            result = fn(*args, **kwargs)
            print(result)
            print(self.n*'*')
            return result
        return wrapper

@Star(5)
def add(a, b):
    return a + b