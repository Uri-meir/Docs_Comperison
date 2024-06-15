import os
from law_keywords import law_keywords
import streamlit as st
from document_reader import read_document
from embedder import Embedder
from llm import LanguageModel
from config import load_config
from comparer import compare_documents

@st.cache_resource
def start_app():
    config_path = os.getenv('CONFIG_PATH')
    config = load_config(config_path)
    embedder = Embedder(config)
    llm = LanguageModel(config)
    return embedder, llm

embedder, llm = start_app()
legal_areas = list(law_keywords.keys())
st.title("Document Comparison App")
st.write("Upload two documents to compare their similarities and differences.")
doc1 = st.file_uploader("Choose the first document", type=["pdf", "docx", "txt"])
doc2 = st.file_uploader("Choose the second document", type=["pdf", "docx", "txt"])



if doc1 and doc2:
    text1 = read_document(doc1)
    legal_area1 = llm.ask_doc_type(text1)
    if legal_area1 == "unknown":
        legal_area1 = st.selectbox("Legal area of Document 1:", legal_areas)
    text2 = read_document(doc2)
    legal_area2 = llm.ask_doc_type(text2)
    if legal_area2 == "unknown":
        legal_area2 = st.selectbox("Legal area of Document 2:", legal_areas)
    st.write("legal_area1 : ", legal_area1,"legal_area2 : ", legal_area2)
    with st.spinner("Embedding documents..."):
        sentences1, embeddings1 = embedder.filter_and_embed_text(text1, legal_area1)
        sentences2, embeddings2 = embedder.filter_and_embed_text(text2, legal_area2)

    similar_sentences, different_sentences = compare_documents(embeddings1, embeddings2, sentences1, sentences2)

    st.write("### Similarities:")
    for sent1, sent2 in similar_sentences:
        explanation = llm.explain_similarity(sent1, sent2)
        st.write(f"**Explanation:** {explanation}")
        with st.expander("Show context from docs"):
            st.write(f"Document 1: {sent1}")
            st.write(f"Document 2: {sent2}")

        st.write("----")

    st.write("### Differences:")
    for sent1, sent2 in different_sentences:
        explanation = llm.explain_similarity(sent1, sent2)
        st.write(f"**Explanation:** {explanation}")
        with st.expander("Show context from docs"):
            st.write(f"Document 1: {sent1}")
            st.write(f"Document 2: {sent2}")
