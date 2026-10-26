from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS


class Embedding:

    def __init__(self, chunks):
        self.chunks = chunks

    def create_embeddings(self):

        embeddings = GoogleGenerativeAIEmbeddings(
            model="gemini-embedding-001"
        )

        vectorstore = FAISS.from_documents(
            self.chunks,
            embeddings
        )

        return vectorstore