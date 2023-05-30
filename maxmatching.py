import sys

def obtener_coordenadas(nombre_archivo):    # O(n)
    """
    parametros: nombre de un archivo que contiene puntos.
    pre: el archivo deben existir y no ser vacio.
    función: extrae los puntos del archivo y los guarda en una lista.
    retorna: la lista con los puntos.
    """
    cords =[]    # O(1)

    try:
        with open(nombre_archivo, 'r', encoding="utf8") as archivo:
            cords = [linea.rstrip().replace(',', '.').split() for linea in archivo] # O(n)
        if cords == []:
            print("Error: el archivo con el nombre ", nombre_archivo,
                  " esta vacío.")
        return cords    # O(1)

    except FileNotFoundError:
        print("Error: el archivo con el nombre ", nombre_archivo
              , " no existe.")    # O(1)
        return cords    # O(1)

def comprobar_listas(set_a, set_b): # O(1)
    """
    parametros: dos listas de puntos.
    pre: las listas deben existir.
    función: comprueba si alguna de las listas esta vacía.
    retorna: True o False dependiendo del resultado.
    """

    if set_a is None or set_b is None:  # O(1)
        print("Error: alguna de las listas de puntos es Nula.")    # O(1)
        return False    # O(1)
    else:
        respuesta1 = False   # O(1)
        respuesta2 = False   # O(1)

        if len(set_a) != 0:  # O(1)
            respuesta1 = True    # O(1)
        if len(set_a) == len(set_b):    # O(1)
            respuesta2 = True    # O(1)

        return respuesta1 and respuesta2   # O(1)

def diferencia_coordenada(dominante, dominado, cord):    # O(1)
    """
    parametros: un punto dominante, un punto dominado y una coordenada.
    pre: los puntos deben tener dos coordenadas decimales.
    función: se fija si el punto dominante es mayor en la coordenada que el dominado.
    retorna: devuelve la diferencia entre las coordenadas.
    """
    if isinstance(dominante, list) is False or isinstance(dominado, list) is False: # O(1)
        print("Error: alguno de los puntos no es una lista.") # O(1)
        return 0    # O(1)
    elif len(dominante) != 2 or len(dominado) != 2: # O(1)
        print("Error: alguno de los puntos no tiene dos coordenadas.") # O(1)
        return 0    # O(1)
    else:

        respuesta = 0   # O(1)

        if cord == 'y': # O(1)
            respuesta = float(dominante[1]) - float(dominado[1]) # O(1)
        else:
            respuesta = float(dominante[0]) - float(dominado[0])  # O(1)

        return respuesta    # O(1)


def es_dominado(dominante, dominado):   # O(1)
    """
    parametros: un punto dominante y un punto dominado.
    pre: los puntos deben tener dos coordenadas decimales.
    función: se fija si el punto dominante es mayor en ambas coordenadas que el dominado.
    retorna: devuelve True o False dependiento del resultado.
    """

    domina_x = False    # O(1)
    domina_y = False    # O(1)

    if float(dominante[0]) >= float(dominado[0]):    # O(1)
        domina_x = True     # O(1)

    if float(dominante[1]) >= float(dominado[1]):    # O(1)
        domina_y = True     # O(1)

    return domina_x and domina_y  # O(1)


def esta_en(a_buscar, lista):   # O(n)
    """
    pre: la lista debe existir y no ser vacía.
    función: comprueba si un elemento esta en la lista.
    retorna: True o False dependiendo del resultado.
    """
    respuesta = False   # O(1)
    for elemento in lista:  # O(n)
        if elemento[1] == a_buscar: # O(1)
            respuesta = True    # O(1)

    return respuesta    # O(1)

def imprimir(match, nombre_archivo_1, nombre_archivo_2):    # O(n)
    """
    parametros: un match de puntos, los nombres de las listas.
    pre: el match de puntos no debe ser vacío.
    función: imprime en consola el match con el formato deseado.
    retorna: -
    """
    if match:   # O(1)
        print("Tamaño del matching: ", len(match))      # O(1)
        print("Matching: ")       # O(1)
        print("(", nombre_archivo_1, " → ", nombre_archivo_2,")") # O(1)
        for pareja in match:    # O(n)
            print(pareja[0], " → ", pareja[1])  # O(1)
    else:
        print("Error: el match que se intenta imprimir es Nulo")    # O(1)

def max_matching(nombre_archivo_1, nombre_archivo_2):   # O(n^2)
    """
    parametros: la cantidad de puntos en las listas y los nombres de las listas.
    pre: las listas tienen que existir y tener la misma cantidad de puntos.
    función: crea un match perfecto entre dominantes y dominados.
    retorna: devuelve el match resultante.
    n: cantidad de puntos en las listas.
    """

    match = []  # O(1)

    set_a = obtener_coordenadas(nombre_archivo_1)   # O(n)
    set_b = obtener_coordenadas(nombre_archivo_2)   # O(n)

    if not comprobar_listas(set_a, set_b):             # O(1)
        print("Error: las listas de puntos obtenidas de los nombres de archivos no",
               " tienen la misma cantidad de puntos o estan vacías.")    # O(1)
    else:

        set_a.sort(key=lambda x: x[1], reverse=True) # O(n log n)
        set_b.sort(key=lambda x: x[0]) # O(n log n)


        for element_a in set_a: # O(n)

            indice = -1     # O(1)
            better = 0      # O(1)

            while indice == -1 and len(set_b) != 0:  # O(n)

                for element_b in set_b: # O(n)
                    if es_dominado(element_a, element_b) and not esta_en(element_b, match):    # O(1)
                        cant_dominado = diferencia_coordenada(element_a, element_b, 'y')  # O(1)
                        if indice == -1 or cant_dominado < better:  # O(1)
                            indice = set_b.index(element_b) # O(1)
                            better = cant_dominado  # O(1)
                    set_b.remove(element_b) # O(1)

            if indice != -1:    # O(1)
                match.append([element_a, set_b[indice]])    # O(1)

        imprimir(match, nombre_archivo_1, nombre_archivo_2)    # O(n)

def main():
    """
    función principal, solo ejecuta max_matching con parámetros recibidos por consola.
    """

    nombre_archivo_1 = sys.argv[2]  # O(1)
    nombre_archivo_2 = sys.argv[3]  # O(1)

    max_matching(nombre_archivo_1, nombre_archivo_2)    # O(n^2)

main()
