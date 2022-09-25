
from models.graph import Graph

def main():

    result =[]
    def callback(graph, node_id):
        node = graph.nodes[node_id]
        result.append(node)
        return node.data.is_end

    graph = Graph(None,None)

    graph.dfs(1,callback)

