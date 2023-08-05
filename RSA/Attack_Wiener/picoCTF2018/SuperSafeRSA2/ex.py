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


c= 74656558022839055957486462819905995876187919411516725694171429102789712929327942602783390443413015793339709672458190916198217092854563013073826016059117106865706437459318250499145704904019507722273390686196228735285877381812173288926254273484207110105872784138331460508370948963482034330305034653674346440792
n= 148337238837980204604258481398486555479662772411127669544511411414637480091964615739652008000282038439580320179857917659146369849900257414100209029025277317009008322530433114360958279216638713900178224553226111248718730750329686617313196229443362042513004804865365680353556694701248340698570731626730407309679
e= 44107111604677056428020584204530379886662319696898620571797517039794933771031851731366993910333034515954372329293242617510494976349334211644884162360431185438204499339781140455266740769128912694626003486588778554609303393869982440909134987801843941738926751485241331998121883562658508426442151685340795506049

d = wiener_attack(n, e)
if d is not None:
    print("Private exponent found:", d)
    m = pow(c, d, n)
    
    msg = bytes.fromhex(hex(m)[2:])
    print(msg)
else:
    print("Attack failed.")

