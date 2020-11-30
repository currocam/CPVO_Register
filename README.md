# CPVO_Register
El objetivo de estos archivos es el de buscar a través del buscador de la CVPO (Community Plant Variety Office) encargada de administrar a nivel europeo la propiedad intelectual de las distintas variedades de plantas.  

https://public.plantvarieties.eu/publicSearch

Para descargar la información respectiva a todas las variedades de una especie en un archivo

>python buscarVariedades.py "{nombre científico de la especie}" "{archivo.json}" 0

Para comprobar si la información contenida en un archivo está actualizada

>python buscarVariedades.py "{nombre científico de la especie}" "{archivo.json}" 1

Es posible crear una lista de especies interés, la cual contenga los nombres científicos y los archivos respectivos de las especies de interés. 

El formato de la lista debe de ser el adecuado: Especie1, archivo1.json \n

Para descargar la información respectiva a todas las variedades de las especies indicadas:

>python vigilanciaVariedades.py 0 "lista.txt"

Para comprobar si la información de las especies indicadas está actualizada:

> python buscarVariedades.py 1 "lista.txt"
