while True:
    datas = input().split()
    if datas[0] == '0' and datas[1] == '0':
        break
    a = int(datas[0])
    b = int(datas[1])
    carry =0
    cc = 0
    while a>0 or b>0:
        a0 = a%10
        b0 = b%10
        carry = (a0 +b0 +carry)//10
        if carry>0:
            cc += 1
        a = a//10
        b = b//10
    if cc ==0:
        print('No carry operation.')
    elif cc ==1:
        print('1 carry operation.')
    else:
        print(f'{cc} carry operations.')