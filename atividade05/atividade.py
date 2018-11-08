import pandas as pd
import matplotlib.pyplot as plt
import numpy

df_credit = pd.read_csv('credit-data.csv')# carregar csv
df_titanic = pd.read_csv('titanic.csv')# carregar csv

# age =   .dropna()
# plt.boxplot(age, showfliers = True)
# plt.show()

# print(df_credit[df_credit['age'].isnull()])
# print(df_credit[df_credit['age'] < 0])

print(df_titanic)