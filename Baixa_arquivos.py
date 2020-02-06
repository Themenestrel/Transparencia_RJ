from pprint import pprint
import wget
import os
from os.path import isfile, join, basename
import shutil

#path = "//unity/corp2/SCE/! NGI/Power BI Paineis/Bases Comuns/Rio Transparente"
#dir = os.listdir(path)
path = "C:/Users/mscanavachi/.PyCharmCE2019.3/config/scratches/Dados Transparência"
dir = os.listdir(path)
path_old = "//unity/corp2/SCE/! NGI/Power BI Paineis/Bases Comuns/Rio Transparente/Rio_Transparência_old"
dir_old = os.listdir(path_old)
path_base = "//unity/corp/planilha/Base_Contratos"
dir_base = os.listdir(path_base)
ext = 'txt'

#try:
for file in dir:
    if os.path.exists(file):
        os.remove(file)
#except:
#    pass
'''
try:
    for item in [join(path, f) for f in os.listdir(path) if isfile(join(path, f)) and f.endswith(ext)]:
        shutil.copy(item, join(path_old, basename(item)))
        print('copiado "{}" -> "{}"'.format(item, join(path_old, basename(item))))
except:
    pass

try:
    for file in dir:
        os.remove(file)
except:
    pass

base_url = 'http://riotransparente.rio.rj.gov.br/riotransparente/arquivos'
anos = [2020, 2019, 2018, 2017, 2016, 2015, 2014, 2013, 2012, 2011, 2010, 2009, 2008]
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
        nome_do_arquivo = wget.download(url, out="//unity/corp2/SCE/! NGI/Power BI Paineis/Bases Comuns/Rio Transparente")
    except:
        pass
try:
    for file_base in path_base:
        os.remove(file_base)
except:
    pass

try:
    for item_base in [join(path, f) for f in os.listdir(path) if isfile(join(path, f)) and f.endswith(ext)]:
        shutil.copy(item_base, join(path_base, basename(item_base)))
        print('copiado "{}" -> "{}"'.format(item_base, join(path_old, basename(item_base))))
except:
    pass
'''
