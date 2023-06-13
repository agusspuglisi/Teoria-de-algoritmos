import sys

def distancia(p, q):
    return ((p[0] - q[0])**2 + (p[1] - q[1])**2) ** 0.5

def cargar_puntos(archivo):
    puntos = []
    with open(archivo) as f:
        for linea in f:
            coordenadas = linea.rstrip('\n').split(" ")
            puntos.append((float(coordenadas[0].replace(",",".")), float(coordenadas[1].replace(",","."))))
    
    return puntos

def calcular_peso(p1, p2, p3):
    return distancia(p1, p2) + distancia(p2, p3) + distancia(p3, p1)


def imprimir_triangulacion(triangulacion, peso):
    print(f"Sumatoria obtenida: {peso}\n")
    print("Triangulos a armar: \n")
    for i in range(len(triangulacion)):
        print(f"triangulo {i+1} -> {triangulacion[i]}")


def triangular(poligono):
    n = len(poligono)
    infinito = float('inf')
    OPT = [[None]*n for _ in range(n)]
    triangulacion = [[[]]*n for _ in range(n)]

    for i in range(n):
        OPT[i][i] = 0
        triangulacion[i][i] = []
        if i < n - 1:
            OPT[i][i+1] = 0
            triangulacion[i][i+1] = []

    for tamanio in range(2,n):
        for i in range(n-tamanio):
            j = i + tamanio
            OPT[i][j] = infinito
            
            for k in range(i+1, j):
                peso = OPT[i][k] + OPT[k][j] + calcular_peso(poligono[i], poligono[j],poligono[k])
                if peso < OPT[i][j]:
                    OPT[i][j] = peso
                    triangulacion[i][j] = triangulacion[i][k] + triangulacion[k][j] + [(poligono[i], poligono[j], poligono[k])]
    
    return OPT[0][n-1], triangulacion[0][n-1]



def main():
    poligono = cargar_puntos(sys.argv[1])
    peso, triangulacion = triangular(poligono)
    imprimir_triangulacion(triangulacion, peso)

main()