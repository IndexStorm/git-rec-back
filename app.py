import json

import faiss
from flask import Flask, request
from flask_cors import CORS, cross_origin
from prometheus_flask_exporter import PrometheusMetrics
from sentence_transformers import SentenceTransformer
from embeddings.sbert import get_predictions, get_data

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
data = get_data()
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
index = faiss.read_index("embeddings/github_repos.index")
metrics = PrometheusMetrics(app)


@app.route("/", methods=['GET'])
def welcome():
    return "Welcome to GitHub Recommendations public beta 0.2"


@app.route("/similar", methods=['POST'])
@cross_origin()
def similarity_route():
    request_data = request.get_json()
    description = request_data.get("description")
    url = request_data.get("url")
    if description is None or type(url) is not str:
        return "Wrong args", 400
    preds = get_predictions(
        model=model, index=index, data=data, description=description)
    if preds is None:
        return "No prediction", 500
    for i in range(len(preds)):
        if url.lower() in preds[i]["url"].lower():
            del preds[i]
            break
    response = app.response_class(
        response=json.dumps(preds),
        status=200,
        mimetype='application/json'
    )
    return response


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000, debug=True)
