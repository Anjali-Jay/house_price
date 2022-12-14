# -*- coding: utf-8 -*-
"""Multicolinearty Removal using VIF.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_5RBmJpJ90gko5w-wCUXUN9yh5v3sEZA
"""

import pandas as pd

data = pd.read_csv("/content/Housing_Modified_prepared.csv")

data.head(5)

# Select independent and dependent variables
Y = data["price"]
independent_var = data.columns
independent_var = independent_var.delete(0)
X = data[independent_var]

# fit the Ordinary Least Squared Regression Model
import statsmodels.api as sm

model = sm.OLS(Y, X)

# Train the model
model = model.fit()

# CHecl the model summary
model.summary()

# Calculate Varience Inflation Factor (VIF)
from statsmodels.stats.outliers_influence import variance_inflation_factor as vif

for i in range(len(independent_var)):
  vif_list = [vif(data[independent_var].values, index) for index in range(len(independent_var))]
  mvif = max(vif_list)
  print("Max VIF value is", mvif)
  drop_index = vif_list.index(mvif)
  print("For the independent variable", independent_var[drop_index])
  if mvif > 10:
    print("Deleting", independent_var[drop_index])
    independent_var = independent_var.delete(drop_index)
print("Final independent variables", independent_var)

Y = data["price"]
X = data[independent_var]

model = sm.OLS(Y, X)
model = model.fit()

model.summary()

user_input = {}
for var in independent_var:
  temp = input("Enter "+var+": ")
  user_input[var] = temp
user_df = pd.DataFrame(data = user_input, index=[0], columns = independent_var)
#price = model.predict(user_df)
#print("Price of House id USD", int(price[0]))
import sklearn.linear_model as lm
lr = lm.LinearRegression()
lr.fit(X, Y)
price = lr.predict(user_df)
print("House price is USD", int(price[0]))

