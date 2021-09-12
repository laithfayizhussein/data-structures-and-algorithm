from collections import deque
class Queue():
    def __init__(self):
        self.dq = deque()
    def enqueue(self, value):
        self.dq.appendleft(value)
    def dequeue(self):
        return self.dq.pop()

    def __len__(self):
        return len(self.dq)

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
        self.adjacency_list={}

    def add_node(self,value):
        t=Top(value)
        self.adjacency_list[t] = []
        return t

    def add_edge(self,s_n, end_node,weight=0):
        all_nodes=self.adjacency_list.keys()
        if not s_n in all_nodes and not end_node in all_nodes:
            return 'Both nodes not in the Graph'
        elif not s_n in all_nodes:
            return 'The first node not in the Graph'
        elif not end_node in all_nodes:
            return 'The seconde node not in the Graph'

        edge=Edge(end_node,weight)
        self.adjacency_list[s_n].append(edge)

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

    def BreadthFirst(self,node):
        if node not in self.adjacency_list:
            return 'This node not in the graph'
        nodes=[]
        breadth =Queue()
        seen =set()

        breadth.enqueue(node)
        seen.add(node)

        while breadth:
            front=breadth.dequeue()
            nodes.append(front)
            for edge in self.adjacency_list[front]:
                if edge.top not in seen:
                    seen.add(edge.top)
                    breadth.enqueue(edge.top)

        return nodes
    def __str__(self):
        output = ''
        for top in self.adjacency_list.keys():
            output += top.value
            for edge in self.adjacency_list[top]:
                output += ' -> ' + edge.top.value
            output += '\n'
        return output


if __name__ == '__main__':
    pass





