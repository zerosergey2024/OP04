#Написать функцию square, принимающую 1 аргумент — сторону квадрата,
# и возвращающую 3 значения (с помощью [кортежа]
# (https://pythonworld.ru/tipy-dannyx-v-python/kortezhi-tuple.html),
# после return перечислить все значения через запятую):
# периметр квадрата, площадь квадрата и диагональ квадрата.

def square(a):
    p = a * 4
    s = a * a
    d = (a * 2) ** 0.5
    return p, s, d

a = int(input())
p, s, d = square(a)
print(p, s, d)
