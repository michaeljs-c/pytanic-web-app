import numpy as np
import pickle

def predict(age, fare, title, pclass, sex, sibsp, parch, embarked):
    print("-------------------=-=-=-",fare)
    cat_cols = [title, int(pclass), sex, int(sibsp), int(parch), embarked]
    cont_cols = [int(age), float(fare)]
    with open('encoder', 'rb') as f:
        encoder = pickle.load(f)
    with open('titanic_model.pickle', 'rb') as f:
        model = pickle.load(f)
    X = encoder.transform([cat_cols]).toarray()
    X = [np.append(cont_cols, X)]
    pred = model.predict(X)[0]
    proba = round(100 * model.predict_proba(X)[0][1])
    return pred, proba


