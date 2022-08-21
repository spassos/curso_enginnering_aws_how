# %%
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import sys
import time
# %%
cep = sys.argv[1]
if cep:
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    time.sleep(5)
    # %%
    #driver.get('https://howedu.com.br/')
    #driver.find_element(By.XPATH, '//*[@id="menu-1-739815d"]/li[1]/a').click()
    #driver.find_element(By.XPATH, '//*[@id="lista-bootcamps"]/div/div/div/div[6]/div/div/section/div/div/div/section[1]/div/div/div/div[1]/div/h3/a').click()
    # %%
    driver.get('https://buscacepinter.correios.com.br/app/endereco/index.php?t')
    elem_cep = driver.find_element(By.NAME, 'endereco')
    elem_cep.clear()
    elem_cep.send_keys(cep)
    # %%
    select = Select(driver.find_element(By.NAME, 'tipoCEP'))
    select.select_by_value('ALL')
    # %%
    driver.find_element(By.ID, 'btn_pesquisar').click()
    # %%
    time.sleep(1)
    logradouro = driver.find_element(By.XPATH, '/html/body/main/form/div[1]/div[2]/div/div[4]/table/tbody/tr/td[1]').text
    bairro = driver.find_element(By.XPATH, '/html/body/main/form/div[1]/div[2]/div/div[4]/table/tbody/tr/td[2]').text
    localidade = driver.find_element(By.XPATH, '/html/body/main/form/div[1]/div[2]/div/div[4]/table/tbody/tr/td[3]').text
    driver.close()
    # %%
    print("""
    Para o CEP {} temos:
    Endereço: {}
    Bairro: {}
    Localidade: {}
    """.format(
    cep,
    logradouro.split(',')[0],
    bairro,
    localidade
    )
    )
# %%
