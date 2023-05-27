while True:
    try:
        st = input().split()
        S = int(st[0])
        D = int(st[1])
        sum_ =  S
        while sum_ < D:
            S+=1
            sum_+=S
        print(S)
    except:
        break