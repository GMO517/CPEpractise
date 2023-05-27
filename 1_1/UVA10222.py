d = {
    ']': 'p', '[': 'o', 'p': 'i', 'o': 'u', 'i': 'y', 'u': 't', 'y': 'r', 't': 'e', 'r': 'w', 'e': 'q',
    '\'': 'l', ';': 'k', 'l': 'j', 'k': 'h', 'j': 'g', 'h': 'f', 'g': 'd', 'f': 's', 'd': 'a',
    '.': 'm',  ',': 'n', 'm': 'b', 'n': 'v', 'b': 'c', 'v': 'x', 'c': 'z'
}

while True:
    try:
        st = input().lower()
        for c in st:
            if c in d:
                print(d[c], end='')
            else:
                print(' ', end="")
        print()
    except:
        break
