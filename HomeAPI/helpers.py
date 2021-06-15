from sklearn.model_selection import train_test_split
from query import load_data

def split_df(data):
    array=data.values
    X=array[:,:-1]
    y=array[:,-1]

    X_train, X_test, y_train, y_test=train_test_split(X,y, test_size=0.2, random_state=1, shuffle=True)

    return X_train, X_test, y_train, y_test

df=load_data()
X_train, X_test, y_train, y_test=split_df(df)