import csv
import json
import networkx as nx
import matplotlib.pyplot as plt

def read_csv(file_name):
    edges = []
    with open(file_name, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if len(row) >= 2:  # at least source & destination
                src, dest = row[0], row[1]
                edges.append((src, dest))
    return edges

def read_json(file_name):
    with open(file_name) as jsonfile:
        data = json.load(jsonfile)
        nodes = data.get("nodes", [])
        edges = data.get("edges", [])
        return nodes, edges

def visualize_graph(G, layout_choice="spring"):
    if layout_choice == "spring":
        pos = nx.spring_layout(G)
    elif layout_choice == "circular":
        pos = nx.circular_layout(G)
    elif layout_choice == "shell":
        pos = nx.shell_layout(G)
    else:
        pos = nx.spring_layout(G)

    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=1200, font_size=10, edge_color='gray')
    plt.show()
.0
try:
    file_type = input("Enter file type (csv/json): ").strip().lower()
    file_name = input("Enter file name with extension: ").strip()
    directed_choice = input("Directed graph? (y/n): ").strip().lower() == 'y'

    G = nx.DiGraph() if directed_choice else nx.Graph()

    if file_type == "csv":
        edges = read_csv(file_name)
        G.add_edges_from(edges)
    elif file_type == "json":
        nodes, edges = read_json(file_name)
        G.add_nodes_from(nodes)
        G.add_edges_from(edges)
    else:
        print("Invalid file type!")
        exit()

    print(f"Nodes: {list(G.nodes())}")
    print(f"Edges: {list(G.edges())}")

    layout_choice = input("Choose layout (spring/circular/shell): ").strip().lower()
    visualize_graph(G, layout_choice)

except FileNotFoundError:
    print("Error: File not found!")
except json.JSONDecodeError:
    print("Error: Invalid JSON format!")
except csv.Error:
    print("Error: Problem reading CSV file!")
except Exception as e:
    print("Unexpected error:", e)
