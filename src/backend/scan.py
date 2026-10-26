import os

def scan(file_path):

    elements = {
        "Folders": [],
        "Files": []
    }

    for root, dirs, files in os.walk('test_files'):
        for file in files:
            elements["Files"].append(os.path.join(root, file))
        for folders in dirs:
            elements["Folders"].append(os.path.join(dirs, folders))

    return elements

        



        
