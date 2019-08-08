from pprint import pprint
import wget


base_url = 'http://riotransparente.rio.rj.gov.br/riotransparente/arquivos'
anos = [2019, 2018, 2017, 2016, 2015, 2014, 2013, 2012, 2011, 2010, 2009, 2008]
links = []

for ano in anos:
    url_contratos = f'{base_url}/Open_Data_Contratos_{ano}.txt'
    links.append(url_contratos)
    url_despesas = f'{base_url}/Open_Data_Desp_{ano}.txt'
    links.append(url_despesas)
    url_despesas_ato = f'{base_url}/Open_Data_Desp_Ato_{ano}.txt'
    links.append(url_despesas_ato)
    url_favorecidos = f'{base_url}/Open_Data_Favorecidos_{ano}.txt'
    links.append(url_favorecidos)
    url_receitas = f'{base_url}/Open_Data_Rec_{ano}.txt'
    links.append(url_receitas)

pprint(links)

for url in links:
    try:
        nome_do_arquivo = wget.download(url)
    except:
        pass
