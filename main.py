from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc
from pylist import mensagens
import pandas as pd
import random
import time

df = pd.read_csv('main.csv')

chrome_options = uc.ChromeOptions()

# chrome_options.add_argument("--load-extension=" + r"C:\Users\USER\AppData\Local\Google\Chrome\User Data\Profile 1\Extensions\ekcgkejcjdcmonfpmnljobemcbpnkamh\4.8.8.3_0")

driver = uc.Chrome(options=chrome_options)

driver.get('https://web.whatsapp.com/')

time.sleep(30)

mensagem_sortida = random.choice(mensagens)

for numero in df['Numero']:
    print(mensagem_sortida['msg'])

    script_js = f"window.location.href = 'https://web.whatsapp.com/send?phone={numero}&text={mensagem_sortida['msg']}'"

    driver.execute_script(script_js)

    time.sleep(50)

    button_locator = (By.XPATH, '//button[@data-tab="11" and @aria-label="Enviar"]')

    button = WebDriverWait(driver, 10).until(EC.presence_of_element_located(button_locator))

    button.click()

    time.sleep(5)

time.sleep(600)

driver.quit()