n = int(input())
for i in range(n):
    st = input().split()
    s  = int(st[0])
    d = int(st[1])
    if(s<d):
        print('impossible')
    else:
        high = (s+d)//2
        low = (s-d)//2
        if (high+low) == s:
            print(high,low)
        else:
            print('impossible')