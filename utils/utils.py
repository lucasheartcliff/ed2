import csv

from src.models.edge import Edge
from src.models.graph import Graph
from src.models.node import Node


def parse_matrix_from_csv_to_graph(filename):
    nodes = {}
    adjacency_list = {}

    with open(filename, "r") as file:
        csvreader = csv.reader(file)
        for i, raw_row in enumerate(csvreader):
            if not len(raw_row): continue
            node = Node(i)
            nodes[node.id] = node
            
            for j, cell in enumerate(raw_row):
                if cell == "" or cell == "0":
                    continue
                
                edge = Edge(i, j, float(cell))

                if i not in adjacency_list:
                    adjacency_list[i] = []

                adjacency_list[i].append(edge)

    return Graph(nodes,adjacency_list)
