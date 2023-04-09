while True:
    try:
        cp = []
        lst = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
               'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        a = list(input().lower())
        b = list(input().lower())
        for c in lst:
            c1 = a.count(c)
            c2 = b.count(c)
            cm = min(c1, c2)
            if cm != 0:
                cp.append(c*cm)
        # cp.sort()
        for c in cp:
            print(c, end="")
        print()
    except:
        break
