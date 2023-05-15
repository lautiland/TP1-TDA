from math import sqrt

def preguntar_nombres():
    """
    parametros: -
    pre: los archivos deben existir y no ser vacios.
    función: pregunta los nombres de los archivos.
    retorna: los nombres de los archivos.
    """
    nombres = []
    nombres.append(input("Cuál es el nombre del primer archivo? "))
    nombres.append(input("Cuál es el nombre del segundo archivo? "))
    return nombres

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
            cords.append(linea.split(' '))

    return cords

def preferencia(solicitante, requerido):
    """
    parametros: un punto solicitante y un punto requerido.
    pre: los puntos deben tener dos coordenadas decimales.
    función: calcula la distancia entre los dos puntos.
    retorna: devuelve la distancia entre los dos puntos.
    """

    puntaje_x = float(solicitante[0].replace(',', '.')) - float(requerido[0].replace(',', '.'))
    puntaje_y = float(solicitante[1].replace(',', '.')) - float(requerido[1].replace(',', '.'))

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

    if float(solicitante[0].replace(',', '.')) >= float(requerido[0].replace(',', '.')):
        domina_x = True

    if float(solicitante[1].replace(',', '.')) >= float(requerido[1].replace(',', '.')):
        domina_y = True

    if domina_x and domina_y:
        return True
    else:
        return False


def gale_shapley(solicitantes, requeridos):
    """
    parametros: una lista de puntos solicitantes y una de puntos requeridos.
    pre: las listas tienen que tener la misma cantidad de puntos.
    función: crea un match perfecto entre solicitantes y requeridos según las condiciónes.
    retorna: devuelve el match resultante.
    """

    match = []
    soli_sin_pareja = solicitantes.copy()

    while soli_sin_pareja:
        solicitante = soli_sin_pareja.pop(0)
        req_sin_pedir = requeridos.copy()
        pareja_encontrada = False

        while req_sin_pedir and not pareja_encontrada:
            requerido = req_sin_pedir.pop(0)

            if dominado(solicitante, requerido):
                indice = -1

                for pareja in match:
                    if requerido in pareja:
                        indice = match.index(pareja)
                        break

                if indice == -1:
                    match.append([solicitante, requerido])
                    pareja_encontrada = True

                else:
                    preferencia_futura = preferencia(match[indice][0], match[indice][1])
                    preferencia_actual = preferencia(solicitante, requerido)
                    if preferencia_futura < preferencia_actual:
                        soli_sin_pareja.insert(0, match[indice][0])
                        match.remove(match[indice])
                        match.append([solicitante, requerido])
                        pareja_encontrada = True

    return match

def imprimir(match, nombres_archivos):
    """
    parametros: un match de puntos, los nombres de las listas.
    pre: el match de puntos no debe ser vacío.
    función: imprime en consola el match.
    retorna: -
    """

    nombre_solicitantes = nombres_archivos.rstrip(".txt")
    nombre_requeridos = nombres_archivos.rstrip(".txt")

    print("Tamaño del matching: ", len(match))
    print("\n")
    print("(", nombre_solicitantes, " → ", nombre_requeridos,")")
    for pareja in match:
        print(pareja[0], " → ", pareja[1])

def main():
    """
    función principal
    """

    nombres_archivos = []

    #cant_puntos = preguntar_puntos()
    nombres_archivos = preguntar_nombres()

    cords_a = obtener_coordenadas(nombres_archivos[0])
    cords_b = obtener_coordenadas(nombres_archivos[1])

    match = gale_shapley(cords_a, cords_b)

    imprimir(match, nombres_archivos)

main()
