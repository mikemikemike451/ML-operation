class DocumentIndexer:
    
    def __init__(self):
        self.dict = {}
    
    def add_document (self, doc_id, text):
        textlist = text.split()
        for i in textlist:
            if i not in self.dict:
                self.dict[i] = {doc_id} 
            else:
                self.dict[i].add(doc_id)

    def boolean_search (self, query_terms, mode ="AND"):
        set0 = self.dict[query_terms[0]]
        for i in range(1,len(query_terms)):
            set_i = self.dict[query_terms[i]]
            set0 = set0.intersection(set_i)
        return set0

indexer = DocumentIndexer()
indexer.add_document(1, "apple banana")
indexer.add_document(2, "apple orange")
indexer.add_document(3, "banana orange")

query_terms = ["apple", "banana"]

print(indexer.boolean_search(query_terms, "AND"))
