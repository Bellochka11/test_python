# Пользователь вводит размеры рамки
# width = int(input("Введите ширину рамки: "))
# height = int(input("Введите высоту рамки: "))
width = 3
height = 3
# Внешний цикл отвечает за строки (высота)
for line in range(height + 1):
    # Внутренний цикл отвечает за столбцы (ширина)
    for col in range(width + 1):
        if col == 0 or col == width:
            print('|',end='')
        elif line == 0 or  line == height:
            print('-', end='')
        else:
            print(' ', end='')
    print()

    