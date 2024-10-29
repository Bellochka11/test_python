# Напишите программу банкомат. 
# ✔ Начальная сумма равна нулю
# ✔ Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой 
# операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег

balans = 0
count = 0
while True:
    print('выберите действие: \n 1. пополнить \n 2. снять \n 3. выйти')
    choice = int(input())
    if choice == 1:
        if balans > 5000000:
            balans -= (balans * 10) / 100
        replenish = int(input('Введите сумму для пополнения: '))
        if replenish % 50 == 0:
            balans += replenish
        else:
            print("сумма для пополнения должна быть кратна 50")
        print(balans)
        count +=1
    if choice == 2:
        if balans > 5000000:
            balans -= (balans * 10) / 100
        remove = int(input('Введите сумму для снятия: '))
        if remove > balans:
            print('снять больше чем на балансе нельзя!')
            continue
        else:
            procent = (balans * 1.5) / 100
            if remove % 50 == 0:
                if 30 < procent < 600:
                    balans -= remove - procent
                else:
                    balans -= remove
            else:
                print("сумма для снятия должна быть кратна 50")
            print(balans)
        count +=1
    if choice == 3:
        print(balans)
        break
    if count == 3:
        balans += (balans * 3) / 100
    print(f'операция номер {count}')