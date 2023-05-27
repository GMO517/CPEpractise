n = int(input())
for i in range(n):
    datas = [int (x) for x in input().split()]
    n = datas[0]
    del datas[0]
    datas.sort
    vito = datas[n//2]
    dist = [abs(vito-x) for x in datas]
    print(sum(dist))