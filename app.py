import streamlit as st
from document_reader import read_document
from embedder import embed_text
from comparer import compare_documents

st.title("Document Comparison App")
st.write("Upload two documents to compare their similarities and differences.")

doc1 = st.file_uploader("Choose the first document", type=["pdf", "docx", "txt"])
doc2 = st.file_uploader("Choose the second document", type=["pdf", "docx", "txt"])

if doc1 and doc2:
    text1 = read_document(doc1)
    text2 = read_document(doc2)

    sentences1, embeddings1 = embed_text(text1)
    sentences2, embeddings2 = embed_text(text2)

    similar_sentences, different_sentences = compare_documents(embeddings1, embeddings2, sentences1, sentences2)

    st.write("### Similarities:")
    for sent1, sent2 in similar_sentences:
        st.write(f"Document 1: {sent1}")
        st.write(f"Document 2: {sent2}")
        st.write("----")

    st.write("### Differences:")
    for sent in different_sentences:
        st.write(f"Document 1: {sent}")
