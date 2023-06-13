from graph import Graph


def graph_parser(file):
    graph = Graph()
    with open(file) as f:
        lines = f.readlines()
        for line in lines:
            data = line.split(",")
            vertex_origin = str(data[0])
            vertex_destination = str(data[1])
            capacity = int(data[2])
            minimum_flow = int(data[3])
            graph.add_edge(
                vertex_origin, vertex_destination, capacity, minimum_flow)
    return graph
