import sys
import os


def calculate_total_size(directory_path):
    try:
        if not os.path.exists(directory_path):
            raise FileNotFoundError
        total_size = 0
        for (root, directories, files) in os.walk(directory_path):
            for fileName in files:
                file = os.path.join(directory_path, fileName)
                total_size += os.path.getsize(file)
                print(f"{file}: {os.path.getsize(file)}")
        print(total_size)
    except Exception as e:
        print(e)


if len(sys.argv) != 2:
    print("incorrect command")
else:
    directory_path = sys.argv[1]
    calculate_total_size(directory_path)
