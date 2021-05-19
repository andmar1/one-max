import numpy as np
import matplotlib.pyplot as plt
import random as rnd


def funcion_OneMax(dim,numero,contar,iterar):
    vp="VP"
    VectorDeProbabilidad=[]
    size=[]
    grafica=[n for n in range(iterar)]
    for _ in range(dim):       
        #VectorDeProbabilidad=np.array(dim,0.5)
        VectorDeProbabilidad.append(0.5)
    listas=np.array(VectorDeProbabilidad)
    print(f'{vp}----{listas}----{vp}')
    for _ in range(iterar):
        nueva=[]
        for _ in range(numero):
            vectorsuma=0
            RandomList=[rnd.random() for x in range(dim)]
            #print(RandomList)
            lista=[1 if a < b else 0 for a,b in zip(RandomList,VectorDeProbabilidad)]
            listafinal=np.array(lista)
            sumarunos=sum(lista)
            contador=dim-sumarunos       
            lista[0]=contador
            nueva.append(lista)
         #for ordenamiento in range(1,len(nueva)):
        #    for posicion in range(len(listafinal)-ordenamiento):
        #       if listafinal[posicion] > listafinal[posicion + 1]:
        #            tmp=listafinal[posicion]
        #            listafinal[posicion]=listafinal[posicion + 1]
        #            listafinal[posicion + 1]= tmp
        #print("ordenado: ",listafinal)    
        ordenamiento=sorted(nueva)
        NPordenamiento=np.array(ordenamiento)
        print("-"*50)
        print(NPordenamiento)
        size.append(NPordenamiento[-1][0]) #Order


        for i in range(contar):
            NP=np.array(ordenamiento[i])
            vectorsuma+=NP/contar
            Nsum=np.array(vectorsuma/contar)
        print(vectorsuma)
        VectorDeProbabilidad=vectorsuma  

    eje_X = grafica
    eje_Y = size


    plt.title("One_Max")
    plt.scatter(eje_X, eje_Y, label="Puntos",color="#3be723")
    plt.plot([-50,50],[0,0], color="black",label="eje X")
    plt.plot([0,0],[-50,50], color="black",label="eje Y")
    plt.legend(loc="upper left")
    plt.show()  

if __name__=="__main__":
    dimension = int (input("Ingresa la dimension: "))
    print(30*"-")
    Nlista= int(input("Ingresa el numero de listas: "))
    print(30*"-")
    evaluar = int(input("Ingrese el numero de elementos a evaluar: "))
    print(30*"-")
    iteraciones = int(input("Ingresa las iteraciones: "))

    funcion_OneMax(dimension,Nlista,evaluar,iteraciones)