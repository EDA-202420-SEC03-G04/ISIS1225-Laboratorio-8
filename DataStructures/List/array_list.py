def new_list():
    lst = {
        "elements" :[],
        "size" :0
    }
    
    return lst

def get_element(lst, pos):
    return lst["elements"][pos]

def is_present(lst, element, cmp_function):
    size = lst["size"]
    if size > 0:
        keyexist = False
        for keypos in range(0, size):
            info = lst["elements"][keypos]
            if (cmp_function(element, info) == 0):
                keyexist = True
                break
        
        if keyexist:
            return keypos
    return -1
       
        
def add_first(lst, elem):
    lst["elements"].insert(0,elem)
    lst["size"]+=1
    
    return lst


def add_last(lst, element):
    lst["elements"].append(element)
    lst["size"]+=1
    
    return lst

def is_empty(lst):
    size = lst["size"]
    if size == 0:
        return True
    else:
        return False
    
    
def first_element(lst):
    elements = lst["elements"]
    size = lst["size"]
    if size > 0:
        return elements[0]
    
def last_element(lst):
    elements = lst["elements"]
    size = lst["size"]
    if size > 0:
        return elements[-1]
    
def get_element(lst,pos):
    elements = lst["elements"]
    size = lst["size"]
    if size > 0:
        return elements[pos]
    
def delete_element(lst,pos):
    if lst["size"] > 0:
        lst["elements"].pop(pos)
        lst["size"] -= 1
    return lst

def remove_first(lst):
    if lst["size"] > 0:
        first_element = lst["elements"].pop(0)
        lst["size"] -= 1
    return first_element
    

def remove_last(lst):
    if lst["size"] > 0:
        last_element = lst["elements"].pop(-1)
        lst["size" ]-= 1
    return last_element
    
def insert_element(lst,element,pos):
    lst["elements"].insert(pos,element)
    lst["size"] += 1
    return lst  
    
def change_info(lst,pos,new_info):
    elements = lst["elements"]
    elements[pos] = new_info
    return lst

def exchange(lst,pos1,pos2):
    pos1 = lst["elements"][0]
    lst["elements"][0] = lst["elements"][1]
    lst["elements"][1] = pos1
    return lst

def size(lst):
    return lst["size"]
        
def sub_list(lst, pos, numelem):
    lista = {
        "elements" :[],
        "size" :0,
        "type":"ARRAY_LIST"
    }
    listica = lst["elements"]
    for posicion in range(pos,pos+numelem):
        dato = listica[posicion]
        lista["size"]+=1
        lista["elements"].append(dato)
    
    return lista
    
def selection_sort(lst, sort_crit):
    
    elements = lst['elements'] 
    size = lst['size']  
   
    if size <= 1:
        return lst

    for i in range(size):
        min_index = i

        for j in range(i + 1, size):
            
            if sort_crit(elements[j], elements[min_index]):
                min_index = j

        if min_index != i:
            elements[i], elements[min_index] = elements[min_index], elements[i]

    return lst


def insertion_sort(lst, sort_crit):
    
    elements = lst['elements']  
    size = lst['size']  

    if size <= 1:
        return lst

    for i in range(1, size):
        current_value = elements[i]
        position = i

        while position > 0 and sort_crit(current_value, elements[position - 1]):
            elements[position] = elements[position - 1]  
            position -= 1  
            
        elements[position] = current_value

    return lst


def shell_sort(lst, sort_crit):
    elements = lst['elements']  
    size = lst['size']
    
    if size <= 1:
        return lst

    gap = size // 2

    while gap > 0:
       
        for i in range(gap, size):
            current_value = elements[i]
            position = i

            while position >= gap and sort_crit(current_value, elements[position - gap]):
                elements[position] = elements[position - gap]  
                position -= gap  
            
            elements[position] = current_value

        gap //= 2

    return lst

def merge_sort(lst, sort_crit):
    elements = lst["elements"]
    size = lst["size"]

    if size <= 1:
        return lst

    mid = size // 2
    left_half = {"elements": elements[:mid], "size": mid}
    right_half = {"elements": elements[mid:], "size": size - mid}

    merge_sort(left_half, sort_crit)
    merge_sort(right_half, sort_crit)

    i = j = k = 0
    left_elements = left_half["elements"]
    right_elements = right_half["elements"]

    while i < len(left_elements) and j < len(right_elements):
        if sort_crit(left_elements[i], right_elements[j]):
            elements[k] = left_elements[i]
            i += 1
        else:
            elements[k] = right_elements[j]
            j += 1
        k += 1

    while i < len(left_elements):
        elements[k] = left_elements[i]
        i += 1
        k += 1

    while j < len(right_elements):
        elements[k] = right_elements[j]
        j += 1
        k += 1

    lst["elements"] = elements
    lst["size"] = size
    return lst


def quick_sort(lst, sort_crit):
    elements = lst["elements"]
    size = lst["size"]
    
    if size <= 1:
        return lst

    def partition(low, high):
        pivot = elements[high]
        i = low - 1  
        
        for j in range(low, high):
            if sort_crit(elements[j], pivot):  
                i += 1
                elements[i], elements[j] = elements[j], elements[i]

        elements[i + 1], elements[high] = elements[high], elements[i + 1]
        return i + 1  

    def quick_sort_recursive(low, high):
        if low < high:
            pivot_index = partition(low, high)
            quick_sort_recursive(low, pivot_index - 1)
            quick_sort_recursive(pivot_index + 1, high)

    quick_sort_recursive(0, size - 1)
    lst["elements"] = elements
    lst["size"] = size

    return lst

