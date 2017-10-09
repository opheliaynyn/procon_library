#---------------------------------------------------------------
#最小公倍数, 最大公約数
import math
math.gcd(a, b)

def lcm(a, b):
    return a * b // math.gcd(a, b)
