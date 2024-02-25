import streamlit as st
from Chat import get_response
# from langchain_community.vectorstores import FAISS
# from Config import config
# from google.ai.generativelanguage_v1beta.services.discuss_service.client import DiscussServiceAsyncClient



# def get_response(user_question):
#     chain, embeddings = config()
#     new_db = FAISS.load_local("faiss_index", embeddings)
#     docs = new_db.similarity_search(user_question)
#     response = chain.invoke({"input_documents": docs, "question": user_question}, return_only_outputs=True)
#     return response['output_text']

user_input = st.text_input("Enter your message:")
if st.button("Send"):
    # Process the user input and generate a response
    response = get_response(user_input)
    st.write("hello world!")