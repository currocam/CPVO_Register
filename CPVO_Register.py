#!/usr/bin/python

from time import strftime
import time
import requests
import json

def obtenerURL_update(especie):
    """Elabora la url de la búsqueda adecuada en la web para descargar todas las variedades registradas hasta la fecha

        Parametros:
        especie (str): Nombre científico de la planta de interés
    
        Returns:
        url (str):url resultante sin el índice de página
    """
    str_specie="&speciesName="+especie.replace(" ", "%20")
    url="https://cpvonode.plantvarieties.eu/api/v2/publicSearch?"+str_specie+"&speciesNameFilter=contains&pageSize=100&pageNumber="
    return url

def descargarJSON(url, num_pag=1):
    """Descarga el contenido del archivo JSON correspondiente y lo devuelve en forma de diccionario
        Parametros:
        url(str): URL de la búsqueda en cuestión.
        num_page(int): Número de la página que se quiere descargar. Por defecto es la 1º página. 
        
        Returns:
        data(dict): Diccionario que contiene la información de la consulta.
    """
    result=[]
    respuesta = requests.get(str(url+str(num_pag)))
    data=respuesta.json()
    return data
    
def archivoUpdate(url, archivo="datos.json"):
    """Itera por todas las páginas de la base para descargar todos los datos y crear un archivo que los contenga todos
        
        Parametros:
        url(str): URL de la búsqueda en cuestión.
        archivo(str): Dirección del archivo que se quiere generar.  
        
    """
    
    data=descargarJSON(url) #descargamos la información de la 1º página
    
    #Determinamos cuantas páginas debemos iterar
    num_entradas=data['data']['count']
    iterador=int(num_entradas / 100) + (num_entradas % 100 > 0)
    
    result=[]
    i=2
    result.append(data['data']['registers'])
    print("Se ha registrado con éxito la página nº 1 de "+str(iterador))
    while i <= iterador:
        data=descargarJSON(url, i)
        result.append(data['data']['registers'])
        print("Se ha registrado con éxito la página nº: "+str(i)+" de "+str(iterador))
        i+=1
        time.sleep(1)
    with open(archivo, 'w') as json_file:
        json.dump(result, json_file)
    print("\n Su archivo ya se encuentra actualizado")
def actualizarAviso(url, archivo="datos.json"):
    """Itera por todas las páginas de la base para descargar todos los datos y crear un archivo que los contenga todos
        
        Parametros:
        url(str): URL de la búsqueda en cuestión.
        archivo(str): Dirección del archivo en que se guardan los datos.  
        
        Return:
        dif(int): Devuelve el número de entradas desactualizadas. En caso de dif=0, el archivo está actualizado. 
    """
    # Contamos el número de de entradas
    with open(archivo) as json_file:
        data_old = json.load(json_file)
    cont=0    
    for i in data_old:
        cont+=len(i)
    # Determinamos el número de entradas registradas en la web
    data_new=descargarJSON(url)
    dif=0
    if cont== data_new['data']['count']:
        print("El archivo sigue actualizado.")
    else:
        dif=data_new['data']['count']-cont
        print("El archivo no está actualizado. Hay un total de {0} entradas nuevas".format(dif))
    return dif


def imprimirAviso(url, archivo="datos.json"):
    """ Imprime en pantalla una serie de información pertinente, descarga el nuevo fichero actualizado e imprime por pantalla las entradas que se han añadido. 
        Parametros:
        url(str): URL de la búsqueda en cuestión.
        archivo(str): Dirección del archivo en que se guardan los datos.  
        
    """
    dif=actualizarAviso(url, archivo)
    if dif != 0:
        print("\n Procedemos a descargar los nuevos datos")
        archivoUpdate(url, archivo)
        with open(nombre_cientifico+ ".json") as json_file:
            data_actualizado = json.load(json_file)
        diccionario=data_actualizado[-1][-dif:]
        for i in diccionario:
            print("\n Entrada nueva:\n")
            print("Denominación: {0}\n Nombre de especie: {1}\n Día de solicitud: {2}".format(i['denomination'], i['speciesName'],i['applicationDate']))    


