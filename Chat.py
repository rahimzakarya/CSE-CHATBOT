from langchain_community.vectorstores import FAISS
from Config import config

def get_response(user_question):
    chain, embeddings = config()
    new_db = FAISS.load_local("faiss_index", embeddings)
    docs = new_db.similarity_search(user_question)
    response = chain.invoke({"input_documents": docs, "question": user_question}, return_only_outputs=True)
    return response['output_text']

