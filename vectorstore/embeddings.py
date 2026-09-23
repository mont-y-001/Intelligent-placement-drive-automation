from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS


class Embedding:

    def __init__(self, chunks):
        self.chunks = chunks

    def create_embeddings(self):

        embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )

        vectorstore = FAISS.from_documents(
            self.chunks,
            embeddings
        )

        return vectorstore