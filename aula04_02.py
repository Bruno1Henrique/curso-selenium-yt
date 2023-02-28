from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By

def find_by_text(browser, tag, text):

    """
    Encontrar o elemento com o texto 'text'.

    Argumentos:
     - browser = instancia do browser [firefox, chrome]
     - texto = conteudo que deve estar na tag
     - tag = tag onde o texto sera procurado
    """
    elementos = browser.find_elements(By.TAG_NAME, tag) #lista

    for elemento in elementos:
        if elemento.text == text:
            return elemento 
        
def find_by_href(browser, link):

    """
    Encontrar o elemento 'a' com o link 'link'.

    Argumentos:
     - browser = instancia do browser [firefox, chrome]
     - link = link que sera procurado em todos as tags 'a'
    """
    elementos = browser.find_elements(By.TAG_NAME, 'a')

    for elemento in elementos:
     if link in elemento.get_attribute('href'):
        return elemento


browser = Firefox()

browser.get('http://selenium.dunossauro.live/aula_04_a.html')

# elemento_ddg = find_by_text(browser, 'li', 'DuckDuckGo')

elemento_ddg = find_by_href(browser, 'ddg')




