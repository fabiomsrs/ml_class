import pandas as pd
import matplotlib.pyplot as plt

def carregar():
	df = pd.read_csv('census.csv')# carregar csv
	return df

def criar_data_frame(data, columns):
	return pd.DataFrame(data, columns=columns)


def questao1():
	df = carregar()
	print(df.head(5))

def questao2():
	df = carregar()

	# --- Letra A ----
	'''
	print(df['age'].describe()[['min','max','mean']])
	print(df['education-num'].describe()[['min','max','mean']])
	print(df['hour-per-week'].describe()[['min','max','mean']])
	'''
	# -------------------------------------------------------------

	# --- Letra B ---
	'''
	data = {
		'Minimo' : [df['age'].describe()['min'], df['education-num'].describe()['min'], df['hour-per-week'].describe()['min']],
		'Maximo' : [df['age'].describe()['max'], df['education-num'].describe()['max'], df['hour-per-week'].describe()['max']],
		'Media' : [df['age'].describe()['mean'], df['education-num'].describe()['mean'], df['hour-per-week'].describe()['mean']],
	}


	temp_df = criar_data_frame(data, ['Minimo', 'Maximo', 'Media'])
	plt.hist(temp_df['Minimo'])
	plt.show()
	plt.hist(temp_df['Maximo'])
	plt.show()
	plt.hist(temp_df['Media'])
	plt.show()
	'''
	# --------------------------------------------------------------------------------------------------------------------------------

	# --- Letra C ---
	'''
	for column in df.columns:
		print(column + ": " , df[column].isnull().sum()) # encontrar colunas de valores nulos
	'''
	#----------------------------------------------------------------------------------------

	# --- Letra D, E ----
	'''
	for column in df.columns:
		if column != 'final-weight' and column != 'age':
			print(column + ": " , df[column].unique())			
			print("Tamanho" + ": " , str(len(df[column].unique().tolist())))	
			print('\n\n')
	'''
	# -------------------------------------------------------------------------------------

questao2()