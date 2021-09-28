def main(): 
    #escribe tu código abajo de esta línea
    numero = int(input())
    Lista1=[]
    Lista2=[]
    
    if numero>0:
        for c in range (numero):
            i=input()
            Lista1.append(i)
            if (i in Lista2)==False:
                Lista2.append(i)
        print(Lista1)
        print(Lista2)
    else:
        print('Error')

if __name__=='__main__':
    main()
