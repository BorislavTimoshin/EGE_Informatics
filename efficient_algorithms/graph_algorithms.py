import collections
import heapq


# Поиск компонент связности. Сложность O(n + m)
class SearchForConnectivityComponents:
    def __init__(self):
        self.adj = None

    def add_edge(self, v, w):
        """ Добавление ребра в граф """
        self.adj[v].append(w)
        self.adj[w].append(v)

    def DFS(self, v, visited, component):
        """ Depth-first search """
        visited[v] = True  # Помечаем, что вершину прошли
        component.append(v)  # Добавлем вершину в пройденный граф (компоненту)
        for i in self.adj[v]:  # Для вершин, в которые следует вершина v
            if not visited[i]:  # Если не посещена
                self.DFS(i, visited, component)

    def connected_components(self, number_of_vertices: int, edges: list[list[int, int]]):
        """ Поиск компонент связности """
        self.adj = [[] for _ in range(number_of_vertices)]  # Список списков вершин, в которые
        # переходит вершина с номером i. Иными словами - список связанности
        for edge in edges:
            self.add_edge(*edge)

        visited = [False] * number_of_vertices
        components = []  # Список пройденных графов
        for v in range(number_of_vertices):  # Для каждой вершины графа
            if not visited[v]:  # Если вершина не посещена
                component = []
                self.DFS(v, visited, component)
                components.append(component)
        return components


class Graph(SearchForConnectivityComponents):
    @staticmethod
    def input_edges(number_of_edges) -> dict[int, list[int]]:
        _graph = {}
        for _ in range(number_of_edges):
            source, purpose = map(int, input().split())
            _graph.setdefault(source, []).append(purpose)
            _graph.setdefault(purpose, []).append(source)
        return _graph

    @staticmethod
    def BFS(info_about_vertice, source, destination, number_of_vertices, pred, dist):
        """ Поиск кратчайшего пути в графе -  BFS (Breadth first search: Поиск в первую очередь по ширине)
         Сложность O(n + m), где n - число вершин, m - число ребер
         Используем двусвязанный список для добавения элемента и его удаления на концах за O(1) """
        deque = collections.deque()
        visited = [False for _ in range(number_of_vertices)]
        visited[source] = True  # Отмечаем, что источник мы уже посетили
        dist[source] = 0  # Расстояние от источника равно 0
        deque.append(source)  # В двусвязанный список добавляем источник, откуда начинается поход

        while deque:
            last_vertice = deque.popleft()
            for i in range(len(info_about_vertice[last_vertice])):
                # Рассматриваем все вершины, в которые можно идти из last_vertice
                new_vertice = info_about_vertice[last_vertice][i]
                if not visited[new_vertice]:  # Если эта вершина еще не посещена, то идем дальше
                    visited[new_vertice] = True  # Отмечаем, что новую вершину посетили
                    dist[new_vertice] = dist[last_vertice] + 1  # К предыдущему расстоянию прибавляем 1
                    pred[new_vertice] = last_vertice  # У новой вершины предком является предыдущая вершина last_vertice
                    deque.append(new_vertice)  # В двусвязанный список идет новая вершина
                    if new_vertice == destination:
                        return True
        return False

    def shortest_distance(self, number_of_vertices, vertices, source, destination):
        """ Вывод кратчайшего пути в графе с помощью BFS. Можно также вывести проделанный путь. Сложность O(n + m) """
        info_about_vertice = [[] for _ in range(number_of_vertices)]
        for first_vertice, second_vertice in vertices:
            info_about_vertice[first_vertice].append(second_vertice)
            info_about_vertice[second_vertice].append(first_vertice)

        # Список потомков, например pred[2] равен 1, значит вершина 2 следует из вершины 1. Изначально все равны -1,
        # чтобы потом могли сделать проверку, что достигли источника, который равен -1
        pred = [-1 for _ in range(number_of_vertices)]
        # Создаем список расстояний для конкретных вершин. Например, dist[7] = 2. Значит, чтобы добраться до вершины 7,
        # нужно пройти через 1 вершину, 2 ребра
        dist = [1e12 for _ in range(number_of_vertices)]

        if not self.BFS(info_about_vertice, source, destination, number_of_vertices, pred, dist):
            print("Данный источник и пункт назначения не подключены")

        path = [destination]
        crawl = destination

        while pred[crawl] != -1:
            path.append(pred[crawl])
            crawl = pred[crawl]

        # Итоговый путь:
        # return path[::-1]
        # Длина самого короткого пути:
        return dist[destination]

    @staticmethod
    def dijkstra(graph, start):
        """ Нахождение кратчайших путей от заданной вершины до всех остальных вершин алгоритмом Дейкстры
        Сложность - O((N + M)logM) """
        distances = {vertex: float('infinity') for vertex in graph}
        distances[start] = 0
        queue = [(0, start)]
        heapq.heapify(queue)

        while queue:
            current_distance, current_vertex = heapq.heappop(queue)
            if current_distance > distances[current_vertex]:
                continue
            for neighbor, weight in graph[current_vertex].items():
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(queue, (distance, neighbor))

        return distances


''' Поиск компонент связности '''

# enges = [
#     [0, 1],
#     [1, 2],
#     [3, 4],
#     [4, 1],
#     [5, 6],
#     [6, 7],
#     [8, 9],
#     [9, 10]
# ]
# g = SearchForConnectivityComponents()
# print(g.connected_components(11, enges))

''' Нахождение кратчайших путей от заданной вершины до всех остальных вершин алгоритмом Дейкстры '''

# graph_object = Graph()
# g = {
#     'A': {'B': 1, 'C': 4},
#     'B': {'A': 1, 'C': 2, 'D': 5},
#     'C': {'A': 4, 'B': 2, 'D': 1, 'M': 6},
#     'D': {'B': 5, 'C': 1, 'M': 3},
#     'M': {'C': 6, 'D': 3, 'K': 4},
#     'K': {'M': 4}
# }
#
# start_vertex = 'A'
# shortest_distances = graph_object.dijkstra(g, start_vertex)
# print(f"Кратчайшие пути от вершины {start_vertex}: {shortest_distances}")
