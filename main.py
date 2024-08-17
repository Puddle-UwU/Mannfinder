from _b_tree import b_tree
from fuzzywuzzy import fuzz


tree = b_tree()

tree.load(path="crate_database")


def search():
    query = input("query: ").strip().lower()

    for item in tree.tree:
        item_cleaned = item.strip().lower()
        if fuzz.ratio(item_cleaned, query) >= 80 or fuzz.ratio(item_cleaned, f"the {query}") >= 80:
            print(item, tree.tree[item])


search()
