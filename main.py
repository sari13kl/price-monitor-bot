from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import smtplib
from email.mime.text import MIMEText
import json
from dotenv import load_dotenv
import os

load_dotenv() #carrega as variaveis de ambiente

URL = "https://www.amazon.com.br/Taming-Ela-%C3%A9-sol-tempestade/dp/6583127059/ref=sr_1_1?crid=3OC5B1ATHNHW5&dib=eyJ2IjoiMSJ9.KNTdwIIXeorvhNhBlIwkgWGsaEo_Iv3K9hl46l2q6P-9PruXU-ir0v96yM4c1mZCRpGNbxwPhuKWU_gSWZ3_zYAHNpFcgLQY4RIqd0n0gvqRBkjDkoNS1pn5Esm9KjOE-pZXL5ekyWpFNsqW27D9Sye16BqOYjFZDa0uOCAz4y42qnWR7B7hiFFKzACH37HvXWQFb5R0nUKDAcFOP7NaBl2ytyEX8nLxofYWjzmuZ9kLgN1DcjadmzaS4ptymKvvX11fnrX7NMqmP961eMHqKLNFI2M3LxDqPco4GbvmwGU.V3Fufgg7a8Ym-tj-e-IfA-hq6em5nqFrs646n_hfPqg&dib_tag=se&keywords=livro+taming+7&qid=1774800497&refinements=p_n_feature_browse-bin%3A8561251011&rnid=8561249011&sprefix=livro+tamin%2Caps%2C256&sr=8-1"
ARQUIVO = 'preco.json'

def pegar_preco():
    opcoes = Options()
    opcoes.add_argument("--headless") #roda invisível
    opcoes.add_argument("--no-sandbox")
    opcoes.add_argument("--disable-dev-shm-usage")

    navegador = webdriver.Chrome(options=opcoes)
    navegador.get(URL)
    
    time.sleep(6)
    
    try:
        preco = navegador.find_element(By.CLASS_NAME, "a-price-whole").text
        preco = preco.replace('.', '').replace(',', '')
        return int(preco)
    except:
        return None
    finally:
        navegador.quit()
        
def salvar_preco(preco):
    with open(ARQUIVO, 'w') as arquivo:
        json.dump({"preco_atual": preco}, arquivo)
        
def carregar_preco():
    try:
        with open(ARQUIVO, 'r') as arquivo:
            preco = json.load(arquivo)
            return int(preco['preco_atual'])
    except:
        return None
    
def enviar_email(preco_antigo, preco_novo):
    remetente = 'EMAIL_REMETENTE'
    destinatario = 'EMAIL_DESTINATARIO'
    senha = 'EMAIL_SENHA'
    
    msg = MIMEText(f"O preço mudou de {preco_antigo} para {preco_novo}")
    msg["Subject"] = "Alerta de Preço 🚨"
    msg["From"] = remetente
    msg["To"] = destinatario
    
    servidor = smtplib.SMTP("smtp.gmail.com", 587)
    try:
        servidor.starttls()
        servidor.login(remetente, senha)
        servidor.send_message(msg)
    except Exception as e:
        print(f"Erro ao enviar email: {e}")
    finally:
        servidor.quit()
    
    
    
def monitorar():
    preco_atual = pegar_preco()
    preco_antigo = carregar_preco()
    
    if preco_atual is not None:
        if preco_antigo and preco_atual != preco_antigo:
            enviar_email(preco_antigo, preco_atual)
        
        salvar_preco(preco_atual)
        
monitorar()