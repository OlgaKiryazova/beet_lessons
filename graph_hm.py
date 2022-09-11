from collections import defaultdict
from queue import Queue


class Graph:

    def __init__(self, count_of_vertex):
        self.count = count_of_vertex
        self.graph = defaultdict(list)

    def add_edge(self, start, end):
        self.graph[start].append(end)

    def dfs(self, vertex, visited_vertex):
        visited_vertex[vertex] = True
        print(f'|{vertex}|', end='')
        for i in self.graph[vertex]:
            if not visited_vertex[i]:
                self.dfs(i, visited_vertex)

    def fill_order(self, vertex, visited_vertex, stack):
        visited_vertex[vertex] = True
        for i in self.graph[vertex]:
            if not visited_vertex[i]:
                self.fill_order(i, visited_vertex, stack)
        stack = stack.append(vertex)

    def transpose(self):
        graph_transpose = Graph(self.count)
        for i in self.graph:
            for j in self.graph[i]:
                graph_transpose.add_edge(j, i)
        return graph_transpose

    def print_scc(self):
        stack = []
        visited_vertex = [False] * self.count
        for i in range(self.count):
            if not visited_vertex[i]:
                self.fill_order(i, visited_vertex, stack)
        graph = self.transpose()
        visited_vertex = [False] * self.count
        while stack:
            i = stack.pop()
            if not visited_vertex[i]:
                graph.dfs(i, visited_vertex)
                print("")

    def bfs(self, start_vertex, target_vertex):
        visited_vertex = set()
        queue = Queue()
        queue.put(start_vertex)
        visited_vertex.add(start_vertex)
        parent = dict()
        parent[start_vertex] = None

        path_found = False
        while not queue.empty():
            current_vertex = queue.get()
            if current_vertex == target_vertex:
                path_found = True
                break

            for next_vertex in self.graph[current_vertex]:
                if next_vertex not in visited_vertex:
                    queue.put(next_vertex)
                    parent[next_vertex] = current_vertex
                    visited_vertex.add(next_vertex)

        path = []
        if path_found:
            path.append(target_vertex)
            while parent[target_vertex]:
                path.append(parent[target_vertex])
                target_vertex = parent[target_vertex]
            path.reverse()
        return path


def main():
    g = Graph(11)
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(1, 3)
    g.add_edge(3, 4)
    g.add_edge(4, 5)
    g.add_edge(5, 3)
    g.add_edge(6, 5)
    g.add_edge(6, 7)
    g.add_edge(7, 8)
    g.add_edge(8, 9)
    g.add_edge(9, 6)
    g.add_edge(10, 9)

    # Task 1
    print("Strongly Connected Components:")
    g.print_scc()

    # Task 2
    print("shortest path from each vertex to other vertex:")
    print(g.bfs(10, 3))


if __name__ == '__main__':
    main()