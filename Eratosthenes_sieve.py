#---------------------------------------------------------------
# エラトステネスの篩
def Eratosthenes_sieve(n):
    prime = []
    table = [True] * n

    for i in range(2, n):
        if not table[i]:
            continue
        k = i + i
        while k < n:
            table[k] = False
            k += i

        prime.append(i)
