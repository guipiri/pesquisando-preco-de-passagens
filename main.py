from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import csv

ida = '27-12-2022'
volta = '03-01-2023'
para = 'SSA'

for k in range(2):
    if k == 1:
        ida = '27-12-2022'
        para = 'IOS'
    for i in range(4):
        if i == 1:
            volta = '04-01-2023'
        if i == 2:
            ida = '26-12-2022'
        if i == 3:
            volta = '03-01-2023'

        URL = f"https://123milhas.com/v2/busca?de=SAO&para={para}&adultos=1&criancas=0&bebes=0&ida={ida}&volta={volta}&classe=3"

        option = Options()
        option.headless = True
        navegador = webdriver.Chrome(options=option)
        navegador.get(URL)
        try:
            WebDriverWait(navegador, 100).until(
                EC.presence_of_element_located(
                    (By.XPATH, "/html/body/div[1]/div/div/div/div[2]/group-selector/div/div[2]/div[1]/flight-price-card/div/form/div[2]/div[2]/price-details/div[4]/p[2]/span[2]"))
            )
            price_element = navegador.find_element(
                By.XPATH, "/html/body/div[1]/div/div/div/div[2]/group-selector/div/div[2]/div[1]/flight-price-card/div/form/div[2]/div[2]/price-details/div[4]/p[2]/span[2]")

            price = float(price_element.text.replace(".", ""))
            date = datetime.today()

            with open(f'milhas123{para}{ida}{volta}.csv', 'a', newline='') as csvfile:
                spamwriter = csv.writer(csvfile)
                spamwriter.writerow([date, price])
        finally:
            navegador.quit()
