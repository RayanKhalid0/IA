import numpy as np
import pandas as pd
from sklearn.ensemble import AdaBoostClassifier, GradientBoostingClassifier, RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import GridSearchCV


def model(path):
    filename = path
    # df = pd.read_csv("TestModelling.csv")
    df = pd.read_csv(filename)

    print(df)

    predict = pd.DataFrame(columns=df.columns)

    for index, row in df.iterrows():

        if pd.isnull(row.iloc[-1]):

            predict = pd.concat([predict, row.to_frame().T])

    print(predict)

    df.dropna(subset=[df.columns[-1]], inplace=True)

    print(df)

    X = df.iloc[:, :-1]
    Y = df.iloc[:, -1]

    target = df.columns[-1]
    print(target)

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.4)

    classifiers = {
        "Random Forest": RandomForestClassifier(),
        "SVC": make_pipeline(StandardScaler(), SVC(kernel='linear', C=3)),
        "Decision Tree": DecisionTreeClassifier(),
        "K-Nearest Neighbors": make_pipeline(StandardScaler(), KNeighborsClassifier(n_neighbors=3)),
        "AdaBoost": AdaBoostClassifier(),
        "Gradient Boosting": GradientBoostingClassifier(),
        "Logistic Regression": LogisticRegression(),
        "Gaussian Naive Bayes": GaussianNB(),
        "Multi-layer Perceptron": MLPClassifier(),
        "SVM with RBF Kernel": SVC(kernel='rbf')
    }


    param_grid = {
        "Random Forest": {
            "n_estimators": [50, 100, 200],
            "max_depth": [None, 10, 20]
        },
        "SVC": {
            "svc__C": [0.1, 1, 10],
            "svc__gamma": [0.1, 0.01, 0.001]
        },
        "Decision Tree": {
            "max_depth": [None, 10, 20]
        },
        "K-Nearest Neighbors": {
            "kneighborsclassifier__n_neighbors": [3, 5, 7]
        },
        "AdaBoost": {
            "n_estimators": [50, 100, 200],
            "learning_rate": [0.01, 0.1, 1.0]
        },
        "Gradient Boosting": {
            "n_estimators": [50, 100, 200],
            "learning_rate": [0.01, 0.1, 1.0],
            "max_depth": [3, 5, 7]
        },
        "Logistic Regression": {
            "C": [0.1, 1, 10]
        },
        "Gaussian Naive Bayes": {},
        "Multi-layer Perceptron": {
            "hidden_layer_sizes": [(50,), (100,), (200,)],
            "activation": ['relu', 'tanh']
        },
        "SVM with RBF Kernel": {
            "C": [0.1, 1, 10],
            "gamma": [0.1, 0.01, 0.001]
        }
    }

    best_model = None
    high = -np.inf

    for name, clf in classifiers.items():
        if name in param_grid:
            print(f"Tuning hyperparameters for {name}...")
            grid_search = GridSearchCV(clf, param_grid[name], cv=5, scoring='accuracy')
            grid_search.fit(X_train, Y_train)
            best_params = grid_search.best_params_
            best_score = grid_search.best_score_
            clf.set_params(**best_params)
            clf.fit(X_train, Y_train)
            accuracy = clf.score(X_test, Y_test) * 100

            if accuracy > high:
                best_model = clf
                high = accuracy
                if accuracy >= 80:
                    break


            print(f"Best parameters: {best_params}")
            print(f"Training accuracy: {best_score:.2f}%")
            print(f"Test accuracy with best parameters: {accuracy:.2f}%")
            print()


        else:
            clf.fit(X_train, Y_train)
            accuracy = clf.score(X_test, Y_test) * 100
            print(f"Model accuracy with {name}: {accuracy:.2f}%")

    predict_X = predict.iloc[:, :-1]
    predict_Y = (best_model.predict(predict_X))
    print(predict_Y)

    predict[target] = predict_Y

    print(predict)
    product = [high, predict]

    Final = pd.concat([df, predict])

    print(Final)

    Final.to_csv(filename, index=False)
    return product


def M():
    return "MMM"


print(model("StressLevelDataset.csv"))

