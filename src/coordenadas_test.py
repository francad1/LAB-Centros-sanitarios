from coordenadas import *

def test_calc_dist(c1:Coordenadas,c2:Coordenadas):
    distancia = calcular_distancia(c1,c2)
    print("TEST CALCULO DISTANCIA")
    print("La distancia entre tus coordenadas es ")
    print(distancia)
    print("#####################################")

def test_media_coord(lista_coord):
    media = calcular_media_coordenadas(lista_coord)
    print("TEST CALCULO DE MEDIA")
    print("La media de tus coordenadas es ")
    print(media)
    print("#####################################")

a = Coordenadas(123.4,345.2)
b = Coordenadas(3485.4,27) 
c = Coordenadas(456.34,2635.2)
lista_coordenadas= [a,b,c]

if __name__ == "__main__":

    test_calc_dist(a,b)
    test_media_coord(lista_coordenadas)