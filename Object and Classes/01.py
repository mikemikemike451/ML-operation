import math

class OnlineStandardScaler:
    def __init__(self, num_features):
        self.num_features = num_features
        self.n = 0
        self.mean = [0] * num_features
        self.M2 = [0] * num_features

    def partial_fit (self , X_batch ):
        for row in X_batch:
            self.n += 1

            for j in range(self.num_features):
                x = row[j]

                delta = x - self.mean[j]
                self.mean[j] += delta / self.n

                delta2 = x - self.mean[j]
                self.M2[j] += delta * delta2

    def transform(self, X_batch):
        result = []

        for row in X_batch:
            new_row = []

            for j in range(self.num_features):
                variance = self.M2[j] / self.n if self.n > 0 else 0
                std = math.sqrt(variance)
                print(variance)

                if std == 0:
                    new_row.append(0.0)
                else:
                    new_row.append((row[j] - self.mean[j]) / std)

            result.append(new_row)
        return result

scaler = OnlineStandardScaler(2)

scaler.partial_fit([
    [1, 10],
    [3, 20]
])

print(scaler.transform([[5, 30]]))
print(scaler.mean, scaler.M2)