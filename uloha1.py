def vypis_typy(zoz):
    if type(zoz) == list:
        for a in range (0,len(zoz)):
            if type(zoz[a]) == str:
                print(zoz[a],'je retazec')
            elif type(zoz[a]) == int or zoz[a] ==float:
                 print(zoz[a], 'je cislo')
            else:
                print(zoz[a],'je iny typ')


vypis_typy([16,'h',7, 423,'sfafs'])


