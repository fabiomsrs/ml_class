from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection  import cross_val_score
from scipy.stats import bayes_mvs
import pandas as pd
import numpy as np

def read():
	df = pd.read_csv('acessos_buscas2.csv')
	return df

def questao1():
	df = read()
	x = df[['home','busca','logado']]
	y = df['comprou']
	x = pd.get_dummies(x)	
	return x,y

def dados():	
	modelo = MultinomialNB()
	k = 10
	x,y = questao1()
	scores = cross_val_score(modelo, x, y, cv = k)

	cont = 0
	for score in scores:
		cont+=1
		print("score "+str(cont)+": ", score)

	taxa_de_acerto = np.mean(scores)
	print("Taxa de Acerto: ",taxa_de_acerto)
	desvio = scores.std()
	print("Desvio", desvio)	
	print(bayes_mvs(scores,0.95))

dados()