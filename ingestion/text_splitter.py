from langchain_text_splitters import RecursiveCharacterTextSplitter
class TextSplitter:

    def __init__(self, documents):
        self.documents = documents

    def split(self):

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=50
        )

        chunks = splitter.split_documents(self.documents)

        return chunks
