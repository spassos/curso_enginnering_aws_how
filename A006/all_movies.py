# %%
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import pandas as pd
# %%
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
def tem_item(xpath, driver = driver):
    try:
        driver.find_element(By.XPATH, xpath)
        return True
    except:
        return False
driver.implicitly_wait(40)
driver.get('https://pt.wikipedia.org/wiki/Nicolas_Cage')
tabela = driver.find_element(By.XPATH, 
            '/html/body/div/div/div[4]/main/div/div[4]/div[1]/table[2]')
time.sleep(1)
# %%
#teste_path = 'html/body/nav[1]/div/ul[1]/li[5]/a'
teste_path = '/html/body/div/div/div[4]/main/div/div[4]/div[1]/table[2]'
i = 0
while not tem_item(teste_path):
    i+=1
    if i >50:
        break
    pass
# %%
df = pd.read_html('<table>' + tabela.get_attribute('innerHTML') + '</table>')[0]
# %%
with open('print.png', 'wb') as f:
    f.write(driver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[1]/table[1]/tbody/tr[2]/td/div/div/div/a/img').screenshot_as_png)

# %%
driver.close()
# %%
df.columns
# %%
df[df['Ano']==1984]
# %%
df.to_csv('filmes_nicolas_cage.csv', sep=';', index=False)
# %%
