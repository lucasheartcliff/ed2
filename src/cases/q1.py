
from ..models.graph import Graph
from utils.utils import parse_matrix_from_csv_to_graph
import os

def q1(filename):
    print()
    print("Q1")
    result =[]
    def callback(graph, node_id):
        node = graph.nodes[node_id]
        result.append(node)
        return node.id == 35

    graph = parse_matrix_from_csv_to_graph(os.path.abspath(filename))
    graph.dfs(0,callback)

    print("Position | Node")
    for index, node in enumerate(result):
        print(str(index) + " | " + str(node.id + 1))

