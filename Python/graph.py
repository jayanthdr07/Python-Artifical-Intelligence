class Graph:
    def __init__(self, directed=False):
        self.directed = directed
        self.nodes = []
        self.adj_list = {}
        self.adj_matrix = []

    def add_node(self, node):
        if node in self.nodes:
            print("Node already exists!")
            return
        self.nodes.append(node)
        self.adj_list[node] = []
        for row in self.adj_matrix:
            row.append(0)
        self.adj_matrix.append([0] * len(self.nodes))
        print(f"Node {node} added.")

    def remove_node(self, node):
        if node not in self.nodes:
            print("Node not found!")
            return
        idx = self.nodes.index(node)
        self.nodes.remove(node)
        self.adj_list.pop(node)
        for n in self.adj_list:
            if node in self.adj_list[n]:
                self.adj_list[n].remove(node)
        self.adj_matrix.pop(idx)
        for row in self.adj_matrix:
            row.pop(idx)
        print(f"Node {node} removed.")

    def add_edge(self, src, dest):
        if src not in self.nodes or dest not in self.nodes:
            print("One or both nodes not found!")
            return
        if dest not in self.adj_list[src]:
            self.adj_list[src].append(dest)
            self.adj_matrix[self.nodes.index(src)][self.nodes.index(dest)] = 1
        if not self.directed:
            if src not in self.adj_list[dest]:
                self.adj_list[dest].append(src)
                self.adj_matrix[self.nodes.index(dest)][self.nodes.index(src)] = 1
        print(f"Edge {src} -> {dest} added.")

    def remove_edge(self, src, dest):
        if src not in self.nodes or dest not in self.nodes:
            print("One or both nodes not found!")
            return
        if dest in self.adj_list[src]:
            self.adj_list[src].remove(dest)
            self.adj_matrix[self.nodes.index(src)][self.nodes.index(dest)] = 0
        if not self.directed:
            if src in self.adj_list[dest]:
                self.adj_list[dest].remove(src)
                self.adj_matrix[self.nodes.index(dest)][self.nodes.index(src)] = 0
        print(f"Edge {src} -> {dest} removed.")

    def display(self):
        print("\nAdjacency List:")
        for node in self.adj_list:
            print(node, ":", self.adj_list[node])
        print("\nAdjacency Matrix:")
        print("   " + " ".join(self.nodes))
        for i, row in enumerate(self.adj_matrix):
            print(self.nodes[i], " ".join(map(str, row)))



directed_choice = input("Directed graph? (y/n): ").lower() == 'y'
g = Graph(directed=directed_choice)

n = int(input("Enter number of nodes: "))
for _ in range(n):
    node = input("Enter node name: ")
    g.add_node(node)

e = int(input("Enter number of edges: "))
for _ in range(e):
    src, dest = input("Enter edge (src dest): ").split()
    g.add_edge(src, dest)

while True:
    print("\nMenu:")
    print("1. Add Node")
    print("2. Remove Node")
    print("3. Add Edge")
    print("4. Remove Edge")
    print("5. Display Graph")
    print("6. Exit")
    choice = input("Enter choice: ")

    if choice == '1':
        g.add_node(input("Enter node name: "))
    elif choice == '2':
        g.remove_node(input("Enter node name: "))
    elif choice == '3':
        src, dest = input("Enter edge (src dest): ").split()
        g.add_edge(src, dest)
    elif choice == '4':
        src, dest = input("Enter edge (src dest): ").split()
        g.remove_edge(src, dest)
    elif choice == '5':
        g.display()
    elif choice == '6':
        break
    else:
        print("Invalid choice!")