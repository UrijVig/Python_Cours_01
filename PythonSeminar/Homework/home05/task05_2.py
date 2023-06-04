# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Циклы использовать нельзя

# Примеры/Тесты:
# <function_name>(0,0) -> 0
# <function_name>(0,2) -> 2
# <function_name>(3,0) -> 3

def sum_numbers(a,b):     
    return sum_numbers(a+1, b-1) if b > 0 else a


num_1 = int(input("Введите первое число: "))
num_2 = int(input("Введите второе число: "))

print(f"Смма чисел {num_1} и {num_2} = {sum_numbers(num_1,num_2)}")