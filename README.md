# Python-Artifical-Intelligence


1️⃣ Taking file name input
filename = input("Enter the file name(with Extension):")

Explanation:

Prompts the user to enter a file name along with its extension
(example: sample.txt, data.py)

The input is stored in the variable filename

This makes the program dynamic, allowing it to work with any text file

2️⃣ Starting the try block
try:

Explanation:

Begins a try block for exception handling

Any error that occurs inside this block will be caught by the except clauses

Prevents the program from crashing unexpectedly

3️⃣ Opening the file
with open(filename, 'r') as file:

Explanation:

Opens the file specified by filename

'r' means read mode

with is a context manager:

Automatically closes the file after use

Prevents file-handling errors and memory leaks

file is the file object used to read the content

4️⃣ Reading the file line by line with line numbers
for lineno, line in enumerate(file, start=1):

Explanation:

file is iterable, so Python reads it line by line

enumerate():

lineno → line number

line → actual line text

start=1 makes line numbering begin at 1 instead of 0

Example:

Hello world
Python


Produces:

1 → Hello world
2 → Python

5️⃣ Printing line number and content
print(f"{lineno}: {line.strip()}")

Explanation:

Uses an f-string for clean formatting

line.strip():

Removes leading and trailing whitespace

Removes the newline character (\n)

Output format:

1: This is the first line
2: This is the second line

6️⃣ Handling file-not-found error ❌ (Typo here)
except FileNotFoundationError:

Explanation:

This line contains a typo

Python’s correct exception name is:

FileNotFoundError

What it should be:
except FileNotFoundError:

Purpose:

Catches the error when the file does not exist

Prevents a crash and shows a friendly message

print(f"Error: The file '{filename}' was not found.")

Explanation:

Prints a clear message explaining why the program failed

7️⃣ Catching any other unexpected errors
except Exception as e:

Explanation:

Catches any other exception not specifically handled above

e stores the error message

print(f"An unexpected error occured: {e}")

Explanation:

Displays the error message

Helpful for debugging issues like:

Permission errors

Encoding problems

✅ Corrected Version of the Code
filename = input("Enter the file name (with extension): ")

try:
    with open(filename, 'r') as file:
        for lineno, line in enumerate(file, start=1):
            print(f"{lineno}: {line.strip()}")

except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")

except Exception as e:
    print(f"An unexpected error occurred: {e}")

🔁 Overall Program Flow

User enters file name

Program attempts to open the file

Reads the file line by line

Prints each line with a line number

Handles missing file or unexpected errors safely
                 *****************************
1. Importing required modules
import csv
import json
import os

Explanation:

csv
→ Used to read CSV (Comma-Separated Values) files in a structured way.

json
→ Used to read and parse JSON (JavaScript Object Notation) files.

os
→ Used here to work with file paths and extensions (os.path.splitext).

2. Taking file name input from the user
filename = input("Enter file name (with extension): ")

Explanation:

Prompts the user to enter a file name (example: data.csv or records.json).

The input is stored in the variable filename.

3. Extracting the file extension
_, ext = os.path.splitext(filename)

Explanation:

os.path.splitext(filename) splits the file name into:

file name without extension

file extension

Example:

"data.csv" → ("data", ".csv")


_ ignores the file name part.

ext stores the extension (.csv or .json).

ext = ext.lower()

Explanation:

Converts the extension to lowercase.

Ensures that .CSV, .Csv, etc. are treated the same as .csv.

4. Starting the error-handling block
try:

Explanation:

Starts a try block to catch runtime errors like:

File not found

Invalid CSV/JSON format

Prevents the program from crashing.

5. Handling CSV files
if ext == ".csv":

Explanation:

Checks whether the entered file is a CSV file.

If true, the CSV-specific code runs.

with open(filename, 'r', encoding='utf-8') as f:

Explanation:

Opens the CSV file in read mode.

utf-8 ensures compatibility with most text files.

with automatically closes the file after use.

reader = csv.DictReader(f)

Explanation:

Reads the CSV file as a dictionary.

Each row becomes a dictionary:

{'Name': 'John', 'Age': '25'}


Column headers become dictionary keys.

for i, row in enumerate(reader, start=1):

Explanation:

Loops through each row in the CSV file.

enumerate:

i → record number (starting from 1)

row → dictionary representing the current row

if "" in row.values():

Explanation:

Checks if any field is empty in the row.

row.values() returns all values of the row.

"" means missing or empty data.

print(f"Warning: Record {i} has missing data → {row}")

Explanation:

Displays a warning if missing data is found.

Shows the entire record for clarity.

