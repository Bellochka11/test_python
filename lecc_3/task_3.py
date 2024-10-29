#  Создайте вручную кортеж содержащий элементы разных типов. 
# ✔ Получите из него словарь списков, где:
# ключ — тип элемента,
# значение — список элементов данного типа

tup = (5, 8.5, 'qwe', 10, 'abc', -3.5)
clovar = {}

for i in tup:
    type_el = type(i)
    if type_el not in clovar:
        clovar[type_el] = []
        
    clovar[type_el].append(i)

print(clovar)