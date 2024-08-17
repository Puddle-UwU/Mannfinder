from _b_tree import b_tree
from fuzzywuzzy import fuzz


tree = b_tree()

tree.load(path="crate_database")


def search():
    query = input("query: ")

    for item in tree.tree:
        if fuzz.ratio(item, query) >= 80:
            print(tree.tree[item])


search()
