while True:
    try:
        x = int(input())
        lsta = [int(s) for s in input().split()]
        lsta.reverse()
        lstad = []
        for i in range(1,len(lsta)):
            a = lsta[i]*i
            lstad.append(a)
        fx =lstad[0]
        for i in range(1, len(lstad)):
            fx = fx +lstad[i]*x **i
        print(fx)
    except:
        break