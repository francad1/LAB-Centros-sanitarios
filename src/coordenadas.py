from collections import namedtuple

Coordenadas = namedtuple("Coordenadas","latitud,longitud")

def calcular_distancia(c1:Coordenadas,c2:Coordenadas):
    distancia = Coordenadas(abs(c1.latitud-c2.latitud),abs(c1.longitud-c2.longitud))
    return distancia
def calcular_media_coordenadas(lista_coord):
    latitudes=[]
    longitudes=[]
    for e in lista_coord:
        latitudes.append(e.latitud)
        longitudes.append(e.longitud)
    media_lat= sum(latitudes)/len(latitudes)
    media_lon= sum(longitudes)/len(longitudes)
    media_coord = Coordenadas(media_lat,media_lon)
    return media_coord
    