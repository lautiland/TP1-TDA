from math import sqrt

def obtener_coordenadas(nombre_archivo):

    with open(nombre_archivo, 'r') as archivo:
        archivo.seek(0)
        cords = []

        for linea in archivo:
            linea = linea.rstrip()
            cords.append(linea.split(' '))

    return cords

def preferencia(solicitante, requerido):

    puntajeX = float(solicitante[0].replace(',', '.')) - float(requerido[0].replace(',', '.'))
    puntajeY = float(solicitante[1].replace(',', '.')) - float(requerido[1].replace(',', '.'))

    modulo = sqrt((puntajeX ** 2) + (puntajeY ** 2))

    return modulo


def dominado(solicitante, requerido):
    dominaX = False
    dominaY = False
    if (float(solicitante[0].replace(',', '.')) >= float(requerido[0].replace(',', '.'))):
        dominaX = True

    if (float(solicitante[1].replace(',', '.')) >= float(requerido[1].replace(',', '.'))):
        dominaY = True

    if dominaX and dominaY:
        return True
    else:
        return False

    

def gale_shapley(solicitantes, requeridos):

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
                    if preferencia(match[indice][0], match[indice][1]) >= preferencia(solicitante, requerido):
                            soli_sin_pareja.insert(0, match[indice][0])
                            match.remove(match[indice])
                            match.append([solicitante, requerido])
                            pareja_encontrada = True
            
    return match

def imprimir(match):
    print("TamaÃ±o del matching: ", len(match))
    print("\n")
    print("(A â†’ B)")
    for pareja in match:
        print(pareja[0], " â†’ ", pareja[1])

def main():

    cordsA = obtener_coordenadas("A.txt")
    cordsB = obtener_coordenadas("B.txt")

    match = gale_shapley(cordsA, cordsB)

    imprimir(match)

main()
