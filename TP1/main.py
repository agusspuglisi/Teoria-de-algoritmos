import argparse



def imprimir_resultados(k, M):
    print("Tamaño del matching: " + str(k))
    print("Matching: " + "\n")
    print("(A -> B)")

    for ai, bj in M:
        print(f"{ai} -> {bj}")



# Realizo el parseo del archivo y le doy el formato que necesito para el algoritmo greedy propuesto
def obtener_puntos(archivo):
    puntos = []
    with open(archivo) as f:

        for linea in f:
            coordenadas = linea.strip().split()
            x = float(coordenadas[0].replace(',', '.'))
            y = float(coordenadas[1].replace(',', '.'))
            puntos.append((x, y))

    return puntos



def matching_maximo(A, B, n):

    A = obtener_puntos(A)
    B = obtener_puntos(B)

    A = sorted(A, key = lambda a: a[0]) 
    B = sorted(B, key = lambda b: b[0]) 

    M = []
    k = 0
    i = 0

    dist_min = float('inf')
    pAseleccionado = None
    pBseleccionado = None

  
    while i < n:
   
        for bj in B:

            if bj[0] > A[i][0]:
                break

            if bj[1] > A[i][1]:
                continue

            dist = abs(bj[1] - A[i][1])

            if dist < dist_min:
                dist_min = dist
                pAseleccionado = A[i]
                pBseleccionado = bj

        if pBseleccionado is not None:
            M.append([pAseleccionado, pBseleccionado])
            B.remove(pBseleccionado)
            k += 1

            dist_min = float('inf')
            pAseleccionado = None
            pBseleccionado = None

        i += 1

    imprimir_resultados(k, M)



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = 'Ejecuta el algoritmo de matching máximo.')
    parser.add_argument('archivo_a', type = str, help = 'Archivo que contiene los puntos del conjunto A')
    parser.add_argument('archivo_b', type = str, help = 'Archivo que contiene los puntos del conjunto B')
    parser.add_argument('n', type = int, help = 'Número de puntos en los conjuntos A y B')
    args = parser.parse_args()

    matching_maximo(args.archivo_a, args.archivo_b, args.n)