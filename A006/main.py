# %%
from selenium import webdriver
from selenium.webdriver.common.by import By
# %%

driver = webdriver.Chrome('./src/chromedriver')

driver.get('https://howedu.com.br/')
# %%

driver.find_element(By.XPATH, '//*[@id="menu-1-739815d"]/li[1]/a').click()
# %%
driver.find_element(By.XPATH, '//*[@id="lista-bootcamps"]/div/div/div/div[6]/div/div/section/div/div/div/section[1]/div/div/div/div[1]/div/h3/a').click()