from DataStructures.List import array_list as lt
from DataStructures.Map import map_functions as mf
from DataStructures.Map import map_entry as me



def new_map(num_elements, load_factor, prime=109345121):
    capacity = int(num_elements / load_factor) + 1
    if capacity < 2:
        capacity = 2
    scale = 1
    shift = 0  
    table = [None] * capacity
    my_map = {
        'prime': prime,
        'capacity': capacity,
        'scale': scale,
        'shift': shift,
        'table': table,
        'current_factor': 0,  
        'limit_factor': load_factor,
        'size': 0,  
        'type': 'PROBING'  
    }
    return my_map

def put(my_map, key, value):
     
    prime = my_map['prime']
    capacity = my_map['capacity']
    scale = my_map['scale']
    shift = my_map['shift']
    
    index = (scale * hash(key) + shift) % prime % capacity
    
    while my_map['table'][index] is not None:
        current_key, _ = my_map['table'][index]
        
        if current_key == key:
            my_map['table'][index] = (key, value)
            return my_map
        
        index = (index + 1) % capacity
        
    my_map['table'][index] = (key, value)
    my_map['size'] += 1
    my_map['current_factor'] = my_map['size'] / capacity
    
    if my_map['current_factor'] > my_map['limit_factor']:
        old_table = my_map['table']
        new_capacity = 2 * capacity + 1  
        my_map['capacity'] = new_capacity
        my_map['table'] = [None] * new_capacity
        my_map['size'] = 0  
        
        for entry in old_table:
            if entry is not None:
                old_key, old_value = entry
                put(my_map, old_key, old_value)
                
        return put(my_map, key, value)

    return my_map



def contains(my_map, key):
    prime = my_map['prime']
    capacity = my_map['capacity']
    scale = my_map['scale']
    shift = my_map['shift']
    
    index = (scale * hash(key) + shift) % prime % capacity
    while my_map['table'][index] is not None:
        current_key, _ = my_map['table'][index]
        if current_key == key:
            return True
        index = (index + 1) % my_map['capacity']

    return False

def get(my_map, key):
    prime = my_map['prime']
    capacity = my_map['capacity']
    scale = my_map['scale']
    shift = my_map['shift']

    index = (scale * hash(key) + shift) % prime % capacity

    while my_map['table'][index] is not None:
        current_key, current_value = my_map['table'][index]
        
        if current_key == key:
            return current_value
        
        index = (index + 1) % capacity

    return None


def size(my_map):
    return my_map['size']

def is_empty(my_map):
    return my_map['size'] == 0

def remove (my_map, key):
    pos = mf.hash_value(my_map, key)
    entry = ("EMPTY", "EMPTY")
    lista = my_map["table"]
    lista[pos] = entry
    my_map["size"] -=1

    return my_map


def key_set(my_map):
    key_list = lt.new_list()
    for pos in range(len(my_map["table"])):
            entry = my_map['table'][pos]
            if entry is not None:
                if entry[1] != "EMPTY":
                    lt.add_last(key_list, entry[0])
    return key_list  


def value_set(my_map):
    ltset = lt.new_list()
    for pos in range(len(my_map["table"])):
            entry = my_map['table'][pos]
            if entry is not None:
                 if entry[1] != "EMPTY":
                    lt.add_last(ltset, entry[1])
    return ltset



def find_slot(my_map, key, hash_value):
    lista = my_map["table"]
    size = len(lista)
    pos = hash_value % size
    initial_pos = pos  
    
    while lista[pos] is not None:
        
        if lista[pos] == ("EMPTY", "EMPTY") or lista[pos] == ("DELETED", "DELETED"):
            return False, pos
        
        if default_compare(lista[pos][0], key):
            return True, pos
        
        pos = (pos + 1) % size
        
        if pos == initial_pos:
            break
    
    return False, pos

def default_compare(a, b):
    return a == b






def is_available (table, pos):
    viable = False
    if table[pos] is None:
        viable = True
    elif table[pos] == ("EMPTY", "EMPTY"):
        viable = True

    return viable



def next_prime(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    while not is_prime(n):
        n += 1
    return n

def rehash(my_map):
    old_table = my_map["table"]
    new_capacity = next_prime(len(old_table) * 2)
    my_map["capacity"] = new_capacity
    my_map["table"] = [("EMPTY", "EMPTY")] * new_capacity
    my_map["size"] = 0  
    for entry in old_table:
        if entry is not None and entry != ("EMPTY", "EMPTY") and entry != ("DELETED", "DELETED"):
            key, value = entry
            pos = mf.hash_value(my_map, key)
            _, new_pos = find_slot(my_map, key, pos)
            my_map["table"][new_pos] = (key, value)
            my_map["size"] += 1
    
    return my_map



