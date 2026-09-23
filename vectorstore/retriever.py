class Retriever:

    def __init__(self, vectorstore):
        self.vectorstore = vectorstore

    def get_retriever(self):

        retriever = self.vectorstore.as_retriever(
            search_kwargs={"k": 2}
        )

        return retriever