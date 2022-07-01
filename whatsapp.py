#pip insall sqlite3
import time
import urllib
import sqlite3 as Firedac

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

navegador = webdriver.Chrome()

navegador.get("http://web.whatsapp.com/")

while len(navegador.find_elements_by_id("side")) <1:
    time.sleep(1)

#FDConnection = Firedec("mensagem.db")
          
#FDQuery = FDQuery.cursor()

contatos = ['85989926382', '85987444812']

#for row in FDQuery.execute("SELECT * FROM mensagens"):
for msg in contatos:
 #  contato = row[1]
 #  numero = '55'+row[5]
    numero = '55'+msg
          
 #  mensagem = row[3]
    mensagem = 'Tou testando o Whatsapp...Chegou uma mensagem aí, hein?'
    texto = urllib.parse.quote(mensagem)
    link = f"https://web.whatsapp.com/send?phone={numero}&text={texto}"
    navegador.get(link)
    while len(navegador.find_elements_by_id("side")) <1:
        time.sleep(1)

    navegador.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]').send_keys(keys.ENTER)
    time.sleep(5)

