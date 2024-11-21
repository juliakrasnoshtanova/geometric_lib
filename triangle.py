from math import *
def area(a, b, c):
    '''Принимает числа a, b, c (стороны треугольника); находит площадь треугольника по формуле Герона'''
    assert a > 0
    assert b > 0
    assert c > 0
    assert a + b > c
    assert a + c > b
    assert b + c > a
    p = (a + b + c) / 2
    return sqrt(p * ((p - a) * (p - b) * (p - c)))


def perimeter(a, b, c):
    '''Принимает числа a, b, c (стороны треугольника); находит периметр треугольника'''
    assert a > 0
    assert b > 0
    assert c > 0
    assert a + b > c
    assert a + c > b
    assert b + c > a
    return a + b + c