import fuckit as fuckit
import pandas as pd
import random
import time
from matplotlib import pyplot as plt
import csv

arreglo = [random.randint(1,100) for i in range (20)]
datos = []

with open('dataPUJ-marzo.csv', encoding='utf-8', mode='r') as archivo_csv:
    lector_csv = csv.DictReader(archivo_csv)
    registros = list(lector_csv)

def ordernar_likes(lst):
    """Aqui se aplica el metodo de organizar por medio de insercion"""
    for i in range(1, len(lst)):
        j = i
        while j > 0 and lst[j - 1]['number_of_likes'] > lst[j]['number_of_likes']:
            lst[j - 1], lst[j] = lst[j], lst[j - 1]
            j -= 1
    """Se crea una nueva variable la cual va a organizar por la funcion sorted el arreglo
    de datos y lo que hace la funcion lambda es que retorna el numero de likes de cada tweet, 
    y en la siguiente linea se seleccionan los 3 primeros y se imprime el texto de cada tweet"""
    top_3_tweets = sorted(lst, key=lambda tweet: tweet['number_of_likes'], reverse=True)[:3]
    top_3_tweet_texts = [tweet['text']for tweet in top_3_tweets]
    print(top_3_tweet_texts)


def busqueda_binaria_nombre(twitter_name):
    left = 0
    right = len(registros) - 1

    while left <= right:
        mid = (left + right) // 2
        if registros[mid]['twitter_name'] == twitter_name:
            return mid
        elif registros[mid]['twitter_name'] < twitter_name:
            left = mid + 1
        else:
            right = mid - 1
    return None

def busqueda_numero_binaria(arreglo, num):
    low = 0
    high = len(arreglo) - 1
    while low <= high:
        mid = (low + high) // 2
        if arreglo[mid] == num:
            return mid
        elif arreglo[mid] < num:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def busqueda_numero_lineal(arreglo, num):
    for i in range(len(arreglo)):
        if arreglo[i] == num:
            return i
    return -1

def metodoBurbuja(arreglo):
    n = len(arreglo)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arreglo[j] > arreglo[j + 1]:
                arreglo[j], arreglo[j + 1] = arreglo[j + 1], arreglo[j]
    return arreglo

def metodoSort(arreglo):
    n = len(arreglo)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arreglo[j] < arreglo[min_idx]:
                min_idx = j
        arreglo[i], arreglo[min_idx] = arreglo[min_idx], arreglo[i]
    return arreglo

def metodoInsercion(arreglo):
    n = len(arreglo)
    for i in range(1, n):
        key = arreglo[i]
        j = i - 1
        while j >= 0 and key < arreglo[j]:
            arreglo[j + 1] = arreglo[j]
            j -= 1
        arreglo[j + 1] = key
    return arreglo

def mostrar_registro(texto):
    print([registros[texto]['text']])

def main():
    #------------------------
    #        PRIMER PUNTO
    #------------------------
    print (arreglo)
    print("------------------------------------------------------------------------------------------------------")
    print(registros)
    print("------------------------------------------------------------------------------------------------------")

    df = pd.DataFrame(columns=['n', 'numero_b', 'nombre_l'])
    dx = pd.DataFrame(columns=['n',  'burbuja', 'sort', 'insercion'])
    n = []
    numero_b = []
    numero_l = []
    burbuja = []
    sort = []
    insercion = []
    seguir = True
    tiempos = []
    tamano2 = 10000

    while seguir == True:

        print("-----------------------------")
        print(" -- Primer Punto --")
        print("-----------------------------")
        print("1. Buscar de forma binaria")
        print("2. Buscar de forma lineal")
        print("3. Metodo burbuja")
        print("4. Metodo sort")
        print("5. Metodo insercion")
        print("6. Mostrar grafica Algoritmos de busqueda")
        print("7. Mostrar grafica Algoritmos de ordanimento")
        print("-----------------------------")
        print(" -- Segundo Punto --")
        print("-----------------------------")
        print("8. Buscar de forma binaria el nombre")
        print("9. Ordenar por los likes")
        print("10. Salir")
        opcion= input()

        if opcion == "1":
            print("Ingrese el numero que quiere buscar")
            num = int(input())
            for i in range (5):
                t0 = time.perf_counter()
                print(busqueda_numero_binaria(arreglo, num))
                t1 = time.perf_counter()
                tiempos.append(t1-t0)
                numero_b.append(t1 - t0)
                n.append(tamano2)
                tamano2 *= 5

        if opcion == "2":
            print("Ingrese el nombre que quiere buscar")
            num = input()
            for i in range (5):
                t2 = time.perf_counter()
                print(busqueda_numero_lineal(arreglo, num))
                t3 = time.perf_counter()
                tiempos.append(t3 - t2)
                numero_l.append(t3 - t2)

        if opcion == "3":
            for i in range (5):
                t2 = time.perf_counter()
                print(metodoBurbuja(arreglo))
                t3 = time.perf_counter()
                tiempos.append(t3 - t2)
                burbuja.append(t3 - t2)
                n.append(tamano2)
                tamano2 *= 5

        if opcion == "4":
            for i in range (5):
                t2 = time.perf_counter()
                print(metodoSort(arreglo))
                t3 = time.perf_counter()
                tiempos.append(t3 - t2)
                sort.append(t3 - t2)

        if opcion == "5":
            for i in range (5):
                t2 = time.perf_counter()
                print(metodoInsercion(arreglo))
                t3 = time.perf_counter()
                tiempos.append(t3 - t2)
                insercion.append(t3 - t2)

        if opcion =="6":
            print("Tiempos de busqueda")
            print("Busqueda binaria:", tiempos[0])
            print("Busqueda lineal:", tiempos[1])
            print()

            df['n'] = n
            df['numero_b'] = numero_b
            df['nombre_l'] = numero_l

            print(df)
            df.plot(x='n', y=['numero_b', 'nombre_l'])
            plt.grid()
            plt.show()

        if opcion =="7":
            print("Tiempos de busqueda")
            print("Ordenamiento Burbuja:", tiempos[0])
            print("Ordenamiento Sort:", tiempos[1])
            print("Ordenamiento Insercion:", tiempos[2])
            print()

            dx['n'] = n
            dx['burbuja'] = burbuja
            dx['sort'] = sort
            dx['insercion'] = insercion

            print(dx)
            dx.plot(x='n', y=['burbuja', 'sort', 'insercion'])
            plt.grid()
            plt.show()

        if opcion == "8":
            print("Ingrese el nombre que quiere buscar")
            nom = input()
            texto = busqueda_binaria_nombre(nom)
            if texto is not None:
                #print(f" {texto}")
                mostrar_registro(texto)
            else:
                print(f"{nom} was not found in the list of tweets.")

        if opcion == "9":
            ordernar_likes(registros)

        if opcion == "10":
            break

if __name__ == "__main__":
    main()


