import json
import time
import numpy as np
from pathlib import Path
from sentence_transformers import SentenceTransformer
import pickle
import faiss


def get_data():
    p = Path(__file__).with_name('clean.json')
    with p.open('r', encoding='utf-8') as f:
        return json.load(f)


def get_data_list_for_ids(ids, data, scores):
    lst = []
    for i, id in enumerate(ids):
        lst.append({
            "title": data[id]["title"][1:],
            "url": data[id]["url"],
            "about": data[id]["about"],
            "stars": data[id]["stars"],
            "score": float(scores[i])
        })
    return lst


def get_predictions(model, index, data, description):
    X_pred = description
    if X_pred == "" or X_pred is None:
        return None
    query_vector = model.encode([description])
    k = 10
    top_k = index.search(query_vector, k)
    return get_data_list_for_ids(ids=top_k[1].tolist()[0],
                                 data=data,
                                 scores=top_k[0][0])


def make_embeddings():
    data = get_data()
    texts = []
    for elem in data:
        current_text = elem['description']
        texts.append(current_text)

    model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
    embeddings = model.encode(texts, show_progress_bar=True)
    embeddings_path = "all-MiniLM-L6-v2_embeddings.pkl"
    with open(embeddings_path, "wb") as fOut:
        pickle.dump({'sentences': texts, 'embeddings': embeddings},
                    fOut, protocol=pickle.HIGHEST_PROTOCOL)


def load_embeddings():
    embeddings_path = "all-MiniLM-L6-v2_embeddings.pkl"
    with open(embeddings_path, "rb") as fIn:
        cache_data = pickle.load(fIn)
        corpus_sentences = cache_data['sentences']
        corpus_embeddings = cache_data['embeddings']
    return corpus_sentences, corpus_embeddings


def create_faiss_index(embeddings):
    index = faiss.IndexIDMap(faiss.IndexFlatIP(384))
    index.add_with_ids(embeddings, np.array(range(0, len(embeddings))))
    faiss.write_index(index, 'github_repos.index')
    return index


if __name__ == '__main__':
    start_time = time.time()
    make_embeddings()
    data = get_data()
    sentences, embeddings = load_embeddings()
    index = create_faiss_index(embeddings)
    print("Finished in --- %s seconds ---" % int(time.time() - start_time))
