import pandas as pd

def carregando():
	df = pd.read_csv('train.csv')# carregar csv
	return df

def letra_a():
	df = carregando()
	print(df[df['Survived'] == 1])

def letra_b():
	df = carregando()
	survivers = df[df['Survived'] == 1]

	todos = df['Survived'].count()

	sobreviventes = survivers[['Survived']].count()['Survived']
	
	porcentagem = (sobreviventes.__float__() * 100)/todos.__float__()

	print(porcentagem, "%")	


def letra_d():
	df = carregando()

	apagar = df[df['Embarked'].isnull() == False]
	# print(apagar.index)
	print(df.drop(apagar.index,axis=0))


def letra_f():
	df = carregando()
	df['FamilySize'] = df['SibSp'] + df['Parch'] + 1
	df['IsAlone'] = 0
	print(df[df['FamilySize'] > 1].index)
	
	# # for i in df['FamilySize'].values:
	# # 	if i > 1:
	# # 		df['IsAlone'] = 1
	# # 	else:
	# # 		df['IsAlone'] = 0
	# # df['IsAlone'] = 1 if df['FamilySize'] > 1 else 0 
	
	# # df[df['FamilySize'] > 1]
	# # print()
	# # sozinho = df[df['FamilySize'] > 1]
	# # sozinho['IsAlone'] = 1	

	# # no_sozinho = df[df['FamilySize'] == 0]
	# # no_sozinho['IsAlone'] = 0
	
	# # df.append(no_sozinho)
	# # df.append(sozinho)
	# print(df)

	return df

def letra_g():
	df = carregando()

	print(pd.get_dummies(df['Embarked']))

def letra_h():
	df = letra_f()

	x = df[['Sex', 'IsAlone', 'Embarked', 'Pclass']]
	y = df['Survived']

	print(x, y)

letra_f()