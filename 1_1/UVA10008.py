d = {}
n = int(input())
for i in range(n):
    s  =input().upper()
    for c in s:
        if 'A' <= c <= 'Z':
            if c in d:
                d[c] += 1
            else:
                d[c] =1
                
cs =sorted(set(d.values()),reverse=True)
for c in cs:
    l = [x for x, y in d.items() if y==c]
    l.sort()
    for x in l:
        print(x,c)