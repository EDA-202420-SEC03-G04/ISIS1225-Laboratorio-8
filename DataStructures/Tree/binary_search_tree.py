from DataStructures.Tree import bst_node as nd


def new_map():
    new_map = {
        "root" : None,
        "type" : "binary_search_tree"
        }
    return new_map




def insert (root, key, value):
    nodo = nd.new_node(key, value)
    if root["key"] >= nodo["key"]:
        if root["right"] == None:
            root["righ"] = nodo
    if root["key"] <= nodo["key"]:
        if root["left"] == None:
            root["left"] = nodo
    return root



def put (my_bst, key, value):
    nodo = nd.new_node(key, value)
    if my_bst["root"] == None:
        my_bst["root"] = nodo
    else:
        

        pass