from sympy import Rational
from sympy.core.numbers import igcd
import math

def continued_fraction_expansion(n, e):
    # 계속된 분수 확장을 계산합니다.
    expansion = []
    while e != 0:
        expansion.append(n // e)
        n, e = e, n % e
    return expansion

def convergents(expansion):
    # 연속 분수 확장의 covergents를 계산합니다.
    convergents = []
    numerator = [0, 1]
    denominator = [1, 0]
    for i in expansion:
        numerator = [numerator[1], i * numerator[1] + numerator[0]]
        denominator = [denominator[1], i * denominator[1] + denominator[0]]
        convergents.append(Rational(numerator[1], denominator[1]))
    return convergents

def wiener_attack(n, e):
    # Wiener's attack을 실행합니다.
    for convergent in convergents(continued_fraction_expansion(e, n)):
        k = convergent.numerator
        d = convergent.denominator

        if k == 0:
            continue

        # phi 값을 계산합니다.
        phi = (e * d - 1) // k

        # 방정식의 해를 찾습니다.
        b = n - phi + 1
        delta = b * b - 4 * n
        if delta >= 0:
            x = (-b + math.isqrt(delta)) // 2
            if n == x * (n // x):
                return d
    return None

