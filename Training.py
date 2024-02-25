from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from Config import config
from langchain_community.vectorstores import FAISS
import streamlit as st

st.title("PDF Files Upload:")
pdf_docs = st.file_uploader("Upload your PDF Files and Click on the Submit Button",accept_multiple_files=True)
if st.button("Submit and Train"):
    with st.spinner("Processing & Training..."):
        raw_text = ""
        for pdf in pdf_docs:
            pdf_reader = PdfReader(pdf)
            for page in pdf_reader.pages:
                raw_text += page.extract_text()
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=1000)
        text_chunks = text_splitter.split_text(raw_text)
        chain, embeddings = config()
        vector_store = FAISS.from_texts(text_chunks, embedding=embeddings)
        vector_store.save_local("faiss_index")
        st.success("Done")