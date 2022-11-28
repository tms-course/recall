dog_count_str = str(10)  
# 10 -> "10"

pi_no_fraction = int(3.14)        
# 3.14 -> 3

true_to_float = float(True)  
# True -> 1.0

class Human: ...
float_john = float(Human())        
# Будет работать, если в классе Human 
# переопределен метод __float__

line = input('Введите список чисел: ')
nums = [int(num) for num in line.split()]
print(sum(nums))