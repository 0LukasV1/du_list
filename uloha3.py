def sucin(zoz):
    a = 1
    if len(zoz) >= 2:
        for b in range (0,len(zoz)):
            a*=zoz[b]
    else:
        print('1')
    return a
x=[6, 5, 8, 16, 7]
print(sucin(x))