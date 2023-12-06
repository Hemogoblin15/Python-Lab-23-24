import os
import sys


def count_number_of_files(path, extension):
    try:
        if (not os.path.exists(path)):
            raise FileNotFoundError
        files = [file for file in os.listdir(path) if os.path.isfile(os.path.join(path, file))]
        count = 0
        for file in files:
            if (file.endswith(extension)):
                count += 1
        print (count)
    except Exception as e:
        print(e)


if (len(sys.argv) != 3):
    print("belea")
else:
    count_number_of_files(sys.argv[1], sys.argv[2])
