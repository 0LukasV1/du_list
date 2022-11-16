def nakup(zoz):
    if type(zoz)== list:
        cena = 0
        a = 0
        for b in range (0, len(zoz)):

            if b % 2 == 0:
                a=zoz[b]
            else:
                cena+= (a*zoz[b])

        print(cena)

nakup([8,5,19,3.2,0.1])