import pandas as pd

def load_data():
    url="https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
    names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
    dataset = pd.read_csv(filepath_or_buffer=url,header=None,sep=',',names=names)
    return dataset
