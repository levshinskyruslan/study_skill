#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь координат городов

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - корень из (x1 - x2) ** 2 + (y1 - y2) ** 2



moscow = sites['Moscow']
london = sites['London']
paris = sites['Paris']

moscow_to_london = ((moscow[0] - london[0]) ** 2 + ((moscow[1] - london[1]) ** 2)) ** .5
moscow_to_paris = ((moscow[0] - paris[0]) ** 2 + (moscow[1] - paris[1]) ** 2) ** 0.5
london_to_moscow = ((london[0] - moscow[0]) ** 2 + (london[1] - moscow[1]) ** 2) ** .5
london_to_paris = ((london[0] - paris[0]) ** 2 + (london[1] - paris[1]) ** 2) ** .5
paris_to_moscow = ((paris[0] - moscow[0]) ** 2 + (paris[1] - moscow[1]) ** 2) ** .5
paris_to_london = ((paris[0] - london[0]) ** 2 + (paris[1] - london[1]) ** 2) ** .5


# distances = {}
#
# distances['Moscow'] = {'to_London': moscow_to_london, 'to_Paris': moscow_to_paris}



# distances = {'Moscow': {'to_London': moscow_to_london, 'to_Paris': moscow_to_paris},
#              'London': {'to_Moscow': london_to_moscow, 'to_Paris': london_to_paris},
#              'Paris': {'to_Moscow': paris_to_moscow, 'to_London': paris_to_london}}

# distances = dict(Moscow={'to_Paris': moscow_to_paris, 'to_London': moscow_to_london},
#                  London={'to_Moscow': london_to_moscow, 'to_Paris': london_to_paris},
#                  Paris={'to_Moscow': paris_to_moscow, 'to_London': paris_to_london})


print(distances)





