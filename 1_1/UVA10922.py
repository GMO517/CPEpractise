while True :
    n = int(input())
    if n==0:
        break
    c =0
    m = n
    while m%9 == 0 and m != 9:
        c += 1
        st =str(m)
        dig = [int(x) for x in st]
        m = sum(dig)
    if n==9:
        print(f'{n} is a multiple of 9 and has 9-degree 1.' )
    elif c==0:
        print(n,'is not a multiple of 9.')
    else:
        print(f'{n} is a multiple of 9 and has 9-degree {c}.')