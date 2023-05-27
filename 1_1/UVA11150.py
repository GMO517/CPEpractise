while True:
    try:
        cola = int(input())
        drink = cola
        empty = 1
        all  = cola + empty
        while all >=3:
            cola = all //3
            drink = drink + cola
            empty = all % 3
            all = cola + empty
        print(drink)
    except:
        break