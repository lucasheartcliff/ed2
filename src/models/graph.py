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

            if node_id not in visited:
                if callback(self, node_id):
                    break
                visited[node_id] = True

            adjacency = (
                self.adjacency_list[node_id] if node_id in self.adjacency_list else []
            )

            for edge in adjacency:
                adj_node_id = edge.target
                if adj_node_id not in visited:
                    stack.append(adj_node_id)

    def __find_parent(self, parent, node_id):
        if node_id == parent[node_id]:
            return node_id
        return self.__find_parent(parent, parent[node_id])

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
                callback(self, edge)

    def __min_key(self, key, visited):
        min_value = maxsize

        for node in self.nodes.values():
            if node.id in key and key[node.id] < min_value and node.id not in visited:
                min_value = key[node.id]
                min_node = node

        return min_node

    def prim(self, start, callback):
        key = {}
        parent = {}
        mstSet = {}

        key[start] = 0
        parent[start] = -1

        for node in self.nodes.values():
            min_node = self.__min_key(key, mstSet)
            mstSet[min_node.id] = True

            adjacency = self.adjacency_list[min_node.id]

            for edge in adjacency:
                if edge.target not in mstSet and (edge.target not in key):
                    key[edge.target] = edge.weight
                    parent[edge.target] = min_node.id
                    callback(self, edge, key, parent)

    def dijkstra(self, start, callback):
        key = {}
        visited = {}

        key[start] = 0

        for node in self.nodes.values():
            min_node = self.__min_key(key, visited)
            visited[min_node.id] = True

            adjacency = self.adjacency_list[min_node.id]

            for edge in adjacency:
                sum_dist = key[edge.source] + edge.weight
                if (
                    edge.target not in visited
                    and (edge.target in key and key[edge.target] > sum_dist)
                    or edge.target not in key
                ):
                    key[edge.target] = sum_dist
                    if callback(self, key):
                        return
