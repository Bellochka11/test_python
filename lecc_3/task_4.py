# ✔ Создайте вручную список с повторяющимися элементами.
# ✔ Удалите из него все элементы, которые встречаются дважды.
list_1 = [1,3,5,6,4,3,8,1,9]
dict_1 = {}
for i in list_1:
    if i not in dict_1:
        dict_1[i] = 1
    else:
        dict_1[i] +=1
print(dict_1)
list_2 = [i for i in list_1 if dict_1[i] == 1]
print(list_2)