# ✔ Пользователь вводит строку текста. 
# ✔ Подсчитайте сколько раз встречается 
# каждая буква в строке без использования 
# метода count и с ним. 
# ✔ Результат сохраните в словаре, где ключ —
# символ, а значение — частота встречи 
# символа в строке. 
# ✔ Обратите внимание на порядок ключей. 
# Объясните почему они совпадают 
# или не совпадают в ваших решениях.

stroka = 'в лесу родилась елочка'
clovar = {}
for i in stroka:
    if i not in clovar:
        clovar[i] = 1
    else:
        clovar[i] +=1
print(clovar)