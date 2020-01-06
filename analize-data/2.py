import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import seaborn as sns
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score

def PlotPolly(model, independent_variable, dependent_variabble, Name):
    x_new = np.linspace(15, 55, 100)
    y_new = model(x_new)

    plt.plot(independent_variable, dependent_variabble, '.', x_new, y_new, '-')
    plt.title('Polynomial Fit with Matplotlib for Price ~ Length')
    ax = plt.gca()
    ax.set_facecolor((0.898, 0.898, 0.898))
    fig = plt.gcf()
    plt.xlabel(Name)
    plt.ylabel('Price of Cars')

    plt.show()
    plt.close()

path = 'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DA0101EN/automobileEDA.csv'

df = pd.read_csv(path)
lm = LinearRegression()
# print(lm)

X = df[['highway-mpg']]
Y = df['price']
# lm.fit(X,Y)

# print(Yhat[0:5])

Z = df[['horsepower', 'curb-weight', 'engine-size', 'highway-mpg']]
lm.fit(Z, df['price'])
# print(lm.intercept_)
# print(lm.coef_)


width = 12
height = 10
# plt.figure(figsize=(width, height))
# # sns.regplot(x="highway-mpg", y="price", data=df)
# # sns.regplot(x="peak-rpm", y="price", data=df)
# sns.residplot(df['highway-mpg'], df['price'])
# # plt.ylim(0,)
# plt.show()

# print(df[["peak-rpm","highway-mpg","price"]].corr())

Yhat=lm.predict(Z)

# plt.figure(figsize=(width, height))
# ax1 = sns.distplot(df['price'], hist=False, color="r", label="Actual Value")
# sns.distplot(Yhat, hist=False, color="b", label="Fitted Values" , ax=ax1)
# plt.title('Actual vs Fitted Values for Price')
# plt.xlabel('Price (in dollars)')
# plt.ylabel('Proportion of Cars')
# plt.show()
# plt.close()

x = df['highway-mpg']
y = df['price']
# # Here we use a polynomial of the 3rd order (cubic)
f = np.polyfit(x, y, 3)
p = np.poly1d(f)
# print(p)
#
# PlotPolly(p, x, y, 'highway-mpg')

pr=PolynomialFeatures(degree=2)
Z_pr=pr.fit_transform(Z)
# print(pr)
# print(Z.shape)
# print(Z_pr.shape)

# We create the pipeline, by creating a list of tuples including the name of the model or estimator and its corresponding constructor.

Input=[('scale',StandardScaler()), ('polynomial', PolynomialFeatures(include_bias=False)), ('model',LinearRegression())]

# we input the list as an argument to the pipeline constructor

pipe=Pipeline(Input)
# print(pipe)
pipe.fit(Z,y)
ypipe=pipe.predict(Z)
# print(ypipe[0:4])

print('Model 1: Simple Linear Regression')
#highway_mpg_fit
lm.fit(X, Y)
# Find the R^2
print('The R-square is: ', lm.score(X, Y))
Yhat=lm.predict(X)
print('The output of the first four predicted value is: ', Yhat[0:4])
# we compare the predicted results with the actual results
mse = mean_squared_error(df['price'], Yhat)
print('The mean square error of price and predicted value is: ', mse)
print()

print('Model 2: Multiple Linear Regression')
# fit the model
lm.fit(Z, df['price'])
# Find the R^2
print('The R-square is: ', lm.score(Z, df['price']))
Y_predict_multifit = lm.predict(Z)
print('The mean square error of price and predicted value using multifit is: ', \
      mean_squared_error(df['price'], Y_predict_multifit))
print()

print('Model 3: Polynomial Fit')
r_squared = r2_score(y, p(x))
print('The R-square value is: ', r_squared)
mean_squared_error(df['price'], p(x))
print()

new_input=np.arange(1, 100, 1).reshape(-1, 1)
lm.fit(X, Y)
# print(lm)
yhat=lm.predict(new_input)
# print(yhat[0:5])
plt.plot(new_input, yhat)
plt.show()