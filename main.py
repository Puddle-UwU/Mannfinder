from _b_tree import b_tree
from fuzzywuzzy import fuzz


tree = b_tree()

tree.load(path="crate_database")


def search():
    query = input("query: ").strip().lower()

    for item in tree.tree:

        item_cleaned = item.strip().lower()
        related = []

        if fuzz.ratio(item_cleaned, query) >= 80 or fuzz.ratio(item_cleaned, f"the {query}") >= 80:
            print(item, tree.tree[item])
            
        if fuzz.partial_ratio(item_cleaned, query) >= 70:
            related.append(item)

    for item in sort_by_similarity(query, related):
        print(item, tree.tree[item])
            


def sort_by_similarity(target_string, items):

    scored_items = [(item, fuzz.ratio(target_string, item)) for item in items]
    sorted_items = sorted(scored_items, key=lambda x: x[1], reverse=True)
    return [item for item, score in sorted_items]


search()
