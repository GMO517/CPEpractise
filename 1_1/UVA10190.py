while True:
    try:
        st = input().split()
        n = int(st[0])
        m = int(st[1])
        if(m==1):
            print("Boring!")
        else:
            lst = []
            lst.append(n)
            while n>1:
                n = n//m
                lst.append(n)
            for i in range(len(lst)-1):
                if lst[i]%m != 0:
                    print("Boring!")
                    break
            else:
                lsts = [str(l) for l in lst]
                print(' '.join(lsts))
    except:
        break