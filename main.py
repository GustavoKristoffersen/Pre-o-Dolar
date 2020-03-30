from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import json
import bot
from datetime import datetime
from pytz import timezone

data = datetime.now()
fuso_horario = timezone('America/Sao_Paulo')
data_e_hora = data.astimezone(fuso_horario)
data_brasil = data_e_hora.strftime('%d/%m/%Y às %H:%M')

req = Request('https://br.investing.com/currencies/usd-brl', headers={'User-Agent': 'Mozilla/5.0'})

webpage = urlopen(req).read()

soup = BeautifulSoup(urlopen(req),"html.parser")
preco = soup.find("span", class_="arial_26 inlineblock pid-2103-last").get_text().strip()

preco = preco[:4]
preco = preco.replace(',','.')
preco = float(preco)
print(preco)

a = open('preco_anterior','r')
preco_antigo = json.loads(a.read())
a.close()

if preco > preco_antigo:
  msg = 'O dólar subiu\U0001F62D - Agora está em R${}\n\nAtualizado em {}'.format(preco,data_brasil)

elif preco < preco_antigo:
  msg = 'O dólar desceu\U0001F60D - Agora está em R${}\n\nAtualizado em {}'.format(preco,data_brasil)

else:
  msg = 'O dólar nem subiu nem desceu\U0001F615 - Agora está em R${} \n\nAtualizado em {}'.format(preco,data_brasil)

bot.enviar_msg(msg)

nome_arquivo = "preco_anterior"
preco_anterior = json.dumps(preco, ensure_ascii=False, indent = 2)
arquivo = open(nome_arquivo,'w')
arquivo.write(preco_anterior)
arquivo.close()

