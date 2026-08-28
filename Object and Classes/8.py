import math

class CentroidManager:
    def __init__(self):
        self.dict = {}
    
    def update_centroid(self, cluster_id, coords):
        self.dict[cluster_id] = coords
    
    def closest_centroid(self, point):
        closest = None
        min_dist = float("inf")

        for cluster_id in self.dict:
            dist = math.sqrt(
                sum((a - b) ** 2 for a, b in zip(point, self.dict[cluster_id]))
            )

            if dist < min_dist:
                min_dist = dist
                closest = cluster_id

        return closest


