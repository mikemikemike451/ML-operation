class SparseVector:
    def __init__(self,dim):
        self.dim = dim        
        self.vector = dict()
    
    def set_item (self , idx , val):
        if val != 0:
            self.vector[idx] = val
    
    def get_item (self, idx):
        return self.vector.get(idx, 0)

    def dot(self, other):
        dot = 0
        for item in self.vector:
            if item in other.vector:
                dot += self.vector[item] * other.vector[item]
        return dot
