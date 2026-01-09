filename=input("Enter the file name(with Extension):")
try:
    with open(filename, 'r') as file:
        for lineno,line in enumerate(file, start=1):
            print(f"{lineno}: {line.strip()}")
except FileNotFoundationError:
    print(f"Error: The file '{filename}' was not found.")
except Exception as e:
    print(f"An unexpected error occured: {e}")