import requests
from bs4 import BeautifulSoup as bs
from utils import download

def baixar_titulos():
	html = download('http://www.tce.pi.gov.br/')
	soup = bs(html, 'html.parser')

	news_div = soup.find('div', id='latestnews')
	lista_news = news_div.find_all('li', class_='latestnews')

	return lista_news

def menu():
	lista_news = baixar_titulos()	
	opcao = 1
	cont = 0
	print("--- MENU ---")	
		

	while True:
		for li in lista_news:
			cont +=1
			print("Noticia" , cont,  ":",  li.find('a', href=True).get_text())
		opcao = int(input("Digite o numero da Noticia: "))
		if opcao == 6:
			print("Opcao invalida")
			break
		
		link = lista_news[opcao-1].find('a', href=True)
		html = download(link['href'])
		soup = bs(html, 'html.parser')
		content = soup.find('div', class_='the_post post_content')
		for p in content.find_all('p'):
			print(p.get_text())
		
		opcao = int(input("\nDeseja voltar para o menu? 0 para sim,  6 para nao"))
		if opcao == 6:
			break
		cont = 0

	

menu()
	# print()
	# 	str(input("Opcao: ")

# print(lista_news)