#  Три друга взяли вещи в поход. Сформируйте 
# словарь, где ключ — имя друга, а значение —
# кортеж вещей. Ответьте на вопросы:
# ✔ Какие вещи взяли все три друга
# ✔ Какие вещи уникальны, есть только у одного друга
# ✔ Какие вещи есть у всех друзей кроме одного 
# и имя того, у кого данная вещь отсутствует
# ✔ Для решения используйте операции 
# с множествами. Код должен расширяться 
# на любое большее количество друзей.

# Создаем словарь с именами друзей и их вещами
friends_items = {
    "Алексей": ("палатка", "спальный мешок", "фляга", "бутерброды"),
    "Сергей": ("палатка", "спальный мешок", "бутерброды", "фотоаппарат"),
    "Иван": ("палатка", "фляга", "бутерброды", "карта")
}

# Извлекаем вещи для анализа
items = {friend: set(items) for friend, items in friends_items.items()}

# Вычисляем вещи, которые взяли все три друга
common_items = set.intersection(*items.values())

# Вычисляем уникальные вещи, которые есть только у одного друга
unique_items = set()
for friend, friend_items in items.items():
    if len(friend_items) == 1:
        unique_items.update(friend_items)
    else:
        unique_items.update(friend_items - set.union(*(items[i] for i in items if i != friend)))

# Вещи, которые есть у всех, кроме одного друга
excluded_items = {}
for friend in items.keys():
    excluded = set.intersection(*(items[i] for i in items if i != friend))
    excluded_items[friend] = excluded

# Вывод результатов
print("Вещи, которые взяли все три друга:", common_items)
print("Уникальные вещи:", unique_items)
print("Вещи, которые есть у всех, кроме одного друга:")
for friend, items in excluded_items.items():
    print(f"{items} отсутствует у {friend}")
