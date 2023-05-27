sts = []
while True:
    try:
        s= input()
        sts.append(s)
    except:
        break
l = len(sts)
m  = [len(x) for x in sts]
max_  = max(m)
sts.reverse()
for i in range(max_):
    for x in range(len(sts)):
        if len(sts[x])>i:
            print(sts[x][i], end = '')
        elif x < len(sts) -1:
            print(' ', end = '')
    print()