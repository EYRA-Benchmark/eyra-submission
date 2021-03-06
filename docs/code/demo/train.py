import os

import pandas as pd

from pathlib import Path
from joblib import dump

from sklearn import svm


def train_svm(in_file):
    """Train Support Vector Machines for the EYRA Demo Benchmark.
    """

    # Read the training file
    train = pd.read_csv(in_file)

    train_data = train[['sepal_length', 'sepal_width', 'petal_length',
                        'petal_width']].values
    train_targets = list(train['class'])

    # Train the classifier
    clf = svm.SVC(gamma=0.001, C=100.)
    clf.fit(train_data, train_targets)

    return clf


def save_model(clf, path):
    dump(clf, path)


def predict(clf, test_data_file):
    test = pd.read_csv(test_data_file)

    return clf.predict(test.values)

if __name__ == "__main__":
    # Create the model using a local copy of the data by typing:
    # python model_creation/train.py
    root = Path(__file__).absolute().parent.parent

    participant_data = Path(root)/'data'/'iris_participant_data.csv'
    out_file = Path(root)/'model_creation'/'iris_svm_model'

    clf = train_svm(str(participant_data))
    save_model(clf, str(out_file))

    # Test whether the prediction mechanics work
    test_file = root/'data'/'iris_public_test_data.csv'
    result = predict(clf, str(test_file))
    print(result)
