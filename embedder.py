import nltk
from transformers import AutoTokenizer, AutoModel
import torch
from sklearn.metrics.pairwise import cosine_similarity
from law_keywords import law_keywords


class Embedder():

    def __init__(self, config):
        # Load the tokenizer and model
        self.tokenizer = AutoTokenizer.from_pretrained(config['tokenizer'])
        self.embedding_model = AutoModel.from_pretrained(config["embedding_model"])

    def filter_and_embed_text(self, text, legal_area):
        sentences = nltk.sent_tokenize(text)
        relevant_sentences = self.filter_sentences(sentences, legal_area)
        inputs = self.tokenizer(relevant_sentences, padding=True, truncation=True, return_tensors="pt")
        with torch.no_grad():
            embeddings = self.embedding_model(**inputs).last_hidden_state.mean(dim=1)
        return sentences, embeddings.numpy()

    def find_similar_sentences(self, embeddings1, embeddings2, threshold=0.75):
        similarities = cosine_similarity(embeddings1, embeddings2)
        similar_pairs = []
        for i, row in enumerate(similarities):
            for j, sim in enumerate(row):
                if sim > threshold:
                    similar_pairs.append((i, j, sim))
        return similar_pairs

    def filter_sentences(self, sentences, legal_area):
        keywords: list = law_keywords[legal_area]
        relevant_sentences = []
        for sentence in sentences:
            if any(keyword in sentence.lower() for keyword in keywords):
                relevant_sentences.append(sentence)
        return relevant_sentences


