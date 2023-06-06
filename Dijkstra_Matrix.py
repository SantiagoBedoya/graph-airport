import sys

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]

    def print_solution(self, distance):
        print("Vertex \tDistance from Source")
        for node in range(self.V):
            print(node, "\t\t", distance[node])

    def min_distance(self, distance, shortest_path_set):
        min_dist = sys.maxsize

        for v in range(self.V):
            if distance[v] < min_dist and shortest_path_set[v] == False:
                min_dist = distance[v]
                min_index = v

        return min_index

    def dijkstra(self, source):
        distance = [sys.maxsize] * self.V
        distance[source] = 0
        shortest_path_set = [False] * self.V

        for count in range(self.V):
            u = self.min_distance(distance, shortest_path_set)
            shortest_path_set[u] = True

            for v in range(self.V):
                if (
                    self.graph[u][v] > 0
                    and shortest_path_set[v] == False
                    and distance[v] > distance[u] + self.graph[u][v]
                ):
                    distance[v] = distance[u] + self.graph[u][v]

        self.print_solution(distance)


g = Graph(9)
g.graph = [
    [0, 4, 0, 0, 0, 0, 0, 8, 0],
    [4, 0, 8, 0, 0, 0, 0, 11, 0],
    [0, 8, 0, 7, 0, 4, 0, 0, 2],
    [0, 0, 7, 0, 9, 14, 0, 0, 0],
    [0, 0, 0, 9, 0, 10, 0, 0, 0],
    [0, 0, 4, 14, 10, 0, 2, 0, 0],
    [0, 0, 0, 0, 0, 2, 0, 1, 6],
    [8, 11, 0, 0, 0, 0, 1, 0, 7],
    [0, 0, 2, 0, 0, 0, 6, 7, 0],
]
g.dijkstra(0)
