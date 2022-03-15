import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df = pd.read_csv('./student_scores.csv')

# print(df.shape)
# print(df.head(5))
# print(df.describe())

# df.plot(x='Hours', y='Scores', style='o')
# plt.title('Hours vs. Percentage')
# plt.xlabel('Hours Studied')
# plt.ylabel('Percentage Scored')
# plt.show()

X = df.iloc[:, :-1].values
y = df.iloc[:, 1].values

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=0)

regressor = LinearRegression()
regressor.fit(X_train, y_train)

y_pred = regressor.predict(X_test)

print(regressor.coef_)

new_df = pd.DataFrame({
    'Actual': y_test,
    'Predicted': y_pred
})

print(new_df)

print('Predictive Analytics with New Data ...')
prediction_result = regressor.predict([[8], [8.9], [2]])
print(prediction_result)
