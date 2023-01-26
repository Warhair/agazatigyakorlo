def korok():
    lista = []
    i = 0
    print("II/A, B, C:")
    while i < 5:
        kor = int(input("Adjon meg egy egész számot:"))
        lista.insert(i, kor)
        i += 1
    i = 0
    print("\t",end="")    
    while i < 5:   
        if i == 4:
            print(lista[i])
            i += 1
        else:
            print(lista[i], end=":")
            i += 1
    print("II/D, E:")
    elso_idos(lista)
    print("\t Első idős ember korának helye a listában: ",elso_idos(lista))
    kiiras(elso_idos(lista))


def elso_idos(lista):
    index = 0
    db = -1
    while index < len(lista) or db == -1:
        if lista[index] > 70:
            db == index
        index += 1
    return db

def kiiras(ev):
    f = open('oreg.txt', 'w')
    f.write("II/F:\n \t Első idős ember korának helye a listában:  {}\n".format(ev))
    f.close()

        
    