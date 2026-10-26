import os

class Data:
    def __init__(self, folder_path):
        self.folder_path = folder_path
        self.filename = os.path.basename(folder_path)
        pass

    def is_file(self):
        for file in self.folder_path:
            if self.filename == os.path.basename(self.folder_path):
                return True
        
    def create_file(self):
        pass

    def get_file(self):
        pass



if __name__ == "__main__":

    from hash import *

    hash_sha256(r"C:\Users\Joaot\OneDrive\Desktop\FileGuard\test_files")







#enter folderpath
#hash folderpath
#get folderpath from baseline