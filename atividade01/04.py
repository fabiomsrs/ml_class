import requests
import re
from bs4 import BeautifulSoup as bs
from operator import itemgetter
from time import sleep

# Calcule a densidade populacional de todos os países disponíveis no site
# http://example.webscraping.com/. Considere que há 25 páginas.

def download(url, quiet=False, num_retries=2):
	if not quiet:
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

base_url = 'http://example.webscraping.com'

for i in range(1,26):
	print('\n   BAIXANDO CONTEUDO DA PAGINA ',i, '\n')
	sleep(0.75)
	soup = bs(download(base_url+'/places/default/index/'+str(i)+'/', quiet=True), 'html.parser') 
	countries_urls = [row['href'] for row in soup.find('div', id='results').find_all('a')]
	for coutry_url in countries_urls:	
		country_soup = bs(download(base_url+coutry_url, quiet=True), 'html.parser')
		country_name = country_soup.find(attrs={'id':'places_country__row'}).find(attrs={'class':'w2p_fw'}).get_text()
		country_population = country_soup.find(attrs={'id':'places_population__row'}).find(attrs={'class':'w2p_fw'}).get_text()
		country_area = country_soup.find(attrs={'id':'places_area__row'}).find(attrs={'class':'w2p_fw'}).get_text().replace(' square kilometres','')
		print('nome do pais: %s | populacao: %s hab | area: %s km2 | densidade demografica : %.2f hab/km2\n' %(country_name,country_population,country_area,   int(country_population.replace(',',''))/int(country_area.replace(',',''))))
		sleep(0.5)
