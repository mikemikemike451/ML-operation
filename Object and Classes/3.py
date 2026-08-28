class MulticlassEvaluator:

    def __init__(self, labels):
        self.labels = labels
        self.confusion_matrix = {}
        for label in labels:
            self.confusion_matrix[label] = {x: 0 for x in labels}

    def update(self, y_true_batch, y_pred_batch):
        for i in range(len(y_true_batch)):
            self.confusion_matrix[y_true_batch[i]][y_pred_batch[i]] += 1

    def precision(self, label):
        count = 0
        for i in self.labels:
            count += self.confusion_matrix[i][label]

        if count == 0:
            return 'NA'

        ans = self.confusion_matrix[label][label] / count
        return ans


A  = MulticlassEvaluator(['A', 'B', 'C'])
A.update(['A', 'A', 'B', 'C'],['A', 'B', 'B', 'A'])
print(A.precision('C'))