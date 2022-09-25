from models.node import Node
from models.edge import Edge


class Graph:
    nodes: dict[any,Node]
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

    def find_parent(self, parent, node_id):
        if node_id == parent[node_id]:
            return node_id
        return self.find_parent(parent[node_id])

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
            source_parent = self.find_parent(parent, edge.source)
            target_parent = self.find_parent(parent, edge.target)

            if source_parent != target_parent:
                if rank[source_parent] < rank[target_parent]:
                    parent[source_parent] = target_parent
                    rank[target_parent] +=1
                else:
                    parent[target_parent] = source_parent
                    rank[source_parent] += 1
                callback(edge)