else:
    print(f"Record {i}: {row}")

Explanation:

If no missing values are found, prints the record normally.

6. Handling JSON files
elif ext == ".json":

Explanation:

Executes this block if the file extension is .json.

with open(filename, 'r', encoding='utf-8') as f:

Explanation:

Opens the JSON file safely for reading.

data = json.load(f)

Explanation:

Reads the JSON file and converts it into Python data:

JSON object → Python dictionary

JSON array → Python list

if isinstance(data, dict):
    data = [data]

Explanation:

Ensures consistent processing.

If the JSON contains a single dictionary:

{"name": "John", "age": 25}


It is converted into a list:

[{"name": "John", "age": 25}]


This allows looping uniformly.

for i, record in enumerate(data, start=1):

Explanation:

Loops through each JSON record.

i is the record number.

record is a dictionary.

if "" in record.values():

Explanation:

Checks for missing (empty string) values in the JSON record.

print(f"Warning: Record {i} has missing data → {record}")

Explanation:

Displays a warning message for incomplete records.

else:
    print(f"Record {i}: {record}")

Explanation:

Prints valid records without missing data.

7. Unsupported file type handling
else:
    print("Only CSV or JSON files are supported.")

Explanation:

Runs if the file is not .csv or .json.

Prevents processing unsupported formats.

8. Handling file-not-found errors
except FileNotFoundError:

Explanation:

Catches errors when the file does not exist.

Prevents the program from crashing.

print(f"Error: File '{filename}' not found.")

Explanation:

Displays a user-friendly error message.

9. Handling CSV and JSON format errors
except (json.JSONDecodeError, csv.Error) as e:

Explanation:

Catches:

Invalid JSON structure

Corrupt or improperly formatted CSV files

print(f"An unexpected error occured: {e}")

Explanation:

Prints the actual error message for debugging.

🔁 Overall Program Flow

User enters file name

Program detects file type

Reads CSV or JSON accordingly

Checks each record for missing data

Displays warnings or records

Handles errors safely
******************************************************
1. Graph Class Definition
class Graph:
    def __init__(self, directed=False):
        self.directed = directed
        self.nodes = []
        self.adj_list = {}
        self.adj_matrix = []


directed: Boolean, determines if the graph is directed (True) or undirected (False).

nodes: List of all nodes in the graph.

adj_list: A dictionary representing the adjacency list, where keys are node names and values are lists of connected nodes.

adj_matrix: A 2D list representing the adjacency matrix. Rows and columns correspond to nodes; 1 indicates an edge.

2. Adding a Node
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


Adds a new node to the graph.

Updates adjacency list: initializes an empty list for the new node.

Updates adjacency matrix:

Adds a new column (0) to all existing rows.

Adds a new row of zeros for the new node.

Ensures the graph structure stays consistent.

3. Removing a Node
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


Removes a node from the graph.

Removes node from:

nodes list

adj_list dictionary

Any adjacency list of other nodes

adj_matrix (removes the corresponding row and column)

4. Adding an Edge
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


Adds an edge from src to dest.

Updates both adjacency list and adjacency matrix.

For undirected graphs, also adds the reverse edge (dest -> src).

5. Removing an Edge
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


Removes an edge from src to dest.

Updates adjacency list and matrix.

For undirected graphs, removes the reverse edge as well.

6. Displaying the Graph
def display(self):
    print("\nAdjacency List:")
    for node in self.adj_list:
        print(node, ":", self.adj_list[node])
    print("\nAdjacency Matrix:")
    print("   " + " ".join(self.nodes))
    for i, row in enumerate(self.adj_matrix):
        print(self.nodes[i], " ".join(map(str, row)))


Prints the graph in adjacency list format.

Prints the graph in adjacency matrix format.

7. User Interaction
directed_choice = input("Directed graph? (y/n): ").lower() == 'y'
g = Graph(directed=directed_choice)


Lets the user choose directed or undirected graph.

n = int(input("Enter number of nodes: "))
for _ in range(n):
    node = input("Enter node name: ")
    g.add_node(node)


Adds nodes interactively.

e = int(input("Enter number of edges: "))
for _ in range(e):
    src, dest = input("Enter edge (src dest): ").split()
    g.add_edge(src, dest)


Adds edges interactively.

8. Interactive Menu
while True:
    print("\nMenu:")
    print("1. Add Node")
    print("2. Remove Node")
    print("3. Add Edge")
    print("4. Remove Edge")
    print("5. Display Graph")
    print("6. Exit")


A simple menu loop that allows the user to modify the graph:

Add/remove nodes

Add/remove edges

Display graph

Exit program
