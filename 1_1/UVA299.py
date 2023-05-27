tc = int(input())
for i in range(tc):
    n = int(input())
    train = [int(s) for s in input().split()]
    c = 0
    for j in range(len(train)):
        for k in range(j+1,len(train)):
            if(train[j]>train[k]):
                c+=1
    print("Optimal train swapping takes",c,"swaps.")