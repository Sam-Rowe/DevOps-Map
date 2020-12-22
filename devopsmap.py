####
#
# This code/app/thoughts have no warranty to the extent of the law. It is released under the MIT licence. 
# Happy hacking.
# Samuel Rowe - 2020
#
####


import json
import pydot

class Practice(object):
    def __init__(self,name,rest):
        self.name = name
        self.label = None

    

def read_map_json():
    practices = {}
    data = json.load(open("DevOpsMap.json",'r',encoding='utf-8'))

    for key, value in data.items():
        practices[key] = Practice(key,value)
    
    return practices

def make_the_map():
    # start = "Automated Testing"
    graph = pydot.Dot()
    # automatic = pydot.Cluster()
    # automatic.set_label("automatic")
    # automatic.set_fontcolour("darkgrey")
    # graph.add_subgraph(automatic)

    practices = read_map_json()

    for practice in practices:
        node = pydot.Node(practice)
        # node.set_label(practice.label)
        node.set_shape('box')
        node.set_style('filled,setlinewidth(3.0)')
        node.set_color('black')
        node.set_fillcolor('lightgrey')
        node.set_fontsize('24')
        graph.add_node(node)

    #print(Practices)
    graph.write_svg('DevOpsMap.svg')

def main():
    make_the_map()


if __name__ == '__main__':
    main()
    