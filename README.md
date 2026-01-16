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
