class Top:
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return f'Top > {self.value}'

class Edge:
    def __init__(self,top,weight):
        self.top=top
        self.weight=weight

class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_node(self, value):
        v = Top(value)
        self.adjacency_list[v] = []
        return v

    def add_edge(self, start_node, end_node, weight=0):
        all_nodes=self.adjacency_list.keys()
        if not start_node in all_nodes and not end_node in all_nodes:
            return 'Both nodes not in the Graph'
        elif not start_node in all_nodes:
            return 'The first node not in the Graph'
        elif not end_node in all_nodes:
            return 'The seconde node not in the Graph'

        edge = Edge(end_node, weight)
        self.adjacency_list[start_node].append(edge)

    def get_nodes(self):
        array=[]
        for top in self.adjacency_list.keys():
            array.append(top)
        if len(array)==0:
            return None
        return array

    def get_neighbors(self, node):
        array=[]
        if node in self.adjacency_list :
            for edge in self.adjacency_list[node]:
               array.append((edge.top, edge.weight))

            return array
        if len(array)==0:
            return None


    def size(self):
        return len(self.adjacency_list.keys())

    def __str__(self):
        output = ''
        for top in self.adjacency_list.keys():
            output += top.value

            for edge in self.adjacency_list[top]:
                output += ' -> ' + edge.top.value
            output += '\n'
        return output

    def depth_first(self,start_node):
        if start_node not in self.adjacency_list.keys():
            return 'The node not in the graph'
        output=[]

        def recursive(node):
            print(node.value)
            if not node in output:
                output.append(node)
            for node2 in self.get_neighbors(node):
                if not node2[0] in output:
                    recursive(node2[0])
        recursive(start_node)
        return output

if __name__ == '__main__':
    pass
