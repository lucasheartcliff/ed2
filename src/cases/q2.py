from ..models.graph import Graph
from utils.utils import parse_matrix_from_csv_to_graph
import os


def print_result(result, point):

    print("")
    print("Distance to point: " + str(point + 1))
    print("Position | Node | Distance from source")
    for index, r in enumerate(result):
        print(
            str(index + 1) + " | " + str(r["node_id"] + 1) + " | " + str(r["distance"])
        )


def parse_to_result_model(node_id, distance):
    return {"node_id": node_id, "distance": distance}


def equals_tolerance(a, b, tolerance):
    return abs(a - b) <= 0.5 * tolerance * (a + b)


def q2(filename):
    print()
    print("Q2")
    stop_points = [14, 25, 26]
    start_point = 7

    for point in stop_points:
        result = []

        def callback(graph, distances):
            if point in distances:
                nonlocal result
                result = [parse_to_result_model(point, distances[point])]
                idx = result[0]["node_id"]
                while idx != start_point:
                    adjacency = graph.adjacency_list[idx]

                    for edge in adjacency:
                        if edge.target not in distances:
                            continue
                        target = edge.target
                        if equals_tolerance(
                            (distances[idx] - edge.weight), distances[target], 0.01
                        ):
                            result.insert(
                                0, parse_to_result_model(target, distances[target])
                            )

                    idx = result[0]["node_id"]
                return True

        graph = parse_matrix_from_csv_to_graph(os.path.abspath(filename))

        # Start node is 8, but the index is 7
        graph.dijkstra(start_point, callback)
        print_result(result, point)
