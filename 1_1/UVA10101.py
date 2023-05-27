name = ['shata', 'hajar' , 'lakh', 'kuti', 'shata', 'hajar','lakh', 'kuti']
div = [100,10,100,100,100,10,100,100,1000]
ts = 0
while True:
    try:
        ts += 1
        nums = []
        num = int(input())
        c=0
        while num > 0:
            nums.append(num%div[c])
            num = num //div[c]
            c+=1
        if len(nums) ==0:
            print(f'{ts:4}. {0}')
        else:
            nums.reverse()
            print(f'{ts:4}.',end='')
            l = len(nums)
            for i in range(0, l):
                if nums[i] != 0:
                    if i==l-1:
                        print(f' {nums[i]}',end = '')
                    else:
                        print(f' {nums[i]} {name[l-i-2]}',end = '')
                elif nums[i] ==0 and nums[i-1] != 0 and l-i-2==3:
                    print(f' {name[l-i-2]}',end = '')
            print()
    except:
        break