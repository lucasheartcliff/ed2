
from ..models.graph import Graph
from utils.utils import parse_matrix_from_csv_to_graph
import os



def q3(filename):
    print()
    print("Q3")
    labels = ["sfo","ord","bos","lax","dfw","jfk","mia"]
    result =[]
    def callback(graph, edge):
        result.append(edge)

    graph = parse_matrix_from_csv_to_graph(os.path.abspath(filename))

    graph.kruskal(callback)

    print()
    print("Source | Destination")
    for edge in result:
        print(labels[edge.source] + " | " + labels[edge.target])

