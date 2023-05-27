n = int(input())
for i in range(n):
    a  = int(input())
    b  = int(input())
    data  = [ x for x in range(a, b+1) if x%2 == 1]
    print(f'Case {i+1}:{sum(data)}')