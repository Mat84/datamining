pip install selenium

pip install webdriver-manager

import selenium.webdriver.common.keys

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType
from bs4 import BeautifulSoup

browser = webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())

def login():
    url      = 'https://web.spaggiari.eu/home/app/default/login.php?custcode='
    username = 'BOLS0006.*******'
    password = '****************'
    browser.get(url)
    browser.find_element_by_id('login').send_keys(username)
    browser.find_element_by_id('password').send_keys(password)
    browser.find_element_by_class_name('check-auth').click()

login()

url2 = 'https://web.spaggiari.eu/cvv/app/default/gioprof.php?classe_id=&materia=203965&ope=LEZ&codocenza=1&gruppo_id=1AC_RELIGIONE'
browser.get(url2)
browser.find_element_by_class_name('align_middle font_size_14 header headerSortDown').click()

html = browser.page_source
html

soup = BeautifulSoup(html, 'html.parser')
lezioni = soup.find_all("span",{"class":"nota_1"})

print(lezioni)

