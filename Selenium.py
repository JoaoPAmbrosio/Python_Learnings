# Selenium Tutorial
# https://sites.google.com/a/chromium.org/chromedriver/download
"""
from selenium import webdriver # O web driver é o que vai fazer rodar todas as acoes
from selenium.webdriver.common.keys import keys # Vai dar acesso a enterkey, diskkeys para poder acessar search bar
import time # Para poder utilizar o tempo no programa como em pausas


path = "copiar o path\chomedriver.exe"
driver = webdriver.Chrome(PATH) # chrome com C maiusculo, é o browser que esta sendo usado

driver.get("https://site que escolher.com") # Se voce rodar o programa, o site deve abrir
print(driver.title) # Recebe o titulo do site


# Procurar por ID(em html é único)> Name(nao necessariamente é único, mas costuma ser)> Class(é ok, mas 
# pode gerar problemas. o primeiro da classe é escolhido e pode nao ser o desejado)>>tag()

search = driver.find                 # vai aparecer muitas possibilidades de onde deseja rastrear o elemento
                    _element_by_name("s") .: s é o encontrado na inspecao

search.send_keys("test") # Como mandar texto no search box, imput field, enviando "test"
search.send_keys(Keys.RETURN) # Para dar enter/return

# print(driver.page_source) # Extrai todo sourcecode do site
# comeca a procurar o que deseja, inspecionando o site. Procure um ID talvez

# (id)
main = driver.find_element.by.id("main")

# Para nao cair no problema de fechar muito rapido e nao acessar a todo recurso que queremos, estabelecemos:
try:
     (main)
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "myDynamicElement"))
    )                                                 (main)
finally:
    driver.quit()
# Vai esperar, até a presenca do elemento(main) seja localizado, para seguir com o código

print(main.text)


# time.sleep(5) # Para o programa desligar por 5 segundos
# driver.close() # Fecha a aba
driver.quit() # Fecha o navegador

"""
