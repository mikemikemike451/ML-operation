class TreeNode:
    def __init__ (self, feature_idx, threshold, left, right, value):
        self._feature_idx = feature_idx
        self._threshold = threshold
        self._left = left
        self._right = right
        self._value = value
        
    def predict (self, x):
        if self._value is not None:
            return self._value
        if x[self._feature_idx] < self._threshold:
            return self._left.predict(x)
        else:
            return self._right.predict(x)

left_leaf = TreeNode(None, None, None, None, "Cat")
right_leaf = TreeNode(None, None, None, None, "Dog")

root = TreeNode(
    0, # 第 0 個條件 對應到x[0] 
    5,
    left_leaf,
    right_leaf,
    None
)

print(root.predict([3]))
print(root.predict([8]))