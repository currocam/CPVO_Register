#!/usr/bin/python
import CPVO_Register as CPVO
import pandas as pd
import sys
from time import time
def leerArchivo(direccion="lista.txt"):
    """Lee un archivo con los nombres de las especies de interés y sus archivos respectivos con el siguiente formato
    
    Especie, Dirección del archivo
    Brassica napus, brassicanapus.json
    """
    data = pd.read_csv(direccion)
    for index, line in data.iterrows():
        url=CPVO.obtenerURL_update(line[0])   
    print(url)

if __name__ == "__main__":
    """
    Ejemplo de uso para realizar la descarga de datos o la vigilancia para todas las especies de una lista. 
    
    python vigilanciaVariedades.py 0 "lista.txt"

    Ejemplo de uso para revisar si el archivo está actualizado.
    
    python buscarVariedades.py 1 "lista.txt"

    """   
    t0 = time()
    modo=sys.argv[1]
    direccion_archivo=sys.argv[2]
    data = pd.read_csv(direccion_archivo)
    for index, line in data.iterrows():
        especie=line[0]
        archivo=line[1]
        print(especie)
        url=CPVO.obtenerURL_update(especie)
        if modo=='0': #Generamos un archivo actualizado
            try:
                CPVO.archivoUpdate(url, archivo)
            except KeyError:
                print('No hay variedades registradas para esta especie')
                print(url)
            except:
                print('Ha habido un error')
                print(url)
                print(archivo)
        elif modo=='1': #Revisamos si el archivo está actualizado
            try: 
                CPVO.imprimirAviso(url, archivo)
            except:
                print('Ha habido un error')
                print(url)
                print(archivo)
        print("Finalizamos el scraping para la especie "+ especie)
    print("Realizado en %0.3fs" % (time() - t0))
