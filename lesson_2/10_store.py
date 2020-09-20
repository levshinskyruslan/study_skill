#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Есть словарь кодов товаров

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

# Есть словарь списков количества товаров на складе.

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

# Рассчитать на какую сумму лежит каждого товара на складе
# например для ламп

lampa_quantity = store[goods['Лампа']][0]['quantity']
lampa_cost = lampa_quantity * store[goods['Лампа']][0]['price']

table_quantity_1 = store[goods['Стол']][0]['quantity']
table_quantity_2 = store[goods['Стол']][1]['quantity']
all_table_quantity = table_quantity_1 + table_quantity_2
table_cost_1 = table_quantity_1 * store[goods['Стол']][0]['price']
table_cost_2 = table_quantity_2 * store[goods['Стол']][1]['price']
all_table_cost = table_cost_1 + table_cost_2

sofa_quantity_1 = store[goods['Диван']][0]['quantity']
sofa_quantity_2 = store[goods['Диван']][1]['quantity']
all_sofa_quantity = sofa_quantity_1 + sofa_quantity_2
sofa_cost_1 = store[goods['Диван']][0]['price'] * sofa_quantity_1
sofa_cost_2 = store[goods['Диван']][1]['price'] * sofa_quantity_2
all_sofa_cost = sofa_cost_1 + sofa_cost_2

chair_quantity_1 = store[goods['Стул']][0]['quantity']
chair_quantity_2 = store[goods['Стул']][1]['quantity']
chair_quantity_3 = store[goods['Стул']][2]['quantity']
all_chair_quantity = chair_quantity_1 + chair_quantity_2 + chair_quantity_3
chair_cost_1 = store[goods['Стул']][0]['price'] * chair_quantity_1
chair_cost_2 = store[goods['Стул']][1]['price'] * chair_quantity_2
chair_cost_3 = store[goods['Стул']][2]['price'] * chair_quantity_3
all_chair_cost = chair_cost_1 + chair_cost_2 + chair_cost_3

print(f'Лампа - {lampa_quantity} шт, стоимость {lampa_cost} руб\n'
      f'Стол - {all_table_quantity} шт, стоимость {all_table_cost} руб\n'
      f'Диван - {all_sofa_quantity} шт, стоимость {all_sofa_cost} руб\n'
      f'Стул - {all_chair_quantity} шт, стоимость {all_chair_cost} руб')
#lamps_cost = store[goods['Лампа']][0]['quantity'] * store[goods['Лампа']][0]['price']

# # или проще (/сложнее ?)
# lamp_code = goods['Лампа']
# lamps_item = store[lamp_code][0]
# lamps_quantity = lamps_item['quantity']
# lamps_price = lamps_item['price']
# lamps_cost = lamps_quantity * lamps_price
# print('Лампа -', lamps_quantity, 'шт, стоимость', lamps_cost, 'руб')

# Вывести стоимость каждого товара на складе: один раз распечать сколько всего столов, стульев и т.д. на складе
# Формат строки <товар> - <кол-во> шт, стоимость <общая стоимость> руб








