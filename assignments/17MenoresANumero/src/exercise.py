def main(): 
    x = int(input(''))
    y = int(input(''))
    z = x*y
    lista=[]
    i=1
    while i<=z:
        i=i+1
        valor = int(input(''))
        if valor<10:
            lista.append(valor)
    print(lista)


if __name__=='__main__':
    main()