import nltk
from transformers import AutoTokenizer, AutoModel
import torch

# Ensure the 'punkt' tokenizer is available
nltk.download('punkt')

# Load the tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("sentence-transformers/all-MiniLM-L6-v2")
model = AutoModel.from_pretrained("sentence-transformers/all-MiniLM-L6-v2")

def embed_text(text):
    sentences = nltk.sent_tokenize(text)
    inputs = tokenizer(sentences, padding=True, truncation=True, return_tensors="pt")
    with torch.no_grad():
        embeddings = model(**inputs).last_hidden_state.mean(dim=1)
    return sentences, embeddings.numpy()
