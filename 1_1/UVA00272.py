c = 0
while True:
    try:
        lsts = list(input())
        for i in range(len(lsts)):
            if(lsts[i]) == '"':
                c+=1
                if c %2==0:
                    print("''",end = '')
                else:
                    print("``",end = '')
            else:
                print(lsts[i],end ='')
        print()
    except:
        break