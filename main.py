from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import time
import csv

PATH = "C:\\Geckodriver\\geckodriver.exe"
service = Service(PATH)

FIREFOX_BINARY = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"

options = Options()
options.binary_location = FIREFOX_BINARY

driver = webdriver.Firefox(service=service, options=options)

url = "https://www.divan.ru/category/svet"

driver.get(url)
time.sleep(3)
lamps = driver.find_elements(By.CSS_SELECTOR, 'div._Ud0k')
parsed_data =[]
for lamp in lamps:
    try:
        name = lamp.find_element(By.CSS_SELECTOR, 'div.lsooF span').text
        price = lamp.find_element(By.CSS_SELECTOR, 'div.q5Uds span').text
        link = lamp.find_element(By.CSS_SELECTOR, 'a').get_attribute('href')
    except Exception as e:
        print(f"Произошла ошибка при парсинге{e}")
        continue
    parsed_data.append([name, price, link])

driver.quit()
with open("lamp.csv", 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Название', 'цена', 'ссылка'])
    writer.writerows(parsed_data)









