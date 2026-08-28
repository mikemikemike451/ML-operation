class DirectedGraph:
    def __init__(self):
        self.dict = {}
    
    def add_edge (self, src, dest):
        if src not in self.dict:
            self.dict[src] = {dest}
        else:
            self.dict[src].add(dest)

    def get_out_degree (self, node):
        ans = self.dict.get(node, 0)
        if ans != 0:
            return len(ans)
        else:
            return 0

    def get_neighbors (self, node):
        ans = self.dict.get(node, 0)
        return ans

