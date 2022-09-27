from ..models.edge import Edge
from utils.utils import parse_matrix_from_csv_to_graph
import os


def q4(filename):
    print()
    print("Q4")
    edges: list[Edge] = []

    def callback(graph, edge, key, parent):
        edges.append(edge)

    graph = parse_matrix_from_csv_to_graph(os.path.abspath(filename))

    graph.prim(0, callback)

    print("Edge | Weight")
    for edge in edges:
        print(str(edge.source) + "-" + str(edge.target) + " | " + str(edge.weight))
