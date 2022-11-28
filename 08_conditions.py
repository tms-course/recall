# Общая форма условного выражения
x = 3

# Условное использование
if x == 3:
    print('x = 3')

# Альтернативное использование
if x == 3:
    ...
else:
    ...

# Последовательность условий
if x == 3:
    print('x = 3')
elif x == 4:
    print('x == 4')
else:
    print('Если не подошло ни одно из условий')

if x == 3:
    ...
if x == 4:
    ...



# Тернарный оператор
y = 20 if x == 3 else 10