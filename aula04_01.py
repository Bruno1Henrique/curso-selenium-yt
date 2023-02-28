from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By

browser = Firefox()

browser.get('http://selenium.dunossauro.live/aula_04_a.html')

lista_n_ordenada = browser.find_element(By.TAG_NAME, 'ul')

lis = lista_n_ordenada.find_elements(By.TAG_NAME, 'li')

lis[0].find_element(By.TAG_NAME, 'a').text

""""
1 - Buscamos o 'ul'
2 - Buscamos todos os 'lis'
3 - No primeiro 'li', buscamos 'a' e pegamos o seu texto
"""