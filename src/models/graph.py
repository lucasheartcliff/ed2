from .node import Node
from .edge import Edge
from sys import maxsize


class Graph:
    nodes: dict[any, Node]
    adjacency_list: dict[any, list[Edge]]

    def __init__(self, nodes, adjacency_list):
        self.nodes = nodes
        self.adjacency_list = adjacency_list

    def dfs(self, start, callback):
        stack = []
        visited = {}
        stack.append(start)

        while len(stack) != 0:
            node_id = stack.pop()

            if not visited[node_id]:
                if callback(self, node_id):
                    break
                visited[node_id] = True

            for edge in self.adjacency_list[node_id]:
                adj_node_id = edge.target
                if not visited[adj_node_id]:
                    stack.append(adj_node_id)

    def __find_parent(self, parent, node_id):
        if node_id == parent[node_id]:
            return node_id
        return self.__find_parent(parent[node_id])

    def kruskal(self, callback):
        merged_edge_list = []
        for edge_list in self.adjacency_list.values():
            merged_edge_list += edge_list

        merged_edge_list = sorted(merged_edge_list, key=lambda x: x.weight)

        parent = {}
        rank = {}

        for node in self.nodes.values():
            parent[node.id] = node.id
            rank[node.id] = 0

        for edge in merged_edge_list:
            source_parent = self.__find_parent(parent, edge.source)
            target_parent = self.__find_parent(parent, edge.target)

            if source_parent != target_parent:
                if rank[source_parent] < rank[target_parent]:
                    parent[source_parent] = target_parent
                    rank[target_parent] += 1
                else:
                    parent[target_parent] = source_parent
                    rank[source_parent] += 1
                callback(edge)

    def __min_key(self, key, visited):
        min_value = maxsize

        for node in self.nodes.values():
            if key[node.id] < min_value and not visited[node.id]:
                min_value = key[node.id]
                min_node = node

        return min_node

    def prim(self, start, callback):
        key = {}
        parent = {}
        mstSet = {}

        for node in self.nodes.values():
            key[node.id] = maxsize
            parent[node.id] = None
            mstSet[node.id] = False

        key[start] = 0
        parent[start] = -1

        for node in self.nodes.values():
            min_node = self.__min_key(key, mstSet)
            mstSet[min_node.id] = True

            adjacency = self.adjacency_list[min_node.id]

            for edge in adjacency:
                if not mstSet[edge.target] and key[edge.target] > edge.weight:
                    key[edge.target] = edge.weight
                    parent[edge.target] = min_node.id
                    callback(self,edge, key, parent)

    def dijkstra(self, start, callback):
        key = {}
        visited = {}

        for node in self.nodes.values():
            key[node.id] = maxsize
            visited[node.id] = False

        key[start] = 0

        for node in self.nodes.values():
            min_node = self.__min_key(key, visited)
            visited[min_node.id] = True

            adjacency = self.adjacency_list[min_node.id]

            for edge in adjacency:
                sum_dist = key[edge.source] + edge.weight
                if not visited[edge.target] and key[edge.target] > sum_dist:
                    key[edge.target] = sum_dist
        callback(key)
