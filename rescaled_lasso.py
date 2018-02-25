import pandas as pd
import numpy as np
from sklearn import metrics
from sklearn import linear_model
from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import MinMaxScaler

df = pd.read_csv('data.csv',index_col=0)
y = df['IR']
x = df[['GDP','UR','CPI','NFP','NHS','CU','CCI','NAPM', 'UNL','RS']]
#y = y.astype('int')
scaler = MinMaxScaler(feature_range=(0, 1))
rescaledX = scaler.fit_transform(x)
x = rescaledX
#train test split
X_train, X_test, y_train, y_test = train_test_split(x,y, test_size = 0.3)

reg = linear_model.Lasso(alpha = 0.1)
reg.fit(X_train, y_train)
print(x)
ytest_pred = reg.predict(X_test)
print(ytest_pred)

#print("alpha_ ", reg.alpha_)
#print("Intercept= ", reg.intercept_)
#print("Coeff= ", reg.coef_)