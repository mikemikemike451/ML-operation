class CategoricalEncoder:
    def __init__(self):
        self.dict = {"<UNK>": 0}
    
    def fit(self, categories):
        index = 1
        for i in categories:
            if i not in self.dict:
                self.dict[i] = index
                index += 1
    
    def transform (self, data):
        ans = []
        for i in data:
            index = self.dict.get(i, 0)
            ans.append(index)
        return ans
