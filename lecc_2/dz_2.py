# Программа принимает два целых числа и находит их наибольший общий делитель (НОД).

num2 = int(input('Введите первое число: '))
num1 = int(input('Введите второе число: '))
while num1 > 0:
    num1, num2 =  num2 % num1, num1
print(f'Наибольший общий делитель равен {num2}')
