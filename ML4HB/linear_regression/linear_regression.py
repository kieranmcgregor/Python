import numpy as np
import matplotlib.pyplot as plt
import csv

def load_dataset():
    num_rows = sum(1 for line in open('dataset_Facebook.csv')) - 1
    X = np.zeros((num_rows, 1))
    y = np.zeros((num_rows, 1))
    with open('dataset_Facebook.csv') as f:
        reader = csv.DictReader(f, delimiter=';')
        next(reader, None)
        for i, row in enumerate(reader):
            X[i] = int(row['share']) if len(row['share']) > 0 else 0
            y[i] = int(row['like'])  if len(row['like']) > 0 else 0
    return X, y

def visualize_dataset(X, y):
    plt.xlabel('Number of shares')
    plt.ylabel('Number of likes')
    plt.scatter(X, y)
    plt.show()

def visualize_solution(X, y, lin_reg):
    plt.xlabel('Number of shares')
    plt.ylabel('Number of likes')
    plt.scatter(X, y)

    x = np.arange(0, 800)
    y = lin_reg.predict(x)
    plt.plot(x, y, 'r--', label='r = %.2f' % lin_reg.rho)
    plt.legend()

    plt.show()    

class LinearRegression(object):
    """Implements linear regression"""
    def __init__(self):
        self.w = 0
        self.b = 0
        self.rho = 0

    def fit(self, X, y):
        mean_x = X.mean()
        mean_y = y.mean()
        errors_x = X - mean_x
        errors_y = y - mean_y
        errors_product_xy = np.sum(np.multiply(errors_x, errors_y))
        squared_errors_x = np.sum(errors_x ** 2)

        self.w = errors_product_xy / squared_errors_x
        self.b = mean_y - self.w * mean_x

        N = len(X)
        std_x = X.std()
        std_y = y.std()
        cov = errors_product_xy / N
        self.rho = cov / (std_x * std_y)

    def predict(self, X):
        return self.w * X + self.b

if __name__ == '__main__':
    X, y = load_dataset()
    lin_reg = LinearRegression()
    lin_reg.fit(X, y)
    
    visualize_solution(X, y, lin_reg)
