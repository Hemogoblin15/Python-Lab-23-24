import os
import sys


def read_and_print_files(directory_path, file_extension):
    try:
        if not os.path.exists(directory_path):
            raise FileNotFoundError(f"Directory not found: {directory_path}")

        for filename in os.listdir(directory_path):
            if filename.endswith(file_extension):
                file_path = os.path.join(directory_path, filename)

                try:
                    with open(file_path, 'r') as file:
                        print(f"Contents of {filename}:")
                        print(file.read())
                        print("-" * 30)

                except Exception as e:
                    print(f"Error reading file {filename}: {e}")

    except Exception as e:
        print(f"Error: {e}")


if len(sys.argv) != 3:
    print("Forma corecta: script.py <directory_path> <file_extension>")
else:
    directory_path = sys.argv[1]
    file_extension = sys.argv[2]

    read_and_print_files(directory_path, file_extension)
