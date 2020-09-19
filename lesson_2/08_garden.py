#!/usr/bin/env python
# -*- coding: utf-8 -*-

# в саду сорвали цветы
garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза', )

# на лугу сорвали цветы
meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка', )

# создайте множество цветов, произрастающих в саду и на лугу
garden_set = set(garden)
meadow_set = set(meadow)


# выведите на консоль все виды цветов
flowers = garden_set | meadow_set
#flowers = garden_set.union(meadow_set)
print(flowers)

# выведите на консоль те, которые растут и там и там
#a = garden_set & meadow_set
a = garden_set.intersection(meadow_set)
print(a)

# выведите на консоль те, которые растут в саду, но не растут на лугу
#b = garden_set - meadow_set
b = garden_set.difference(meadow_set)
print(b)

# выведите на консоль те, которые растут на лугу, но не растут в саду
#c = meadow_set - garden_set
c = meadow_set.difference(garden_set)
print(c)


