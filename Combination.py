#---------------------------------------------------------------
# Combination nCk

def nCk(n, k):
    ret = 1
    mo = 10**9 + 7
    for i in range(k):
        ret = ret * (n - i) * pow(i + 1, mo - 2, mo) % mo
    return ret

#---------------------------------------------------------------
#Combination_mod

mod = 1000000007

n = num
f = [0] * n
finv = [0] * n

f[0] = 1
finv[0] = finv[1] = 1
for i in range(1, n):
    f[i] = (f[i - 1] * i) % mod

finv[n - 1] = pow(f[n - 1], mod - 2, mod)
for i in range(n - 2, 1, -1):
    finv[i] = ((i + 1) * finv[i + 1]) % mod

def Combination_mod(n, k):
    ret = f[n]
    ret = (ret * finv[k]) % mod
    ret = (ret * finv[n - k]) % mod
    return ret
