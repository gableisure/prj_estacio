from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

class Scraping:

    def __init__(self):
        print('Running module Scraping')
        driver = webdriver.Chrome()
        driver.get('https://sia.estacio.br/sianet/Logon')
        sleep(5)

    