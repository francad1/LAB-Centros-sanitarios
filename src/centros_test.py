from centros import *
from coordenadas import Coordenadas


archivo = open("C:\\Users\\river\\Documents\\FP\\practica sanitarios\\LAB-Centros-sanitarios\\data\\centrosSanitarios.csv",encoding="UTF-8")

a = Coordenadas(136,10)


def dar_lista(datos):
    lista_centros = leer_centros(datos)
    return lista_centros


def test_lee_archivo(lista_centros):
    
    print("TEST LECTURA ARCHIVOS")
    print("LOS TRES PRIMEROS CENTROS SON:")
    print(lista_centros[0])
    print(lista_centros[1])
    print(lista_centros[2])
    print("#####################################################################################3")

def test_camas_totales(lista_centros):
    camas = calcular_total_camas_centros_accesibles(lista_centros)
    print("TEST CALCULO NUMERO TOTAL DE CAMAS")
    print("El numero total de camas es ")
    print(camas)
    print("#############################################################################################")

def test_centros_cercanos_a(lista_centros,coord:Coordenadas,dist:float):
    centros_cercanos = obtener_centros_con_uci_cercanos_a(lista_centros,coord,dist)
    #print("TEST OBTENER CENTROS CON UCI CERCANOS A UN PUNTO")
    #print("Los centros con UCI cercanos a las coordenadas dadas en funcion de la distancia dada son ")
    #print(centros_cercanos)
    #print("######################################################################################33")
    return centros_cercanos

def test_generar_mapa(lista_tuplas):
        print("TEST PARA GENERAR MAPA")
        generarMapa(lista_tuplas,"C:\\Users\\river\\Documents\\FP\\practica sanitarios\\LAB-Centros-sanitarios\\data\\mapa.html")



if __name__ == "__main__":
    centros= dar_lista(archivo)
    
    test_lee_archivo(centros)
    test_camas_totales(centros)
    test_centros_cercanos_a(centros,a,200)
    test_generar_mapa(test_centros_cercanos_a(centros,a,100))
