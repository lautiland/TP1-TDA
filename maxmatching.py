from math import sqrt

def obtener_coordenadas(nombre_archivo):    # O(n)
    """
    parametros: nombre de un archivo que contiene puntos.
    pre: el archivo deben existir y no ser vacio.
    función: extrae los puntos del archivo y los guarda en una lista.
    retorna: la lista con los puntos.
    """

    cords = []
    with open(nombre_archivo, 'r', encoding="utf8") as archivo: 
        archivo.seek(0) # O(1)

        for linea in archivo:   # O(n)
            linea = linea.rstrip()  # O(1)
            linea = linea.replace(',', '.') # O(1)
            cords.append(linea.split(' '))  # O(1)

    return cords

def preferencia(solicitante, requerido):    # O(1)
    """
    parametros: un punto solicitante y un punto requerido válido.
    pre: los puntos deben tener dos coordenadas decimales.
    función: calcula la distancia entre los dos puntos.
    retorna: devuelve la distancia entre los dos puntos.
    """
    if dominado(solicitante, requerido):    # O(1)
        puntaje_x = float(solicitante[0]) - float(requerido[0]) # O(1)
        puntaje_y = float(solicitante[1]) - float(requerido[1]) # O(1)

        modulo = sqrt((puntaje_x ** 2) + (puntaje_y ** 2))  # O(1)
    else:
        modulo = 0  # O(1)
    return modulo   # O(1)


def dominado(solicitante, requerido):   # O(1)
    """
    parametros: un punto solicitante y un punto requerido.
    pre: los puntos deben tener dos coordenadas decimales.
    función: se fija si el punto solicitante es mayor en ambas coordenadas que el requerido.
    retorna: devuelve True o False dependiento del resultado.
    """

    domina_x = False    # O(1)
    domina_y = False    # O(1)

    if float(solicitante[0]) >= float(requerido[0]):    # O(1)
        domina_x = True     # O(1)

    if float(solicitante[1]) >= float(requerido[1]):    # O(1)
        domina_y = True     # O(1)

    return bool(domina_x and domina_y)  # O(1)

def imprimir(match, nombre_archivo_1, nombre_archivo_2):    # O(n)
    """
    parametros: un match de puntos, los nombres de las listas.
    pre: el match de puntos no debe ser vacío.
    función: imprime en consola el match.
    retorna: -
    """

    print("Tamaño del matching: ", len(match))      # O(1)
    print("\n")    # O(1)
    print("(", nombre_archivo_1.rstrip(".txt"), " → ", nombre_archivo_2.rstrip(".txt"),")") # O(1)
    for pareja in match:    # O(n)
        print(pareja[0], " → ", pareja[1])  # O(1)

def merge_sort(element_x, set_y):   # O(n log n)
    """
    parametros: una lista de puntos a ordenar por cercania a otro punto.
    pre: el match de puntos no debe ser vacío.
    función: imprime en consola el match.
    retorna: la lista ordenada.
    """
    set_rta = set_y   # O(1)

    if len(set_y) > 1:  # O(1)

        rta_izq = []    # O(1)
        rta_der = []    # O(1)

        mid = len(set_y)//2   # O(1)

        set_izq = set_y[:mid]   # O(1)
        set_der = set_y[mid:]   # O(1)

        rta_izq = merge_sort(element_x, set_izq)    # O(n log n)
        rta_der = merge_sort(element_x, set_der)    # O(n log n)

        if preferencia(element_x, rta_izq[0]) < preferencia(element_x, rta_der[0]): # O(1)
            set_rta = rta_izq + rta_der   # O(1)

    return set_rta  # O(1)

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

def comprobar_listas(set_a, set_b): # O(1)
    """
    parametros: dos listas de puntos.
    pre: las listas deben existir.
    función: comprueba si alguna de las listas esta vacía.
    retorna: True o False dependiendo del resultado.
    """
    respuesta = False   # O(1)

    if not set_a or not set_b:  # O(1)
        respuesta = True    # O(1)
    if len(set_a) != len(set_b):    # O(1)
        respuesta = True    # O(1)

    return respuesta

def verificar(match):   # O(n)
    """
    parametros: un match de puntos.
    pre: el match debe existir.
    función: comprueba si el match es perfecto.
    retorna: True o False dependiendo del resultado.
    """
    respuesta = True    # O(1)
    for pareja in match:    # O(n)
        if not dominado(pareja[0], pareja[1]):  # O(1)
            respuesta = False   # O(1)

    if respuesta:   # O(1)
        print("EL match es perfecto")   # O(1)
    else:
        print("Error")  # O(1)


def max_matching(numero_de_puntos, nombre_archivo_1, nombre_archivo_2): # O(n^2 log n)
    """
    parametros: una lista de puntos solicitantes y una de puntos requeridos.
    pre: las listas tienen que tener la misma cantidad de puntos.
    función: crea un match perfecto entre solicitantes y requeridos según las condiciónes.
    retorna: devuelve el match resultante.
    n: cantidad de puntos en las listas.
    """

    match = []  # O(1)

    set_a = obtener_coordenadas(nombre_archivo_1)   # O(n)
    set_b = obtener_coordenadas(nombre_archivo_2)   # O(n)

    if comprobar_listas(set_a, set_b):             # O(1)
        print("Las listas no tienen la misma cantidad de puntos o estan vacías")    # O(1)
    else:

        for element_a in set_a: # O(n)

            indice = -1     # O(1)
            better = 0      # O(1)

            set_b = merge_sort(element_a, set_b)    # O(n log n)

            for element_b in set_b: # O(n)
                if dominado(element_a, element_b) and not esta_en(element_b, match):    # O(1)   
                    if better == 0 or preferencia(element_a, element_b) < better:      # O(1)
                        indice = set_b.index(element_b)                               # O(1)
                        better = preferencia(element_a, element_b)                    # O(1)
            if indice != -1:    # O(1)
                match.append([element_a, set_b[indice]])    # O(1)

        #imprimir(match, nombre_archivo_1, nombre_archivo_2)
        verificar(match)

def main():
    """
    función principal, solo ejecuta max_matching con parámetros
    """
    numero_de_puntos = 3

    for i in range(1, 15):
        nombre_archivo_1 = "ejemplos/A" + str(i) + ".txt"
        nombre_archivo_2 = "ejemplos/B" + str(i) + ".txt"
        numero_de_puntos = len(obtener_coordenadas(nombre_archivo_1))
        max_matching(numero_de_puntos, nombre_archivo_1, nombre_archivo_2)

main()
