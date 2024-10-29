# ✔ В большой текстовой строке подсчитать количество встречаемых 
# слов и вернуть 10 самых частых. Не учитывать знаки препинания 
# и регистр символов. За основу возьмите любую статью 
# из википедии или из документации к языку.

stroka = 'В лесу родилась елочка в лесу она росла елочка лесу'
stroka = stroka.upper().split()
print(stroka)
clovar = {}
for i in stroka:
    if i not in clovar:
        clovar[i] = 1
    else:
        clovar[i] +=1
print(clovar)
max_key = max(clovar, key=clovar.get)
print(f' Слово {max_key} встречалось в списке {clovar[max_key]} раз')