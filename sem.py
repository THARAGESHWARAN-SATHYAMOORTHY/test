import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import VotingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

df = pd.read_csv("/content/data.csv")

print(df.shape)

print("S.No     ColumnName                              DataType")
for i,(j,k) in enumerate(df.dtypes.items(),start=1):
  print(f'{i:<9}{j:<40}{k}')

df.isna().sum()

df.drop(columns=["Unnamed: 32"], inplace=True)
df['area_mean'].fillna(df['area_mean'].mean(), inplace=True)

df.isna().sum()

le = LabelEncoder()

df= df.drop(["id"], axis = 1)
y = df["diagnosis"].values
y = le.fit_transform(y)
X = df.drop(["diagnosis"], axis = 1).values
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=42)

tree = DecisionTreeClassifier(
          max_depth=10,
          random_state=42)
tree = tree.fit(X_train, y_train)
y_train_pred = tree.predict(X_train)
y_test_pred = tree.predict(X_test)
tree_train = accuracy_score(y_train, y_train_pred)
tree_test = accuracy_score(y_test, y_test_pred)
print(f'Decision tree train/test accuracies: {tree_train:.4f}/{tree_test:.4f}')

print(tree.predict([[17.99,10.38,122.8,1001,0.1184,0.2776,0.3001,0.1471,0.2419,0.07871,1.095,0.9053,8.589,153.4,0.006399,0.04904,0.05373,0.01587,0.03003,0.006193,25.38,17.33,184.6,2019,0.1622,0.6656,0.7119,0.2654,0.4601,0.1189]])[0])

ada = AdaBoostClassifier(
           estimator=tree,
           n_estimators=500,
           learning_rate=0.5,
           random_state=42)
ada = ada.fit(X_train, y_train)
y_train_pred = ada.predict(X_train)
y_test_pred = ada.predict(X_test)
ada_train = accuracy_score(y_train, y_train_pred)
ada_test = accuracy_score(y_test, y_test_pred)
print(f'Adaboost train/test accuracies: {ada_train:.3f}/{ada_test:.3f}')

print(ada.predict([[17.99,10.38,122.8,1001,0.1184,0.2776,0.3001,0.1471,0.2419,0.07871,1.095,0.9053,8.589,153.4,0.006399,0.04904,0.05373,0.01587,0.03003,0.006193,25.38,17.33,184.6,2019,0.1622,0.6656,0.7119,0.2654,0.4601,0.1189]])[0])

logistic = LogisticRegression(max_iter=1000, solver='liblinear')
knearest = KNeighborsClassifier(n_neighbors = 6)

voting = VotingClassifier(estimators = [('LR', logistic), ('KNN', knearest)], voting = 'soft')
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 100)
voting.fit(X_train, y_train)
predicted = voting.predict(X_test)
accuracy_voting = accuracy_score(predicted, y_test)

models = [logistic, knearest]
for model in models:
    model.fit(X_train, y_train)
    predicted = model.predict(X_test)
    accuracy = accuracy_score(predicted, y_test)
    model_name = model.__class__.__name__
    print(f'{model_name}: {accuracy:.4f}')

print(f'Voting accuracy score:{accuracy_voting:.4f}')

print(voting.predict([[17.99,10.38,122.8,1001,0.1184,0.2776,0.3001,0.1471,0.2419,0.07871,1.095,0.9053,8.589,153.4,0.006399,0.04904,0.05373,0.01587,0.03003,0.006193,25.38,17.33,184.6,2019,0.1622,0.6656,0.7119,0.2654,0.4601,0.1189]])[0])
