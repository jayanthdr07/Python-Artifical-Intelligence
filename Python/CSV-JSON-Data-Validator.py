
import csv
import json
import os

filename = input("Enter file name (with extension): ")
_, ext = os.path.splitext(filename)
ext = ext.lower()

try:
    if ext == ".csv":
        with open(filename, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for i, row in enumerate(reader, start=1):
                if "" in row.values():
                    print(f"Warning: Record {i} has missing data ? {row}")
                else:
                    print(f"Record {i}: {row}")

    elif ext == ".json":
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
            if isinstance(data, dict):
                data = [data]
            for i, record in enumerate(data, start=1):
                if "" in record.values():
                    print(f"Warning: Record {i} has missing data ? {record}")
                else:
                    print(f"Record {i}: {record}")
    else:
        print("Only CSV or JSON files are supported.")

except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")
except (json.JSONDecodeError, csv.Error) as e:
     print(f"An unexpected error occured: {e}")
