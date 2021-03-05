from uteis import metodos
from urllib.parse import quote

#----------------------------------------------------------
# Definições da mensagem e caminho do arquivo a ser enviado
#----------------------------------------------------------

mensagem = """Defina aqui sua mensagem com seus respectivos parágrafos. Aceita emojis."""

caminho_do_arquivo = "Defina aqui o caminho do arquivo. Para Windows, utilize contra-barra"

#----------------
# Execução do bot
#----------------

contatos = metodos.carregar_lista()
parsedMessage = quote(mensagem)

for contato in contatos:  
  metodos.enviar_mensagem(contato, parsedMessage)
  metodos.enviar_arquivo(caminho_do_arquivo)



