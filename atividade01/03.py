import requests
from bs4 import BeautifulSoup as bs

# Exiba os dados referentes ao clima de Teresina. Guarde em banco as 5 últimas
# atualizações. https://www.climatempo.com.br/previsao-dotempo/cidade/264/teresina-pi

def download(url, num_retries=2):
	print('Downloading data from:', url)
	page = None
	try:
		response = requests.get(url)
		page = response.text
		if response.status_code >= 400:
			print('Download error:', response.text)
		if num_retries and 500 <= response.status_code < 600:
			return download(url, num_retries - 1)
	except requests.exceptions.RequestException as e:
		print('Download error:', e.reason)
	return page

def read_from_database():
	try:
		data = [eval(line) for line in open('db03.txt').readlines()]
		if len(data) > 5:
			return data[len(data)-5::]
		return data
	except:
		return []

def write_to_database(struct):
	if len(read_from_database())==0 or read_from_database().pop()['atualizacao']!=struct['atualizacao']:
		db = open('db03.txt','a')
		db.write(str(struct)+"\n")
		db.close()
		
html = download('https://www.climatempo.com.br/previsao-do-tempo/cidade/264/teresina-pi')
soup = bs(html, 'html.parser')

temperatura_momento = soup.find('p',class_='left normal txt-gray-cw temp-topo').get_text()
condicao_momento = soup.find('p', id='momento-condicao').get_text()
momento_sensacao = soup.find('li', id='momento-sensacao').get_text()
momento_humidade = soup.find('li', id='momento-humidade').get_text()
momento_pressao = soup.find('li', id='momento-pressao').get_text()
momento_vento = soup.find('a', id='momento-vento').get_text().replace(' ','').replace('\n','').replace('\xa0','')
atualizacao = soup.find('p', id='momento-atualizacao').get_text().replace('\n','').replace(' ','').replace('Atualizadoàs','')

estrutura = {
		'temperatura_momento':temperatura_momento,
		'condicao_momento':condicao_momento,
		'momento_sensacao':momento_sensacao,
		'momento_humidade':momento_humidade,
		'momento_pressao':momento_pressao,
		'momento_vento':momento_vento,
		'atualizacao':atualizacao
		}

write_to_database(estrutura)

dados = read_from_database()

print('                        dados de temperatura                            ')
print(' horario | temperatura | sensacao | umidade | pressao | vento | condicao')
print('------------------------------------------------------------------------')

for dado in dados:
	print(" %s%s| %s%s| %s%s | %s%s | %s%s | %s%s | %s "%(
		dado['atualizacao'], (8-len(dado['atualizacao']))*' ',
		dado['temperatura_momento'], (12-len(dado['temperatura_momento']))*' ',
		dado['momento_sensacao'], (8-len(dado['momento_sensacao']))*' ',
		dado['momento_humidade'], (7-len(dado['momento_humidade']))*' ',
		dado['momento_pressao'], (7-len(dado['momento_pressao']))*' ',
		dado['momento_vento'], (5-len(dado['momento_vento']))*' ',
		dado['condicao_momento'])
	)
