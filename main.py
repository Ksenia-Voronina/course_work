class Graph:
    def __init__(self):
        self.edges = []
        self.length = 0

    def add_edge(self, start, end, weight):
        self.edges.append((start, end, weight))
        self.length += 1

    def __len__(self):
        return self.length

    def get_edges(self):
        return self.edges


class Min_spanning_tree:
    def __init__(self):
        self.edges = []
        self.totalWeight = 0

    def add_edge(self, start, end, weight):
        self.edges.append((start, end, weight))
        self.totalWeight += weight

    def get_edges(self):
        return self.edges

    def get_total_weight(self):
        return self.totalWeight


class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root == y_root:
            return
        if self.rank[x_root] < self.rank[y_root]:
            self.parent[x_root] = y_root
        elif self.rank[x_root] > self.rank[y_root]:
            self.parent[y_root] = x_root
        else:
            self.parent[y_root] = x_root
            self.rank[x_root] += 1


def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2][2]
    left = [x for x in arr if x[2] < pivot]
    middle = [x for x in arr if x[2] == pivot]
    right = [x for x in arr if x[2] > pivot]
    return quicksort(left) + middle + quicksort(right)


def kruskal(graph):
    edges = quicksort(graph)

    num_vertices = len(graph)
    min_spanning_tree = Min_spanning_tree()
    disjointSet = DisjointSet(num_vertices)

    for edge in edges:
        start, end, weight = edge
        if disjointSet.find(start) != disjointSet.find(end):
            min_spanning_tree.add_edge(start, end, weight)
            disjointSet.union(start, end)

    return min_spanning_tree


def output_graph(letters, graph):
    # вывод списка ребер
    print("Список ребер:", sep="\n")
    for i in graph.get_edges():
        print(f"[{letters[i[0]]}, {letters[i[1]]}, {i[2]}]")

    # вывод матрицы инцидентности
    print()
    print("Матрица инцидентности:", sep="\n")
    print("      ", *letters)
    for i in range(len(letters)):
        for el in graph.get_edges():
            if i == el[0]:
                print(f"({letters[i]}, {letters[el[1]]})", end=" ")
                for j in range(len(letters)):
                    if j == el[1]:
                        print(el[2], end=" ")
                    else:
                        print(0, end=" ")
                print()

    # вывод списков смежности
    print()
    print("Списки смежности:", sep="\n")
    cnt = 0
    for i in range(len(letters)):
        print(f"[{letters[i]}] ", end="")
        cnt = 0
        for el in graph.get_edges():
            if i == el[0]:
                print(f"-> {letters[el[1]]}:{el[2]} ", end="")
                cnt += 1
        if cnt == 0:
            print("-> нет вершин, следующих из этой")
        print()


def read_graph_from_file(filename):
    file = open(filename, 'r')
    letters = file.readline().split()
    graph = Graph()
    for i in range(len(letters)):
        line = file.readline().split()
        for j in range(i, len(line)):
            if int(line[j]) > 0:
                start, end, weight = i, j, int(line[j])
                graph.add_edge(start, end, weight)
    return letters, graph


print('Введите имя файла: ')
filename = input()
letters, graph = read_graph_from_file(filename)
output_graph(letters, graph)  # вывод матрицы инцидентности, списка смежности и списка ребер

min_tree = kruskal(graph.get_edges())

print("Конечный ответ")
for i in range(len(letters)):
    for j in min_tree.get_edges():
        if i == j[0]:
            print(letters[i], letters[j[1]])
print(min_tree.get_total_weight())



