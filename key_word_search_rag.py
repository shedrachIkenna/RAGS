import re 

class BasicRAG: 
    def __init__(self):
        self.documents = []

    def add_documents(self, document):
        self.documents.append(document)
    

    def search(self, query):
        results = []
        for doc in self.documents:
            if re.search(query.lower, doc.lower):
                results.append(doc)

        return results