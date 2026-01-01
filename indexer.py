# indexer.py
import os
import json

DATA_DIR = "data"
INDEX_FILE = "index.json"

def build_index(data_dir):
    index = {}
    for filename in os.listdir(data_dir):
        if filename.endswith(".txt"):
            path = os.path.join(data_dir, filename)
            with open(path, "r", encoding="utf-8") as f:
                text = f.read().lower()
                words = set(text.split())
                for word in words:
                    if word not in index:
                        index[word] = []
                    index[word].append(filename)
    return index

if __name__ == "__main__":
    index = build_index(DATA_DIR)
    with open(INDEX_FILE, "w", encoding="utf-8") as f:
        json.dump(index, f, indent=4)
    print(f"Index built and saved to {INDEX_FILE}")
