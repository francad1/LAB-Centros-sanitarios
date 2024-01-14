import csv
from collections import namedtuple
from coordenadas import Coordenadas, calcular_distancia, calcular_media_coordenadas
from typing import List
from mapas import *

CentroSanitario = namedtuple('CentroSanitario', 'nombre, localidad, coordenadas, estado, num_camas, acceso_minusvalidos, tiene_uci')

def leer_centros(path):

    centros=[]

    with path as archivo:
        next(archivo)
        reader = csv.reader(archivo,delimiter=";")
        for line in reader:
            nombre= str(line[0])
            localidad= str(line[1])
            coordenadas = Coordenadas(float(line[2]),float(line[3]))
            estado = str(line[4])
            num_camas= int(line[5])
            if str(line[6]) == "false":
                acceso_minusvalidos= False
            else :
                acceso_minusvalidos=True
            if str(line[7]) == "false":
                tiene_uci= False
            else :
                tiene_uci=True
            centro = CentroSanitario(nombre,localidad,coordenadas,estado,num_camas,acceso_minusvalidos,tiene_uci)
            centros.append(centro)
        return centros
    

def calcular_total_camas_centros_accesibles(centros):
    camas=[]
    for e in centros:
        camas.append(e.num_camas)
    camas_totales=sum(camas)
    return camas_totales

def obtener_centros_con_uci_cercanos_a(centros:List[CentroSanitario],coord:Coordenadas,dist:float):
    centros_cercanos=[]

    for e in centros:
        distancia = calcular_distancia(coord,e.coordenadas)
        if distancia.latitud<=dist and distancia.longitud<=dist:
            tupla= (e.nombre,e.localidad,e.coordenadas)
            centros_cercanos.append(tupla)

    return centros_cercanos

def generarMapa(lista_tuplas,path):
    
    coord = []

    for e in lista_tuplas:
        coord.append(e[2])
    media_coord= calcular_media_coordenadas(coord)
    mapa = crea_mapa(media_coord)
    for e in lista_tuplas:
        agrega_marcador(mapa,e[2],e[0],"red")
    
    guarda_mapa(mapa,path)