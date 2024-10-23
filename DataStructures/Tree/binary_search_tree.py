from DataStructures.Tree import bst_node as node
from DataStructures.List import array_list as al


from DataStructures.List import array_list as al
from DataStructures.Tree import bst_node as node
# Funciones sin máscaras
from DataStructures.List import array_list as al
def new_map():
     bst = {'root': None,
           'type': 'BST' }
     return bst
  
def mascara_conteins(nodo,key,value):
    if nodo==None or value==True:
        return value
        
    
    if nodo["key"]==key:
        value=True
    else:
        value=mascara_conteins(nodo["right"],key,value)
        value=mascara_conteins(nodo["left"],key,value)
            
    return value
       
    

def contains(my_bst, key):
    if my_bst["root"]==None:
        return False
    value=False
    a=(mascara_conteins(my_bst["root"],key,value))
    return a
    
        
    
    """
    Informa si la llave key se encuentra en la tabla de símbolos.
    
    Args:
        my_bst: El árbol de búsqueda.
        key: La llave a buscar.
    
    Returns:
        True si la llave está presente, False en caso contrario.
    
    Raises:
        Exception
    """
    pass

def default_compare(key, element):
    
    
    
    """
    
    Función de comparación por defecto. Compara una llave con la llave de un elemento llave-valor.
    
    Parameters:
        key (any): Llave a comparar.
        element (map_entry): Entrada a comparar.
    
    Returns:
        0 si son iguales, 1 si key > la llave del element, -1 si key < que la llave del element.
    
    Return type:
        int
    """
    other_key = node.get_key(element)
    if key == other_key:    
        return 0
    elif key > other_key:
        return 1
    else:    
        return -1

def is_empty(my_bst):
    return my_bst["root"] is None

# Funciones con máscaras
#TODO: QUITAR "DESDE ACÁ"

# máscara
def put(my_bst, key, value):
    """
    Ingresa una pareja llave,valor. Si la llave ya existe, se reemplaza el valor.
    
    Parameters:
        my_bst (binary_search_tree): El BST.
        key (any): La llave asociada a la pareja.
        value (any): El valor asociado a la pareja.
    
    Returns:
        El árbol con la nueva pareja.
    
    Return type:
        binary_search_tree
    """
    my_bst['root'] = insert_node(my_bst['root'], key, value)

    return my_bst   
    

# recursiva
def insert_node(root, key, value):
    """
    Ingresa una pareja llave,valor. Si la llave ya existe, se reemplaza el valor.
    
    Parameters:
        root (bst_node): La raíz del árbol.
        key (any): La llave asociada a la pareja.
        value (any): El valor asociado a la pareja.
    
    Returns:
        El árbol con la nueva pareja.
    
    Return type:
        bst_node
    """
    if root is None:
        nodo = node.new_node(key, value)
        return nodo
    
    elif node.get_key(root) == key:
        root["value"] = value
        return root

    else:
        if node.get_key(root) > key:
            root["left"] = insert_node(root["left"], key, value)
        else:
            root["right"] = insert_node(root["right"], key, value)

        left_size = root["left"]["size"] if root["left"] is not None else 0
        right_size = root["right"]["size"] if root["right"] is not None else 0
        root["size"] = 1 + left_size + right_size
        
        return root


# máscara
def get(my_bst, key):
    """
    Retorna la pareja llave-valor con llave igual a key.
    
    Args:
        my_bst: El árbol de búsqueda.
        key: La llave asociada a la pareja.
    
    Returns:
        El nodo con la pareja llave-valor en caso de que haya sido encontrada.
    
    Raises:
        Exception: Si la llave no existe en el árbol.
    """
    node = get_node(my_bst["root"], key)
    
    if node is None:
        return None
    
    return node["value"]


#recursiva
def get_node(root, key):
    """
    Busca recursivamente el nodo con la llave igual a key.
    
    Args:
        root: El nodo actual en el árbol.
        key: La llave que se está buscando.
    
    Returns:
        El nodo con la pareja llave-valor.
    
    Raises:
        Exception: Si la llave no se encuentra en el árbol.
    """
    if root is None:
        return None
    
    current_key = node.get_key(root)
    
    if current_key == key:
        return root
    
    elif key < current_key:
        return get_node(root["left"], key)
    
    else:
        return get_node(root["right"], key)
    

# máscara
def size(my_bst):
    """
    Retorna el número de entradas en la tabla de símbolos.
    
    Args:
        my_bst: El árbol de búsqueda.
    
    Returns:
        El número de elementos en la tabla.
    
    Raises:
        Exception
    """
    size = size_tree(my_bst["root"])
    
    return size


