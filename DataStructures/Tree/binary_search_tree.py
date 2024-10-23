from DataStructures.Tree import bst_node as nd
from DataStructures.List import array_list as al


def new_map():
    new_map = {
        "root" : None,
        "type" : "BST",
        "size" : 0
        }
    return new_map



def get (new_map, key):
    value = get_node(new_map['root'], key)
    return value


def get_node(node, key):
    if node is None:
        return None
    else:
        if default_compare(key, node) == 0:
            return node["value"]
        elif default_compare(key, node) == 1:
            return get_node(node["right"], key)
        else:
            return get_node (node["left"], key)
    
    
def min_key(new_map):
    min = min_key_node(new_map["root"])
    return min 

def min_key_node (node):
    
    if node == None:
        return None
    else:
        if node["left"] is None:
            return node["key"] 
        else:
            return min_key_node(node["left"])
         


def max_key(new_map):
    max = min_key_node(new_map["root"])
    return max 

def max_key_node (node):
    
    if node == None:
        return None
    else:
        if node["right"] is None:
            return node["key"] 
        else:
            return min_key_node(node["right"])
        
def height(node):
    """
    Retorna la altura de un nodo en el árbol binario de búsqueda (BST).
    """
    if node is None:
        return -1  
    else:
       
        left_height = height(node["left"])
        right_height = height(node["right"])
        return 1 + max(left_height, right_height)
        
        
            






def put (my_map, key, value):
    my_map["root"] = insert_node (my_map["root"], key, value)

    return my_map


def insert_node (root, key, value):
    nodo = nd.new_node(key, value)
    if default_compare():
        if root["right"] == None:
            root["righ"] = nodo
    if root["key"] <= nodo["key"]:
        if root["left"] == None:
            root["left"] = nodo
    return root






def contains(my_map, key):
    pass



def max_key (my_map):
    pass  



def default_compare(key, elemnet):
    if elemnet["key"] == key: 
        return 0 
    elif elemnet["key"] < key: 
        return 1
    else:
        return -1
    