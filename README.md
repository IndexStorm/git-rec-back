# GitHub Recommendations Backend

<img src="https://user-images.githubusercontent.com/23217571/183360309-4ae85889-de22-4360-b946-3e79d019ba69.jpg" 
data-canonical-src="https://user-images.githubusercontent.com/23217571/183360309-4ae85889-de22-4360-b946-3e79d019ba69.jpg" width="200" height="200" />

This is an official repository for the backend part of <a href="https://chrome.google.com/webstore/detail/github-recommender/hbiichfklkmlebacdfhkojcpmmakmamk">GitHub Recommender extension</a>

<h2>Repository with extension code</h2>

<a href="https://github.com/IndexStorm/git-rec-ext">indexStorm/git-rec-ext</a>

## Motivation

We find it hard to explore the world of GitHub repositories and are afraid of missing out some useful repos. That is why we decided to build this extension to help people to discover new horizons of hidden GitHub gems.

Once you've loaded the GitHub repo page, the extension adds a list of similar repositories based on their titles and descriptions. We do not collect any data and open source this product to everyone.


## Explanation

Using [SBERT](https://github.com/UKPLab/sentence-transformers) embeddings and scrapped repo's descriptions we have constructed vector embeddings for over 100,000 repositories. Once the client sends the description of the current repo, we construct a vector from it and then search for the nearest embeddings in the vector space. You can read more about [vector cosine similarity](https://www.pinecone.io/learn/vector-embeddings/). Constructed embeddings and scrapped repo's descriptions can be shared upon request.

## Tech/frameworks used
The backend was built on **Python 3.9** using: 
- [Flask](https://github.com/pallets/flask) for server
- [SBERT](https://github.com/UKPLab/sentence-transformers) for building repo's embeddings
- [FAISS](https://github.com/facebookresearch/faiss) for fast cosine similarity search


<h3>Made by <a href="https://indexstorm.com/">indexStorm</a></h3>

<h3>Follow on <a href="https://twitter.com/index_storm">Twitter @index_storm</a></h3>

<h3>Authors:</h3>

- <a href="https://github.com/ovyan">Mike</a>
- <a href="https://github.com/own2pwn">Evgeniy</a>

<p align="middle">
<a href="https://indexstorm.com/"><img src="https://user-images.githubusercontent.com/23217571/183392524-2a566828-f567-4b08-b218-f97a905954b2.png" 
data-canonical-src="https://user-images.githubusercontent.com/23217571/183392524-2a566828-f567-4b08-b218-f97a905954b2.png" width="200" height="200" />
</a>
</p>
