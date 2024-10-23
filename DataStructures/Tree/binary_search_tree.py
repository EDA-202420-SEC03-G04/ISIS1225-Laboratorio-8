from DataStructures.Tree import bst_node as node
from DataStructures.List import array_list as al
def new_map():
    return {
        'root': None,
        'type': 'BST'
    }

my_bst = new_map()
  
def _conteins(nodo,key,value):
    if nodo==None or value==True:
        return value
    if nodo["key"]==key:
        value=True
    else:
        value=_conteins(nodo["right"],key,value)
        value=_conteins(nodo["left"],key,value)
            
    return value
       
def contains(my_bst, key):
    if my_bst["root"]==None:
        return False
    value=False
    a=(_conteins(my_bst["root"],key,value))
    return a
    
def default_compare(key, element):
    other_key = node.get_key(element)
    if key == other_key:    
        return 0
    elif key > other_key:
        return 1
    else:    
        return -1

def is_empty(my_bst):
    return my_bst["root"] is None

def put(my_bst, key, value):
    my_bst['root'] = insert_node(my_bst['root'], key, value)
    return my_bst   
    
def insert_node(root, key, value):
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


def get(my_bst, key): 
    node = get_node(my_bst["root"], key)
    
    if node is None:
        return None
    
    return node["value"]


def get_node(root, key):
    if root is None:
        return None
    current_key = node.get_key(root)
    if current_key == key:
        return root
    elif key < current_key:
        return get_node(root["left"], key)
    else:
        return get_node(root["right"], key)
    
def size(my_bst):
    size = size_tree(my_bst["root"])
    return size

def size_tree(root):
    if root is None:
        return 0 
    
    left_size = size_tree(root["left"])
    right_size = size_tree(root["right"])
    
    return 1 + left_size + right_size

def key_set(my_bst):
    key_list = al.new_list()
    if my_bst["root"] is not None:
        key_set_tree(my_bst["root"], key_list)
    
    return key_list

def key_set_tree(root, key_list):
    if root is not None:
        key_set_tree(root["left"], key_list)
        
        al.add_last(key_list, root["key"])
        
        key_set_tree(root["right"], key_list)

def value_set(my_bst):
    lsit=al.new_list()
    lsit=value_set_tree(my_bst["root"], lsit)
    return lsit
    
def value_set_tree(root, value_list):
   

    if root is not None:
       
        value_set_tree(root["left"], value_list)
        al.add_last(value_list,root["value"])
        value_set_tree(root["right"],value_list) 
    else:
        pass    
    return value_list

def min_key(my_bst):
    return min_key_node(my_bst["root"])
     
def min_key_node(root):
    
    if root == None:
        return None
    if root["left"] is  None:
        return root["key"]
    return min_key_node(root["left"])
  
def max_key(my_bst):
    return max_key_node(my_bst["root"])
    
def max_key_node(root):
    if root == None:
        return None
    if root["right"] is  None:
        return root["key"]
    return max_key_node(root["right"])
  
def delete_min(my_bst):
    if my_bst["root"] !=None:
        delete_min_tree(my_bst["root"])
    return my_bst

def delete_min_tree(root):
    root["size"]-=1
    if root["left"]["left"]==None:
        root["left"]=None
    else:
        delete_min_tree(root["left"])    
   
def delete_max(my_bst):
    if is_empty(my_bst):
        return None
    else:  
        root = my_bst["root"]
        my_bst["root"] = delete_max_tree(root)
        return my_bst

def delete_max_tree(root):
    root["size"]-=1
    if root["right"] is None:
        return root["left"]
    root["right"] = delete_max_tree(root["right"])
    return root

def height(my_bst):
    return height_tree(my_bst["root"])

def height_tree(root):
    if root is None:
        return -1
    else:
        return 1 + max(height_tree(root["left"]), height_tree(root["right"]))

def keys(my_bst, key_lo, key_hi):
    if is_empty(my_bst):
        return al.new_list()
    else:  
        lista = al.new_list()
        return keys_range(my_bst["root"], key_lo, key_hi, lista)

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

def values(my_bst, key_lo, key_hi):
    if is_empty(my_bst):
        return al.new_list()
    else:  
        return values_range(my_bst["root"], key_lo, key_hi, al.new_list())

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
    