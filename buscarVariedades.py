#!/usr/bin/python
import CPVO_Register as CPVO
import sys
from time import time
if __name__ == "__main__":
    """
    Ejemplo de uso para generar un archivo con todas las variedades de una especie.
    
    python buscarVariedades.py "Brassica napus" "entradas.json" 0

    Ejemplo de uso para revisar si el archivo está actualizado.
    
    python buscarVariedades.py "Brassica napus" "entradas.json" 1

    """
    t0 = time() #Medir tiempo utilizado
    especie= sys.argv[1] 
    direccion_archivo=sys.argv[2]
    modo=sys.argv[3]
    url=CPVO.obtenerURL_update(especie)   
    if modo=='0': #Generamos un archivo actualizado
        try:
            CPVO.archivoUpdate(url, direccion_archivo)
        except:
            print('Ha habido un error')
            print(url)
    elif modo=='1': #Revisamos si el archivo está actualizado
        try: 
            CPVO.imprimirAviso(url, direccion_archivo)
        except:
            print('Ha habido un error')
            print(url)
            print(direccion_archivo)
    print("Realizado en %0.3fs" % (time() - t0))
