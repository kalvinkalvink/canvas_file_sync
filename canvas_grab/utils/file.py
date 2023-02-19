import os


class File:
    def make_dir(path):
        if not os.path.exists(path):
            print("making directory: ", path)
            os.makedirs(path)