import os
import sys

def rename_files_with_sequential_numbers(directory_path):
    try:
        if not os.path.exists(directory_path):
            raise FileNotFoundError(f"Directory not found: {directory_path}")

        files = [file for file in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, file))]

        for index, old_name in enumerate(files, start=1):
            new_name = f"file{index}{os.path.splitext(old_name)[1]}"
            old_path = os.path.join(directory_path, old_name)
            new_path = os.path.join(directory_path, new_name)

            try:
                os.rename(old_path, new_path)
                print(f"Renamed {old_name} to {new_name}")
            except Exception as e:
                print(f"Error renaming {old_name}: {e}")

    except Exception as e:
        print(f"Error: {e}")

if len(sys.argv) != 2:
    print("Usage: python script.py <directory_path>")
else:
    directory_path = sys.argv[1]
    rename_files_with_sequential_numbers(directory_path)


