import pandas as pd

def questao1():
	df = pd.read_csv('risco-credito.csv')# carregar csv
	return df

def questao2():
	df = questao1()
	print(df.head(3)) # primeiras 3 linhas

def questao3():
	df = questao1()
	print(df.describe()) # descrição da tabela

def questao4():
	df = questao1()
	print(df['historia'].unique(),df['divida'].unique(),df['garantias'].unique(),df['risco'].unique())# registros unicos de cada coluna

def questao5():
	df = questao1()
	print("Alto Risco:")
	print(df[ df['risco'] == 'alto' ]) # filtrar registros de risco alto

	print("Baixo Risco:")
	print(df[ df['risco'] == 'baixo' ]) # filtrar registros de risco baixo

def questao6():
	df = questao1()
	for column in df.columns:
		print(column + ": " , df[column].isnull().sum()) # encontrar colunas de valores nulos

def questao7():
	# Separar tabela em risco e resto(historia, divida e garantias)
	df = questao1()
	
	y = df['risco']

	x = df[ ['historia', 'divida', 'garantias'] ]

	
	return (x,y)

def questao8():
	# categorizar as colunas x
	x,y = questao7()
	
	X = pd.get_dummies(x)
	print(X)
	return X

def questao9():
	from sklearn.model_selection import train_test_split
	from sklearn.naive_bayes import MultinomialNB
	
	x,y = questao7()
	X = pd.get_dummies(x)

	x_treino, x_teste, y_treino, y_teste = train_test_split(X, y, test_size=0.25,random_state=0) # separar treino e teste( 25% teste)

	return x_treino, x_teste, y_treino, y_teste

def questao10():
	#checar o score
	x_treino, x_teste, y_treino, y_teste = questao9	

	modelo = MultinomialNB()	

	modelo.fit(x_treino, y_treino)

	print(modelo.score(x_teste, y_teste)) 

def questao11():
	# checar o score com a modificação na coluna de marcação(Risco)
	from sklearn.model_selection import train_test_split
	from sklearn.naive_bayes import MultinomialNB

	x,y = questao7()
	x = pd.get_dummies(x)

	y = y.map( {'alto': 1, 'baixo': 0, 'moderado': 0} )	
	
	x_treino, x_teste, y_treino, y_teste = train_test_split(x, y.values, test_size=0.25,random_state=0)	
	
	modelo = MultinomialNB()	
	modelo.fit(x_treino, y_treino)

	print(modelo.score(x_teste, y_teste))

def main():
	questao8()

if __name__ == '__main__':
	main()