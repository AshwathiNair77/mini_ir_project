# search.py
import json

INDEX_FILE = "index.json"

def load_index():
    with open(INDEX_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def search(query, index):
    query_words = query.lower().split()
    results = {}
    for word in query_words:
        docs = index.get(word, [])
        for doc in docs:
            results[doc] = results.get(doc, 0) + 1
    # Sort by frequency
    sorted_results = sorted(results.items(), key=lambda x: x[1], reverse=True)
    return [doc for doc, freq in sorted_results]

if __name__ == "__main__":
    index = load_index()
    query = input("Enter search query: ")
    results = search(query, index)
    print("Matching documents:", results)
