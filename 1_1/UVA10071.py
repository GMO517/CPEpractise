while True:
    try:
        input_str = input()
        input_list = input_str.split()
        lst = []
        lst.append(2*int(input_list[0])*int(input_list[1]))
        print(lst[0])
    except EOFError:
        break
