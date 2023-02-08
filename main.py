from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

class CookieClicker:
    def __init__(self) -> None:
        self.tags = {
            "language": '//*[@id="langSelect-PT-BR"]',
            "cookie": '//*[@id="bigCookie"]',
            "upgrades": '/html/body/div[2]/div[2]/div[19]/div[3]/div[5]/div',
            "produtos": '//*[@id="product$$cash$$"]'
        }
        self.init = webdriver.Chrome(executable_path='ChromeDriver\chromedriver.exe')

    def abrir_navegador(self, url):
        self.init.get(url)
        self.init.maximize_window()
        sleep(6)
        self.init.find_element(By.XPATH, self.tags['language']).click()
        sleep(6)

    def clicker(self):
        count = 1
        increments_produsts = 0
        while count:
            self.init.find_element(By.XPATH, self.tags['cookie']).click()
            product = self.init.find_element(By.XPATH, self.tags['produtos'].replace('$$cash$$', str(increments_produsts)))
            upgrades = self.init.find_elements(By.XPATH, self.tags['upgrades'])

            is_enabled = product.get_attribute('class')

            if len(upgrades) > 0:
                upgrade = upgrades[0]
                is_enabled_upgrade = upgrade.get_attribute('class').split(' ')
                if 'enabled' in is_enabled_upgrade:
                    upgrades[0].click()

            if is_enabled.split(' ')[2] == 'enabled':
                product.click()

            if increments_produsts == 18:
                increments_produsts = 0


            increments_produsts += 1

cookie = CookieClicker()
cookie.abrir_navegador('https://orteil.dashnet.org/cookieclicker/')
cookie.clicker()