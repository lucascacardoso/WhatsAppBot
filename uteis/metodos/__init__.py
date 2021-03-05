from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(ChromeDriverManager().install())

def carregar_lista():
    """Carregar lista de contatos no array 'lista'
    """

    try:
        lista = list()
        with open('contatos.txt', 'r') as arq:
            for valor in arq:
                lista.append(valor.replace('\n', ''))
    except:
        print('Erro ao localizar o arquivo!')
    finally:
        arq.close()
    return lista

def enviar_mensagem(contato, parsedMessage):  
  driver.get('https://web.whatsapp.com/send?phone='+contato+'&text='+parsedMessage)
  time.sleep(15)

  campo_mensagem = driver.find_elements_by_xpath(
    '//div[contains(@class,"copyable-text selectable-text")]'
  )
  
  campo_mensagem[1].click()
  time.sleep(3)
  campo_mensagem[1].send_keys(Keys.ENTER)
  time.sleep(3)

def enviar_arquivo(file_path):
  driver.find_element_by_css_selector("span[data-icon='clip']").click()
  driver.find_element_by_css_selector("input[type='file']").send_keys(file_path)
  time.sleep(3)
  driver.find_element_by_css_selector("span[data-icon='send']").click()
  time.sleep(3)