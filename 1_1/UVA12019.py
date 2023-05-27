weeks = ['Monday','Tuesday','Wednesday','Thursday', 'Friday','Saturday','Sunday']

months = [10,21,14,4,9,6,11,8,5,10,7,12]

n = int(input())
for i in range(n):
    st = input().split()
    m = int(st[0])
    d = int(st[1])
    dif = d - months[m-1]
    if -6 < dif <6:
        print(weeks[dif])
    else:
        dif = dif%7
        print(weeks[dif])