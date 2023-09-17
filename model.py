import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import pickle

#loading data
df = pd.read_csv('data_pre.csv')

#splitting data
X = df.drop(['Attack Type'], axis = 1)
y = df['Attack Type']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.33, random_state = 42,shuffle=True)

#scaling data
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

#training model
lg = LogisticRegression(max_iter = 1200000)
lg.fit(X_train, y_train)

#saving model
pickle.dump(lg, open('model.pkl','wb'))