n = int(input())
d = []
for i in range(n):
    nation = input().split(" ")
    if nation in d:
        d[nation] = d[nation] + 1
    else:
        d[nation] = 1

ns = sorted(d)
for s in ns:
    print(s, d[s])
