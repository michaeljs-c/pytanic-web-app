import pandas as pd
import pickle
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

def get_title(name):
    return name[name.index(",")+1: name.index(".")].strip()

train = pd.read_csv('train.csv')
train["Title"] = train.Name.map(get_title)
train["Age"] = train.Age.fillna(train.Age.mean())
train["Embarked"] = train.Embarked.fillna('mode')
X = train.drop(['Survived', 'Cabin', 'Name', 'Ticket', 'PassengerId'], axis=1)
y = train.Survived

cat_cols = ['Title','Pclass','Sex','SibSp','Parch','Embarked']
encoder = OneHotEncoder().fit(X[cat_cols])
encoded_cols = encoder.transform(X[cat_cols])
encoded_df = pd.DataFrame(encoded_cols.toarray(), columns=encoder.get_feature_names_out(cat_cols))
X_encoded = pd.concat([X.drop(cat_cols, axis=1), encoded_df], axis=1)


X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, random_state=42)
rf = RandomForestClassifier()
rf.fit(X_train, y_train)

with open('titanic_model.pickle', 'wb') as f:
    pickle.dump(rf, f)
with open('encoder', 'wb') as f:
    pickle.dump(encoder, f)