while True:
    st = input().split()
    a = int(st[0])
    b = int(st[1])
    if a== 0 and b==0:
        break
    c = 0
    for i in range(a,b+1):
        if i**0.5%1==0:
            c+=1
    print(c)