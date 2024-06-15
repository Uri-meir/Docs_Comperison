from sklearn.metrics.pairwise import cosine_similarity


def compare_documents(embeddings1, embeddings2, sentences1, sentences2, threshold=0.8):
    """
    Compare two sets of embeddings and return similar and different sentences.

    :param embeddings1: List of embeddings for the first document
    :param embeddings2: List of embeddings for the second document
    :param sentences1: List of sentences for the first document
    :param sentences2: List of sentences for the second document
    :param threshold: Similarity threshold to consider sentences as similar
    :return: Tuple containing lists of similar and different sentences
    """
    similarities = cosine_similarity(embeddings1, embeddings2)
    similar_sentences = []
    different_sentences = []

    for i, sim_row in enumerate(similarities):
        max_sim = max(sim_row)
        if max_sim >= threshold:
            similar_sentences.append((sentences1[i], sentences2[sim_row.argmax()]))
        else:
            different_sentences.append((sentences1[i], sentences2[sim_row.argmax()]))
    return similar_sentences, different_sentences
