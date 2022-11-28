##
## Циклы, их виды и ключевые операторы
##

condition = True
x = 10

while condition:
    print('Тело цикла выполняется пока condition=True')

    if x == 1:
        break

    if x == 2:
        continue
else:
    print('Зайдет сюда, если не был вызван break')


for i in range(10):
    print(i)

    if i == 8:
        break

    if i == 2:
        continue
else:
    print('Зайдет сюда, если не был вызван break')

##
## Генераторы списков (list comprehentions)
##

# Пример обычного генератора списка
generated_lst = [i for i in range(10)]

# Пример генератора с условием
conditional_lst = [i for i in range(10) if i % 2 == 0]

# Пример использования генератора со словарем
dct = {'a': 1, 'b': 2, 'c': 3}
gen_dct = {v: k for k, v in dct.items()}

# Пример генератора с вложенным циклом
nested_lst = [[1, 2], [3, 4]]
flat_lst = [j for i in nested_lst for j in i]