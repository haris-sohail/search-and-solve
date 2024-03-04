from collections import deque
from queue import PriorityQueue
import util as ut

class Graph:
    class Node:
        def __init__(self, name):
            self.name = name
            self.children = []
            self.parent = None

        def add_child(self, child):
            self.children.append(child)

    def __init__(self):
        self.nodes = {}
        self.edge_costs = {}

    def add_node(self, name):
        if name not in self.nodes:
            self.nodes[name] = Graph.Node(name)

    def add_edge(self, parent, child, cost):
        if parent not in self.nodes:
            self.add_node(parent)
        if child not in self.nodes:
            self.add_node(child)
        self.nodes[parent].add_child(self.nodes[child])
        self.edge_costs[(parent, child)] = cost
        
    def reconstruct_path(self, came_from, start, goal):
        path = []
        current = goal
        while current != start:
            path.append(current)
            current = came_from[current]
            if current is None:
                return []
        path.append(start)
        path.reverse()
        return path
    
    def bfs(graph, start):
        min = float('inf')
        children = []
        visited = set()
        queue = deque([start])

        while queue:
            vertex = queue.popleft()
            if vertex not in visited:
                visited.add(vertex)
                
                if vertex != 'S':
                    cost = ut.getCost(vertex)
                    if(cost < min):
                        minPath = vertex
                        min = cost
                    
                for child in graph.nodes[vertex].children:
                    children.append(child.name)
                queue.extend(children)
                
        print("Minimum Path in BFS: ", minPath, ", with cost: ", min)
        
    def dfs(graph, start):
        min = float('inf')
        children = []
        visited = set()
        stack = deque([start])

        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.add(vertex)
                
                if vertex != 'S':
                    cost = ut.getCost(vertex)
                    if(cost < min):
                        minPath = vertex
                        min = cost
                    
                for child in graph.nodes[vertex].children:
                    children.append(child.name)
                stack.extend(children)
                
        print("Minimum Path in DFS: ", minPath, ", with cost: ", min)
        
    def ucs(graph, start): # graph is unweighted, same algorithm as bfs
        min = float('inf')
        children = []
        visited = set()
        queue = deque([start])

        while queue:
            vertex = queue.popleft()
            if vertex not in visited:
                visited.add(vertex)
                
                if vertex != 'S':
                    cost = ut.getCost(vertex)
                    if(cost < min):
                        minPath = vertex
                        min = cost
                    
                for child in graph.nodes[vertex].children:
                    children.append(child.name)
                queue.extend(children)
                
        print("Minimum Path in UCS: ", minPath, ", with cost: ", min)