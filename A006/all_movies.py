# %%
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import pandas as pd
# %%
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://pt.wikipedia.org/wiki/Nicolas_Cage')
tabela = driver.find_element(By.XPATH, 
            '/html/body/div/div/div[4]/main/div/div[4]/div[1]/table[2]')
time.sleep(1)
# %%
df = pd.read_html('<table>' + tabela.get_attribute('innerHTML') + '</table>')[0]
driver.close()
# %%
df.columns
# %%
df[df['Ano']==1984]
# %%
df.to_csv('filmes_nicolas_cage.csv', sep=';', index=False)