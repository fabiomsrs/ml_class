import pandas as pd
df = pd.read_csv('dataset.csv')
x = df[[ 'educacao-esposa', 'educacao-marido', 'marido-ocupacao', 'standard-of-living' ]]
y = df.drop([ 'educacao-esposa', 'educacao-marido', 'marido-ocupacao', 'standard-of-living' ], axis=1)

X = pd.get_dummies(x)
print(X,y)