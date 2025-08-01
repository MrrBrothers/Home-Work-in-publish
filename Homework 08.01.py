# clients = ['Michael Scott', 'Dwight Schrute', 'Jim Halpert',
#         'Pam Beesly', 'Kevin Malone']
#
# # выведем третий элемент списка
# print(clients[3])
#
# # изменим третий элемент списка
# clients[3] = 'Pam Halpert'
#
# # выведем третий элемент списка
# print(clients)


# clients = ['Michael Scott', 'Dwight Schrute', 'Jim Halpert',
#         'Pam Beesly', 'Kevin Malone']
#
# # выведем исходный список
# print(clients)
#
# # добавим новый элемент в список
# clients.append('Oscar Martinez')
#
# # выведем получившийся список
# print(clients)
#
# # считаем имя клиента с консоли
# new_client = input('Введите имя клиента: ')
# # добавим этого клиента в список
# clients.append(new_client)
#
# # выведем итоговый список
# print(clients)


# coworkers = ['Tolya', 'Vasya', 'Jenya', 'Sasha', 'Andrew']
#
# print(coworkers[::4])
# print(f'{coworkers[0]}\n{coworkers[-1]}')
# print(f'Количество моих коллег = {len(coworkers)}')
#
# # add a new kolleg!
#
# new_kolleg = input('Press name a new kolleg: ')
# if len(new_kolleg) != 0:
#     coworkers.append(new_kolleg)
# else:
#     print('Имя должно иметь хотя бы один символ!')
#
# print(f'Обнавленный список коллег: {coworkers}')
#
# # Проверка работает ли этот человек со мной?
#
# search_kolleg = input('Press searching name: ')
# if len(search_kolleg) != 0:
#     if search_kolleg in coworkers:
#         print('Этот человек работает с вами!')
#     else:
#         print("Этот человек не найден.")
# else:
#     print("Имя должно содержать буквы.")

# Кортедж
# korteg = (1,)
# print(korteg)

# # Множества!
# set = {1, 2, 3, 5, 1, 2, 3, 1, 1, 4, 7, 1, 6, 8, 9, 1}
# print(set)


# family = ('Kirill', 'Ksunya', 'Anna', 'Vlad')
# print(family[::3])
# print(family[::2])
# print(len(family))
#
# set_numbers = {1,2,2,3,4,5,4,3,5,6,7,8,9,0,4,4,6,7}
# print(set_numbers)
# new_number = int(input('Press number: '))
# if new_number in set_numbers:
#     set_numbers.remove(new_number)
# else:
#     set_numbers.add(new_number)
#
# print(f'Длинна множества = {len(set_numbers)}\n'
#       f'И измененное множество - {set_numbers}')

# МЕТОДЫ ДОБАВЛЕНИЯ И УДАЛЕНИЯ ЭЛЕМЕНТОВ СПИСКА

# clients = ['Michael Scott', 'Dwight Schrute', 'Jim Halpert',
#         'Pam Beesly', 'Kevin Malone']
#
# # добавим несколько элементов в список
# clients.extend(['Oscar Martinez', 'Creed Bratton', 'Andy Bernard'])
#
# # выведем получившийся список
# print(clients)

# clients = ['Michael Scott', 'Dwight Schrute', 'Jim Halpert',
#         'Pam Beesly', 'Kevin Malone']
#
# # добавим элемент по индексу 1
# clients.insert(1, 'Oscar Martinez')
#
# # выведем получившийся список
# print(clients)

# DELETE metod -- .remove

# clients = ['Michael Scott', 'Dwight Schrute', 'Jim Halpert',
#         'Pam Beesly', 'Kevin Malone']
# print(f'Список клиентов: {clients}')
#
# # считываем элемент, который нужно удалить
# name = input('Введите клиента, которого нужно удалить: ')
#
# # удаляем элемент из списка
# clients.remove(name)
# print('Клиент удален из списка.')
#
# # выведем получившийся список
# print(f'Список клиентов: {clients}')


