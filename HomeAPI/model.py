from sklearn.linear_model import LogisticRegression
import pickle

def clf_model(X_train, y_train):
    clf=LogisticRegression()
    clf.fit(X_train, y_train)
    pickle.dump(clf, open('LRClassifier.pkl', 'wb'))

    
