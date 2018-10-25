from sklearn.metrics import confusion_matrix
from sklearn.naive_bayes import GaussianNB, BernoulliNB, MultinomialNB	
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
import pandas as pd

def carregando():
	df = pd.read_csv('train.csv')# carregar csv
	return df

def letra_h():
	df = carregando()
	
	df['Sex'] = df['Sex'].map( {'female': 0, 'male': 1} )
	df['FamilySize'] = df['SibSp'] + df['Parch'] + 1
	df['IsAlone'] = (df['FamilySize']<=1)
	df['IsAlone'] = df['IsAlone'].map( {True: 1, False: 0} )
	x = df[['Sex','IsAlone','Embarked', 'Pclass']]
	y = df['Survived']

	return pd.get_dummies(x), y

def algoritmos():
	g = GaussianNB()
	b = BernoulliNB()
	m = MultinomialNB()	

	x, y = letra_h()
	x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size=0.25,random_state=0)

	g.fit(x_treino, y_treino)
	b.fit(x_treino, y_treino)
	m.fit(x_treino, y_treino)
	
	return g,b,m

def scores():
	print("\n\n" + "Scores Confusao")
	g, b, m = algoritmos()

	x, y = letra_h()
	x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size=0.25,random_state=0)

	print("Multinomial", m.score(x_teste, y_teste)) 
	print("Gaussian", g.score(x_teste, y_teste))
	print("Bernoulli", b.score(x_teste, y_teste))

def matriz_confusao():
	print("\n\n" + "Matriz Confusao:" + "\n")
	g, b, m = algoritmos()

	x, y = letra_h()
	x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size=0.25,random_state=0)

	print("Multinomial", confusion_matrix(y_teste, m.predict(x_teste)))
	print("Gaussian", confusion_matrix(y_teste, g.predict(x_teste)))
	print("Bernoulli", confusion_matrix(y_teste, b.predict(x_teste)))


scores()

matriz_confusao()