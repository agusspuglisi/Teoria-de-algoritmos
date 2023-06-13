from graph_parser import graph_parser
import sys


def print_matrix(vertex_names, ad_matrix):
    print(vertex_names)
    for i in range(len(vertex_names)):
        print(vertex_names[i], ad_matrix[i][: len(vertex_names)])


path = sys.argv[1]
graph = graph_parser(path)
max_flow, matrix = graph.max_flow()
print(max_flow)
if max_flow != -1:
    print_matrix(graph.get_vertex_names(), matrix)
else:
    print("Cant satisfy the minimum flow requirements")
