#pip insall sqlite3
import time
import urllib
import sqlite3 as Firedac

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

host = 'localhost'
database = "tar.gdb"
user='SYSDBA'
senha='masterkey'
pasta = 'D:/Bd/Tarefas/'

navegador = webdriver.Chrome()

navegador.get("http://web.whatsapp.com/")

while len(navegador.find_elements_by_id("side")) <1:
    time.sleep(1)

print("side")

#FDConnection = Firedec("mensagem.db")
          
#FDQuery = FDQuery.cursor()

banco_gdb = pasta + database
conn_gdb = fdb.connect(
                       host=host,
                       database=banco_gdb,
                       port=3050,
                       user=user,
                       password=senha,
                       charset='ISO8859_1')

curr = conn_gdb.cursor()
curr.execute('SELECT CLI_CONTATO, CLI_CONTA_FONE, CLI_COD_PROX_VENC FROM CLIENTES WHERE CLI_CELULAR IS NOT NULL')
for c in curr.fetchall():
   celular = c[0]
   contato = c[1]
   serie = c[2]


contatos = ['85989926382', '85987444812', '85999542929']

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

