import os


class b_tree:
    def __init__(self):
        self.tree = {}

    def load(self, path):

        DIR = os.scandir(path)
        database = [file.name for file in DIR]

        for file in database:
            with open(f"{path}/{file}", "r") as curent:
                items = curent.read().split("\n")
                for item in items:
                    if item in self.tree:
                        if not file in self.tree[item]:
                            self.tree[item].append(file)
                    else:
                        self.tree[item] = [file]
