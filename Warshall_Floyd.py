#---------------------------------------------------------------
#Warshall-Floyd
n, m = map(int,input().split())
a = [0] * m
b = [0] * m
c = [0] * m

for i in range(m):
    a[i], b[i], c[i] = map(int,input().split())
    a[i] -= 1
    b[i] -= 1

d = [[float('inf') for i in range(n)] for j in range(n)]

for i in range(n):
    d[i][i] = 0

for i in range(m):
    d[a[i]][b[i]] = c[i]
    d[b[i]][a[i]] = c[i]

for k in range(n):
    for i in range(n):
        for j in range(n):
            d[j][i] = min(d[j][i], d[k][i] + d[j][k])
