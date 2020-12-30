####
#
# This code/app/thoughts have no warranty to the extent of the law. It is released under the MIT licence. 
# Happy hacking.
# Samuel Rowe - 2020
#
####


import json
import pydot
import constants


class Practice(object):
    
    def __init__(self, name, practice_detail):
        self.name = name
        self.label = None
        self.enables = []
        self.reduces_failure_of = []
        self.better_with = []

        # if 'Description' in practice_detail:
        #     print(practice_detail.Description)

        if 'Enables' in practice_detail:
            for enabled in practice_detail['Enables']:
                self.enables.append(enabled)

        if 'ReducesFailureOf' in practice_detail:
            for reduces_failure_of in practice_detail['ReducesFailureOf']:
                self.reduces_failure_of.append(reduces_failure_of)

        if 'BetterTogetherWith' in practice_detail:
            for better_with in practice_detail['BetterTogetherWith']:
                self.better_with.append(better_with)

        # print(practice_detail)
    



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
        node.set_shape('egg')
        node.set_style('filled,setlinewidth(3.0)')
        node.set_fontcolor(constants.NODE_TEXT)
        node.set_fillcolor(constants.NODE_COLOUR)
        node.set_fontsize('24')
        graph.add_node(node)

    for practice in practices:
        print(practice)
        if hasattr(practices[practice], 'enables'):
            for Enables in practices[practice].enables:
                print(f"{practice}  --->   {Enables}")
                edge = pydot.Edge(practice, Enables)
                edge.set_tooltip(f"{practice}  enables   {Enables}")
                edge.set_color(constants.EDGE1)
                graph.add_edge(edge)

        if hasattr(practices[practice], 'reduces_failure_of'):
            for reduce_fail in practices[practice].reduces_failure_of :
                print(f"{practice}  -!!->   {reduce_fail}")
                edge = pydot.Edge(practice, reduce_fail)
                edge.set_tooltip(f"{practice}  reduces the failure rate of  {reduce_fail}")
                edge.set_color(constants.EDGE2)
                graph.add_edge(edge)

        if hasattr(practices[practice], 'better_with'):
            for better_with in practices[practice].better_with :
                print(f"{practice}  -+->   {better_with}")
                edge = pydot.Edge(practice, better_with)
                edge.set_tooltip(f"{practice}  better together with  {better_with}")
                edge.set_color(constants.EDGE3)
                graph.add_edge(edge)

    #print(Practices)
    graph.write_svg('DevOpsMap.svg')

def main():
    make_the_map()


if __name__ == '__main__':
    main()
    