# def check_password(password):
#     # Проверяем длину пароля
#     while True:
#         if len(password) < 8:
#             print('Длина пароля должна быть не менее 8 символов')
#         else:
#             print('Its Ok')
#         upper, lower, digit = False, False, False
#         # ПроверяемПароль должен содержать хотя бы одну цифру каждый символ в пароле
#         for i in password:
#             if i.isupper():
#                 upper = True
#             elif i.islower():
#                 lower = True
#             elif i.isdigit():
#                 digit = True
#         # Проверяем наличие хотя бы одной заглавной буквы, строчной буквы и цифры
#         if not upper:
#             print('Пароль должен содержать хотя бы одну заглавную букву')
#         else:
#             print('Its Ok')
#         if not lower:
#             print('Пароль должен содержать хотя бы одну строчную букву')
#         else:
#             print('Its Ok')
#         if not digit:
#             print('Пароль должен содержать хотя бы одну цифру')
#         else:
#             print('Its Ok')
#
#
#
# def main():
#     password = input("Введите ваш пароль: ")
#     if check_password(password):
#         print('Пароль принят!')
#     else:
#         print('Пароль не соответствует требованиям.')
#     check_password(password)
# main()


import json
from collections import defaultdict
from datetime import datetime

# Считываем данные из файла
with open("orders_july_2023.json", "r", encoding="utf-8") as my_file:
    orders = json.load(my_file)

# Переменные для хранения результатов
max_price = 0
max_order = ''
max_quantity = 0
max_quantity_order = ''
daily_orders_count = defaultdict(int)
user_orders_count = defaultdict(int)
user_total_spent = defaultdict(float)
total_price = 0
total_quantity = 0
order_count = len(orders)

# Обработка данных
for order_num, order_data in orders.items():
    # Получаем данные о заказе
    price = order_data['price']
    quantity = order_data['quantity']
    date = order_data['date']
    user_id = order_data['user_id']

    # 1. Номер самого дорогого заказа
    if price > max_price:
        max_price = price
        max_order = order_num

    # 2. Номер заказа с самым большим количеством товаров
    if quantity > max_quantity:
        max_quantity = quantity
        max_quantity_order = order_num

    # 3. Подсчет количества заказов по дням
    day = datetime.strptime(date, "%Y-%m-%d").date()
    daily_orders_count[day] += 1

    # 4. Подсчет количества заказов по пользователям
    user_orders_count[user_id] += 1

    # 5. Подсчет общей стоимости заказов по пользователям
    user_total_spent[user_id] += price

    # Суммарная стоимость и количество товаров для средних расчетов
    total_price += price
    total_quantity += quantity

# 6. День с наибольшим количеством заказов
most_orders_day = max(daily_orders_count, key=daily_orders_count.get)

# 7. Пользователь с наибольшим количеством заказов
top_user_by_orders = max(user_orders_count, key=user_orders_count.get)

# 8. Пользователь с наибольшей суммарной стоимостью заказов
top_user_by_spent = max(user_total_spent, key=user_total_spent.get)

# 9. Средняя стоимость заказа
average_order_price = total_price / order_count if order_count > 0 else 0

# 10. Средняя стоимость товаров в заказе
average_price_per_item = total_price / total_quantity if total_quantity > 0 else 0

# Вывод результатов
print(f'Номер заказа с самой большой стоимостью: {max_order}, стоимость заказа: {max_price}')
print(f'Номер заказа с самым большим количеством товаров: {max_quantity_order}, количество: {max_quantity}')
print(
    f'День с наибольшим количеством заказов: {most_orders_day}, количество заказов: {daily_orders_count[most_orders_day]}')
print(
    f'Пользователь с наибольшим количеством заказов: {top_user_by_orders}, количество заказов: {user_orders_count[top_user_by_orders]}')
print(
    f'Пользователь с наибольшей суммарной стоимостью заказов: {top_user_by_spent}, сумма: {user_total_spent[top_user_by_spent]}')
print(f'Средняя стоимость заказа: {average_order_price}')
print(f'Средняя стоимость товаров в заказе: {average_price_per_item}')
