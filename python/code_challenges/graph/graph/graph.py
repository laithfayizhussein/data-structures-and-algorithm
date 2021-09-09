class top:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'top > {self.value}'

class Edge:
    def __init__(self, top , weight):
        self.top =top
        self.weight =weight

class Graph:
    def __init__(self):
        self.adjc_list ={}

    def add_node(self, value):
        v = top(value)
        self.adjc_list[v] = []
        return v

    def add_edge(self, start_node, end_node, weight=0):
        all_nodes=self.adjc_list.keys()
        if not start_node in all_nodes and not end_node in all_nodes:
            return 'two nodes not in Graph'
        elif not start_node in all_nodes:
            return ' first node  not in  Graph'
        elif not end_node in all_nodes:
            return 'seconde node not in Graph'

        edge =Edge(end_node, weight)
        self.adjc_list[start_node].append(edge)

    def get_nodes(self):
        array=[]
        for top in self.adjc_list.keys():
            array.append(top)
        if len(array)==0:
            return None
        return array

    def get_neighbors(self, node):
        array=[]
        
        if node in self.adjc_list :
            for edge in self.adjc_list[node]:
               array.append((edge.top, edge.weight))
            return array

        if len(array)==0:
            return None

    def size(self):
        return len(self.adjc_list.keys())

    def __str__(self):
        output = ''
        for top in self.adjc_list.keys():

            output += top.value

            for edge in self.adjc_list[top]:
                output += ' -> ' + edge.top.value

            output += '\n'
        return output


if __name__ == '__main__':
    pass
