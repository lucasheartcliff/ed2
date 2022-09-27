class Dijkstra:

    def __init__(self, vertices, graph):
        self.vertices = vertices
        self.graph = graph

    def find_route(self, start, end):
        unvisited = {n: float("inf") for n in self.vertices}
        unvisited[start] = 0
        visited = {}
        parents = {}
        while unvisited:
            min_vertex = min(unvisited, key=unvisited.get)  
            for neighbour, _ in self.graph.get(min_vertex, {}).items():
                if neighbour in visited:
                    continue
                new_distance = unvisited[min_vertex] + self.graph[min_vertex].get(neighbour, float("inf"))
                if new_distance < unvisited[neighbour]:
                    unvisited[neighbour] = new_distance
                    parents[neighbour] = min_vertex
            visited[min_vertex] = unvisited[min_vertex]
            unvisited.pop(min_vertex)
            if min_vertex == end:
                break
        return parents, visited

    def generate_path(self, parents, start, end):
        path = [end]
        while True:
            key = parents[path[0]]
            path.insert(0, key)
            if key == start:
                break
        return path

input_vertices = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10",
                "11", "12", "13", "14", "15", "16", "17", "18", "19", "20",
                "21", "22", "23", "24", "25", "26", "27", "28")



input_graph = {
        '1': {'2':12.8, '7':29, '8':27.7, '9':23.6},
        '2': {'1':12.8, '3':24.1, '4':42, '8':22.3, '7':17},
        '3': {'2':24.1, '4':12.8, '6':30.8, '7':32},
        '4': {'3':12.8, '5':20, '2': 42},
        '5': {'4':20, '6':25, '15':21.6, '14':45},
        '6': {'3':30.8, '5':25, '14':31.3, '13':33.4, '12':37.3, '7':14.8},
        '7': {'2':17, '3':32, '6':14.8, '13':41.3, '12':33, '11':32.5, '8':24.8, '1':29},
        '8': {'1':27.7, '2':22.3, '7':24.8, '11':19.8, '10':50, '9':26.3},
        '9': {'1':23.6, '8':26.3, '10':24},
        '10': {'9':24, '8':50, '11':24, '19':20, '20':39.8},

        '11': {'8':19.8, '7':32.5, '12':23, '19':38, '10':24},
        '12': {'7':33, '6':37.3, '13': 20, '17':39, '18':59, '11':23},
        '13': {'7':41.3, '6':33.4, '16':32.5, '14':16, '17':34.4, '12':20},
        '14': {'15':23.8, '5':45, '6':31.3, '13':16, '16':39},
        '15': {'5':21.6, '14':23.8},
        '16': {'13':32.5, '14':39, '27':38, '28':33, '17':62.2},
        '17': {'12':39, '13':34.4, '16':62.2, '23':12.2, '18':22.6},
        '18': {'19':14.7, '12':59, '17':22.6, '23':20.4, '22':28.3},
        '19': {'10':20, '11':38, '18':14.7, '22':29, '20':34},
        '20': {'10':39.8, '21':15.7, '19':34},

        '21': {'20':15.7},
        '22': {'19':29, '18':28.3, '23':58.3},
        '23': {'22':58.3, '18':20.4, '17':12.2, '24':9.5, '26':24.2},
        '24': {'23':9.5, '25':23.6, '28':58, '26':21},
        '25': {'24':23.6, '28':42},
        '26': {'24':21, '23':24.2},
        '27': {'16':38, '28':26},
        '28': {'27':26, '16':33, '25':42, '24':58},
}
start = "8"
end = "26"
dijkstra = Dijkstra(input_vertices, input_graph)
p, v = dijkstra.find_route(start, end)
print("A distancia de  %s para %s e': %.2f" % (start, end, v[end]))
se = dijkstra.generate_path(p, start, end)
print("O caminho de  %s para %s e': %s" % (start, end, " -> ".join(se)))
print()


start = "8"
end = "27"
dijkstra = Dijkstra(input_vertices, input_graph)
p, v = dijkstra.find_route(start, end)
print("A distancia de  %s para %s e': %.2f" % (start, end, v[end]))
se = dijkstra.generate_path(p, start, end)
print("O caminho de  %s para %s e': %s" % (start, end, " -> ".join(se)))
print()


start = "8"
end = "15"
dijkstra = Dijkstra(input_vertices, input_graph)
p, v = dijkstra.find_route(start, end)
print("A distancia de  %s para %s e': %.2f" % (start, end, v[end]))
se = dijkstra.generate_path(p, start, end)
print("O caminho de  %s para %s e': %s" % (start, end, " -> ".join(se)))
print()