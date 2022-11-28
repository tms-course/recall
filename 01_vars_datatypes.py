# Переменная с целочисленным значением
dog_count = 10
type(dog_count) # <type 'int'>

# Переменная со строчным значением
title = "Some article title"
description = """
Текст, состоящий из 
нескольких строк
удобно задавать 
используя тройные ковычки.
"""
type(description) # <type 'str'>

# Переменные с плавающей точкой
pi = 3.14
sci_notation_val1 = 1.35e-05 # 0.0000135
sci_notation_val2 = 6.12e6 # 6120000
type(pi) # <type 'float'>

# Переменные с булевым значением
is_done = True
type(is_done) # <type 'bool'>

# Переменные хранящие коллекции
ids = [10, 23, 35, 18]
type(ids) # <type 'list'>

class Human: ...
# Переменные хранящие объекты классов
john = Human('John', 'Wick')
type(john) # <type 'type'>