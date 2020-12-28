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
    
    
    def __init__(self, name, practice_detail):
        self.name = name
        self.label = None
        self.enables = set()

        # if 'Description' in practice_detail:
        #     print(practice_detail.Description)

        if 'Enables' in practice_detail:
            for enabled in practice_detail['Enables']:
                self.enables.update(enabled)

        print(practice_detail)
    



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

    for practice in practices:
        print(practice)
        if hasattr(practices[practice], 'enables'):
            # I don't understand why enables which I was trying to make an array is now a character map and my iterator is going through one letter at a time?
            for Enables in practices[practice].enables:
                print(practice & " -> " & Enables)
                edge = pydot.Edge(practice, Enables)
                graph.add_edge(edge)

    #print(Practices)
    graph.write_svg('DevOpsMap.svg')

def main():
    make_the_map()


if __name__ == '__main__':
    main()
    