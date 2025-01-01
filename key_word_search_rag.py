import re 

class BasicRAG: 
    def __init__(self):
        self.documents = []

    # Add documents 
    def add_documents(self, document):
        self.documents.append(document)
    
    # Search 
    def search(self, query):
        results = []
        for doc in self.documents:
            if re.search(query.lower, doc.lower):
                results.append(doc)

        return results

def main():
    rag = BasicRAG()

    rag.add_documents("C is a popular programming language")
    rag.add_documents("Machine learning uses python extensively ")
    rag.add_documents("Data science relies on python an it libraries")


if __name__ == "__main__":
    main()