#recursiva
def size_tree(root):
    """
    Retorna el número de entradas en la tabla a partir de un punto dado.
    
    Args:
        root: El árbol de búsqueda.
    
    Returns:
        El número de elementos en la tabla.
    
    Raises:
        Exception
    """
    if root is None:
        return 0 
    
    left_size = size_tree(root["left"])
    right_size = size_tree(root["right"])
    
    return 1 + left_size + right_size


# máscara
def key_set(my_bst):
    """
    Retorna una lista con todas las llaves de la tabla en orden ascendente.
    
    Args:
        my_bst: La tabla de símbolos.
    
    Returns:
        Una lista con todas las llaves de la tabla.
    
    Raises:
        Exception
    """
    key_list = al.new_list()
    if my_bst["root"] is not None:
        key_set_tree(my_bst["root"], key_list)
    
    return key_list


# recursiva
def key_set_tree(root, key_list):
    """
    Realiza un recorrido in-order del árbol para construir una lista con las llaves.
    
    Args:
        root: El nodo actual del árbol.
        key_list: La lista de respuesta donde se agregan las llaves.
    
    Returns:
        None. Las llaves se agregan a key_list.
    
    Raises:
        Exception
    """
    if root is not None:
        key_set_tree(root["left"], key_list)
        
        al.add_last(key_list, root["key"])
        
        key_set_tree(root["right"], key_list)

#TODO: HASTA ACÁ

# máscara
# #empiezo
def value_set(my_bst):
    lsit=al.new_list()
    
    lsit=value_set_tree(my_bst["root"], lsit)
    
    
    
    """
    Construye una lista con los valores de la tabla.
    
    Args:
        my_bst: La tabla con los elementos.
    
    Returns:
        Una lista con todos los valores.
    
    Raises:
        Exception
    """
    return lsit
    

# recursiva
def value_set_tree(root, value_list):
   

    if root is not None:
       
        value_set_tree(root["left"], value_list)
        al.add_last(value_list,root["value"])
        value_set_tree(root["right"],value_list)
        
        
        
       
    else:
        pass    
    return value_list

# máscara
def min_key(my_bst):
    
    return min_key_node(my_bst["root"])
     
  
# recursiva
def min_key_node(root):
    
    if root == None:
        return None
    if root["left"] is  None:
        return root["key"]
    return min_key_node(root["left"])
  

# máscara
def max_key(my_bst):
    return max_key_node(my_bst["root"])
    

# recursiva
def max_key_node(root):
    if root == None:
        return None
    if root["right"] is  None:
        return root["key"]
    return max_key_node(root["right"])
  

# máscara
def delete_min(my_bst):
    if my_bst["root"] !=None:
        delete_min_tree(my_bst["root"])
    
    
    return my_bst
   

# recursiva
def delete_min_tree(root):
    root["size"]-=1
    if root["left"]["left"]==None:
        root["left"]=None
    else:
        delete_min_tree(root["left"])    
   

# máscara
def delete_max(my_bst):
    if is_empty(my_bst):
        return None
    else:  
        root = my_bst["root"]
        my_bst["root"] = delete_max_tree(root)
        return my_bst

# recursiva#mi ultima
def delete_max_tree(root):
    root["size"]-=1
    if root["right"] is None:
        return root["left"]
    root["right"] = delete_max_tree(root["right"])
    return root
# máscara
def height(my_bst):
    return height_tree(my_bst["root"])

# recursiva
def height_tree(root):
    if root is None:
        return -1
    else:
        return 1 + max(height_tree(root["left"]), height_tree(root["right"]))

# máscara
def keys(my_bst, key_lo, key_hi):
    if is_empty(my_bst):
        return al.new_list()
    else:  
        lista = al.new_list()
        return keys_range(my_bst["root"], key_lo, key_hi, lista)

# recursiva
def keys_range(root, key_lo, key_hi, list_keys):
    if root == None:
        return list_keys
    if root["key"] > key_lo:
        keys_range(root["left"], key_lo, key_hi, list_keys)
    if key_lo <= root["key"] <= key_hi:
        al.add_last(list_keys, root["key"])
    if root["key"] < key_hi:
        keys_range(root["right"], key_lo, key_hi, list_keys)
    return list_keys

# máscara
def values(my_bst, key_lo, key_hi):
    if is_empty(my_bst):
        return al.new_list()
    else:  
        return values_range(my_bst["root"], key_lo, key_hi, al.new_list())

# recursiva
def values_range(root, key_lo, key_hi, list_values):
    if root is None:
        return list_values
    if root["key"] > key_lo:
        values_range(root["left"], key_lo, key_hi, list_values)
    if key_lo <= root["key"] <= key_hi:
        al.add_last(list_values, root["value"])
    if root["key"] < key_hi:
        values_range(root["right"], key_lo, key_hi, list_values)
    return list_values
    