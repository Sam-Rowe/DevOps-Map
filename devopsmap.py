####
#
# This code/app/thoughts have no warranty to the extent of the law. It is released under the MIT licence. 
# Happy hacking.
# Samuel Rowe - 2020
#
####


import json
import pydot

class Node(object):
    def __init__(self,name,rest):
        self.name = name
        self.label = None

def read_map_json():
    nodes = {}
    data = json.load(open("./DevOpsMap.json",'r',encoding='utf-8'))

    for key, value in data.items():
        nodes[key] = Node(key,value)
    
    return nodes

def make_the_map():
    start = "Automated Testing"
    graph = pydot.Dot()
    automatic = pydot.Cluster()
    # automatic.set_label("automatic")
    # automatic.set_fontcolour("darkgrey")
    graph.add_subgraph(automatic)

    nodes = read_map_json()
    print(nodes)

def main():
    make_the_map()


if __name__ == '__main__':
    main()
    