from math import sqrt
import sorting

def obtener_coordenadas(nombre_archivo):
    """
    parametros: nombre de un archivo que contiene puntos.
    pre: el archivo deben existir y no ser vacio.
    función: extrae los puntos del archivo y los guarda en una lista.
    retorna: la lista con los puntos.
    """

    cords = []
    with open(nombre_archivo, 'r', encoding="utf8") as archivo:
        archivo.seek(0)

        for linea in archivo:
            linea = linea.rstrip()
            linea = linea.replace(',', '.')
            cords.append(linea.split(' '))

    return cords

def preferencia(solicitante, requerido):
    """
    parametros: un punto solicitante y un punto requerido.
    pre: los puntos deben tener dos coordenadas decimales.
    función: calcula la distancia entre los dos puntos.
    retorna: devuelve la distancia entre los dos puntos.
    """

    puntaje_x = float(solicitante[0]) - float(requerido[0])
    puntaje_y = float(solicitante[1]) - float(requerido[1])

    modulo = sqrt((puntaje_x ** 2) + (puntaje_y ** 2))

    return modulo


def dominado(solicitante, requerido):
    """
    parametros: un punto solicitante y un punto requerido.
    pre: los puntos deben tener dos coordenadas decimales.
    función: se fija si el punto solicitante es mayor en ambas coordenadas que el requerido.
    retorna: devuelve True o False dependiento del resultado.
    """

    domina_x = False
    domina_y = False

    if float(solicitante[0]) >= float(requerido[0]):
        domina_x = True

    if float(solicitante[1]) >= float(requerido[1]):
        domina_y = True

    return bool(domina_x and domina_y)

def imprimir(match, nombre_archivo_1, nombre_archivo_2):
    """
    parametros: un match de puntos, los nombres de las listas.
    pre: el match de puntos no debe ser vacío.
    función: imprime en consola el match.
    retorna: -
    """

    print("Tamaño del matching: ", len(match))
    print("\n")
    print("(", nombre_archivo_1.rstrip(".txt"), " → ", nombre_archivo_2.rstrip(".txt"),")")
    for pareja in match:
        print(pareja[0], " → ", pareja[1])

def merge_sort(element_x, set_y):
    """
    parametros: una lista de puntos a ordenar por cercania a otro punto.
    pre: el match de puntos no debe ser vacío.
    función: imprime en consola el match.
    retorna: -
    """
    set_rta = set_y

    if len(set_y) > 1:

        rta_izq = []
        rta_der = []

        mid = len(set_y)//2

        set_izq = set_y[:mid]
        set_der = set_y[mid:]

        rta_izq = merge_sort(element_x, set_izq)
        rta_der = merge_sort(element_x, set_der)

        if preferencia(element_x, rta_der[0]) > preferencia(element_x, rta_izq[0]):
            set_rta.extend(rta_izq)
            set_rta.extend(rta_der)
        else:
            set_rta.extend(rta_der)
            set_rta.extend(rta_izq)

    return set_rta
      

def max_matching(numero_de_puntos, nombre_archivo_1, nombre_archivo_2):
    """
    parametros: una lista de puntos solicitantes y una de puntos requeridos.
    pre: las listas tienen que tener la misma cantidad de puntos.
    función: crea un match perfecto entre solicitantes y requeridos según las condiciónes.
    retorna: devuelve el match resultante.
    """

    match = []
    set_a = obtener_coordenadas(nombre_archivo_1)
    set_b = obtener_coordenadas(nombre_archivo_2)

    for element_a in set_a:
        indice = -1
        better = 0
        merge_sort(element_a, set_b)
        for element_b in set_b:
            if dominado(element_a, element_b) and (element_b not in match):
                if preferencia(element_a, element_b) > better:
                    indice = set_b.index(element_b)
                    better = preferencia(element_a, element_b)
        if indice != -1:
            match.append([element_a, set_b[indice]])

    imprimir(match, nombre_archivo_1, nombre_archivo_2)

def main():
    """
    función principal
    """
    numero_de_puntos = 4
    nombre_archivo_1 = "A.txt"
    nombre_archivo_2 = "B.txt"

    max_matching(numero_de_puntos, nombre_archivo_1, nombre_archivo_2)

main()
