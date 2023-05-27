
def n31(n):
    if n == 1:
        return 1
    elif n % 2 == 1:
        return 1+n31(3*n+1)
    else:
        return 1+n31(n//2)


while True:
    try:
        lst = input().split()
        i = int(lst[0])
        j = int(lst[1])
        maximumCycleLength = 0

        for n in range(min(i, j), max(i, j+1)):
          # 要記得判定i跟j誰大誰小
            maximumCycleLength = max(maximumCycleLength, n31(n))
        print(i, j, maximumCycleLength)
    except:
        break
