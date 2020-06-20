from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium import webdriver
import os
files = [f for f in os.listdir('.') if os.path.isfile(f)]
for f in files:
    print(f)

options = FirefoxOptions()
options.add_argument("--headless")
driver = webdriver.Firefox(options=options, executable_path="/app")
driver.get("https://www.google.com.br/")
print (driver.page_source)
driver.quit()
print ("Deu certo!")