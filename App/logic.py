"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * Contribuciones
 *
 * Dario Correal
 """

import os
import csv
import datetime

from DataStructures.Tree import binary_search_tree as bst
from DataStructures.List import array_list as al
from DataStructures.Map import map_linear_probing as lp


data_dir = os.path.dirname(os.path.realpath('__file__')) + '/Data/'



def new_logic():
    """ Inicializa el analizador

    Crea una lista vacia para guardar todos los crimenes
    Se crean indices (Maps) por los siguientes criterios:
    -Fechas

    Retorna el analizador inicializado.
    """
    analyzer = {'crimes': None,
                'dateIndex': None
                }

    analyzer['crimes'] = al.new_list()
    analyzer['dateIndex'] = al.new_list
    
    return analyzer

# Funciones para realizar la carga

def load_data(analyzer, crimesfile):
    """
    Carga los datos de los archivos CSV en el modelo
    """
    crimesfile = data_dir + crimesfile
    input_file = csv.DictReader(open(crimesfile, encoding="utf-8"),
                                delimiter=",")
    for crime in input_file:
        add_crime(analyzer, crime)
    return analyzer



# Funciones para agregar informacion al analizador


def add_crime(analyzer, crime):
    """
    funcion que agrega un crimen al catalogo
    """
    al.add_last(analyzer['crimes'], crime)
    update_date_index(analyzer['dateIndex'], crime)
    return analyzer


def update_date_index(map, crime):
    """
    Se toma la fecha del crimen y se busca si ya existe en el arbol
    dicha fecha.  Si es asi, se adiciona a su lista de crimenes
    y se actualiza el indice de tipos de crimenes.

    Si no se encuentra creado un nodo para esa fecha en el arbol
    se crea y se actualiza el indice de tipos de crimenes
    """
    occurreddate = crime['OCCURRED_ON_DATE']
    crimedate = datetime.datetime.strptime(occurreddate, '%Y-%m-%d %H:%M:%S')
    entry = bst.get(map, crimedate.date())
    crimedate_key = crimedate.date()
    if entry is None:
        datentry = {
            'date': crimedate_key,
            'crimes': al.new_list()  
        }
        bst.put(map, crimedate_key, datentry)
    else:
        datentry = entry
    
    add_date_index(datentry, crime)
    
    return map


def add_date_index(datentry, crime):
    """
    Actualiza un índice de tipo de crímenes. Este índice tiene una lista
    de crímenes y una tabla hash cuya llave es el tipo de crimen y
    el valor es una lista con los crímenes de dicho tipo en la fecha que
    se está consultando (dada por el nodo del árbol).
    """
    lst = datentry['lstcrimes']
    al.add_last(lst, crime)
    offenseIndex = datentry['offenseIndex']
    offense_type = crime['OFFENSE_CODE_GROUP']
    offentry = lp.get(offenseIndex, offense_type)
    
    if offentry is None:
        new_offentry = al.new_list()
        al.add_last(new_offentry, crime)  
        lp.put(offenseIndex, offense_type, new_offentry)  
    else:
        al.add_last(offentry, crime)
    
    return datentry



def new_data_entry(crime):
    """
    Crea una entrada en el indice por fechas, es decir en el arbol
    binario.
    """
    entry = {'offenseIndex': None, 'lstcrimes': None}
    entry['offenseIndex'] = lp.new_map(num_elements=30,
                                        load_factor=0.5)
    entry['lstcrimes'] = al.new_list()
    return entry


def new_offense_entry(offensegrp, crime):
    """
    Crea una entrada en el indice por tipo de crimen, es decir en
    la tabla de hash, que se encuentra en cada nodo del arbol.
    """
    ofentry = {'offense': None, 'lstoffenses': None}
    ofentry['offense'] = offensegrp
    ofentry['lstoffenses'] = al.new_list()
    return ofentry


# ==============================
# Funciones de consulta
# ==============================


def crimes_size(analyzer):
    """
    Número de crimenes
    """
    return al.size(analyzer['crimes'])


def index_height(analyzer):
    """
    Altura del arbol
    """
    # TODO Completar la función de consulta
    pass


def index_size(analyzer):
    """
    Numero de elementos en el indice
    """
    tree = analyzer['bst']  
    return bst.height(tree)

def min_key(analyzer):
    """
    Retorna la llave más pequeña del árbol binario de búsqueda (BST) dentro del analyzer.
    """
    tree = analyzer['bst']  
    return bst.min_key(tree)  



def max_key(analyzer):
    """
    Llave mas grande
    """
    tree = analyzer["bst"]
    return bst.max_key(tree)

def get_crimes_by_range(analyzer, initialDate, finalDate):
    """
    Retorna el número de crímenes en un rango de fechas.
    """
    tree = analyzer['bst']  
    crimes_in_range = bst.keys(tree, initialDate, finalDate)  
    total_crimes = 0

    for date in crimes_in_range:
        entry = bst.get(tree, date)  
        crimes_list = entry['lstcrimes']  
        total_crimes += al.size(crimes_list)  

    return total_crimes



def get_crimes_by_range_code(analyzer, initialDate, offensecode):
    """
    Para una fecha determinada, retorna el número de crímenes de un tipo específico (offensecode).
    """
    tree = analyzer['bst']  
    entry = bst.get(tree, initialDate)  

    if entry is None:
        return 0  
    
    offenseIndex = entry['offenseIndex']
    crime_list_by_type = lp.get(offenseIndex, offensecode)
    
    if crime_list_by_type is None:
        return 0  
    
    return al.size(crime_list_by_type)

