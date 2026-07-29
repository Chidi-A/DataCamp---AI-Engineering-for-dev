# ── 1. Imports & setup ────────────────────────────────────────────────────────
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from openai import OpenAI
from scipy.spatial import distance
from sklearn.manifold import TSNE

# Replace with your actual key, or set OPENAI_API_KEY as an env variable
client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

# ── 2. Reusable embedding helper ──────────────────────────────────────────────
def create_embeddings(texts):
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=texts
    )
    response_dict = response.model_dump()
    return [data["embedding"] for data in response_dict["data"]]

# ── 3. Load the dataset ───────────────────────────────────────────────────────
reviews = pd.read_csv("womens_clothing_e-commerce_reviews.csv")
reviews.head()

# ── 4. Create and store embeddings ────────────────────────────────────────────
reviews_clean = reviews.dropna(subset=["Review Text"]).reset_index(drop=True)
review_texts = reviews_clean["Review Text"].tolist()

# Batch embed all reviews in one API call
response = client.embeddings.create(
    model="text-embedding-3-small",
    input=review_texts
)
response_dict = response.model_dump()
embeddings = [item["embedding"] for item in response_dict["data"]]

print(f"Number of embeddings: {len(embeddings)}")
print(f"Embedding dimensions: {len(embeddings[0])}")

# ── 5. Dimensionality reduction & visualization ───────────────────────────────
tsne = TSNE(n_components=2, perplexity=50, random_state=42)
embeddings_2d = tsne.fit_transform(np.array(embeddings))

plt.figure(figsize=(12, 8))
plt.scatter(embeddings_2d[:, 0], embeddings_2d[:, 1], alpha=0.4, s=8)
plt.title("2D Visualization of Clothing Review Embeddings (t-SNE)")
plt.xlabel("t-SNE Dimension 1")
plt.ylabel("t-SNE Dimension 2")
plt.show()

# ── 6. Feedback categorization by topic ──────────────────────────────────────
topics = ["quality", "fit", "style", "comfort", "price", "sizing", "delivery"]
topic_embeddings = create_embeddings(topics)

def classify_review(review_embedding, topic_embeddings, topics):
    distances = [
        {"topic": topic, "distance": distance.cosine(review_embedding, topic_embeddings[i])}
        for i, topic in enumerate(topics)
    ]
    return min(distances, key=lambda x: x["distance"])["topic"]

reviews_clean["topic"] = [
    classify_review(emb, topic_embeddings, topics)
    for emb in embeddings
]

print(reviews_clean["topic"].value_counts())

# ── 7. Similarity search ──────────────────────────────────────────────────────
def find_n_closest(query_vector, embeddings, n=3):
    distances = []
    for index, embedding in enumerate(embeddings):
        dist = distance.cosine(query_vector, embedding)
        distances.append({"distance": dist, "index": index})
    distances_sorted = sorted(distances, key=lambda x: x["distance"])
    # Skip index 0 — it's the query review itself (distance ≈ 0)
    return distances_sorted[1:n+1]

first_review = "Absolutely wonderful - silky and sexy and comfortable"
query_vector = create_embeddings(first_review)[0]

hits = find_n_closest(query_vector, embeddings, n=3)
most_similar_reviews = [review_texts[hit["index"]] for hit in hits]

print(f'\nQuery: "{first_review}"\n')
for i, review in enumerate(most_similar_reviews, 1):
    print(f"{i}. {review}")