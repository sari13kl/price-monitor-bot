#  Bot de Monitoramento de Preços

Bot de monitoramento de preços da Amazon usando Python e Selenium.
Verifica automaticamente o preço de um produto e envia um e-mail de alerta quando o preço mudar.

---

## Funcionalidades

- Acessa a página do produto na Amazon automaticamente
- Captura o preço atual via web scraping
- Compara com o preço salvo anteriormente
- Envia e-mail de alerta quando o preço muda
- Salva o histórico de preço em arquivo JSON

---

## Tecnologias utilizadas

- [Python 3](https://www.python.org/)
- [Selenium](https://www.selenium.dev/) — automação do navegador
- [smtplib](https://docs.python.org/3/library/smtplib.html) — envio de e-mail
- [python-dotenv](https://pypi.org/project/python-dotenv/) — variáveis de ambiente

---

## Estrutura do projeto
```
price-monitor-bot/
├── main.py          # Script principal
├── preco.json       # Preço salvo (gerado automaticamente)
├── .env             # Credenciais (não sobe pro Git)
├── .gitignore       # Ignora .env e outros arquivos sensíveis
├── requirements.txt # Dependências do projeto
└── README.md
```
