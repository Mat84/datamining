# ___________________SPAGGIARI_SCRAPER____________________#
#############################################################################
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import tkinter as tk


#############################################################################

def login(browser, username, password):
    url = 'https://web.spaggiari.eu/home/app/default/login.php'
    browser.get(url)
    browser.find_element(By.ID, 'login').send_keys(username)
    browser.find_element(By.ID, 'password').send_keys(password)
    browser.find_element(By.CLASS_NAME, 'accedi.btn.btn-primary').click()


def inside(browser, class_name, materia):
    url2 = f'https://web.spaggiari.eu/cvv/app/default/gioprof.php?classe_id=&materia=203965&ope=LEZ&codocenza=1&gruppo_id={class_name}_{materia}'
    browser.get(url2)

    ######ALTERNATIVE METHOD########
    # browser.find_element(By.XPATH, '//*[@id="data_table"]/tbody/tr[16]/td[3]/a').click()
    # url2 = browser.find_element(By.XPATH, '//*[@id="data_table"]/tbody/tr[3]/td[3]/div/div[2]/div[1]/a').click()
    # url2.format(class_name)


def downloader():
    username = user_entry.get()
    password = pass_entry.get()
    materia = materia_entry.get()
    classi = classi_entry.get()
    classi = classi.split(',')
    class_list = [j.strip() for j in classi]
    master_fun.destroy()

    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Esegui il browser in modalità headless se non hai bisogno di vedere la GUI
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    service = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service, options=options)

    # Executable part
    login(browser, username, password)
    time.sleep(5)

    lezioni_dict = {}
    # Cycle all classes
    for class_name in class_list:
        print(class_name)
        inside(browser, class_name, materia)
        time.sleep(5)

        html = browser.page_source
        soup = BeautifulSoup(html, 'html.parser')
        lezioni = soup.find_all("span", {"class": "nota_1"})
        lezioni_clean = [str(i).replace('<span class="nota_1">', '').replace('</span>', '') for i in lezioni]
        lezioni_clean.reverse()
        lezioni_dict[class_name] = lezioni_clean

    print(lezioni_dict)
    # One file per class
    for class_name in class_list:
        with open(f'lezioni_{class_name}.txt', 'w', encoding='utf-8') as f:
            for j in lezioni_dict[class_name]:
                f.write(j + '\n')
    # All classes in one file
    with open('lezioni.txt', 'w', encoding='utf-8') as f:
        for class_name in lezioni_dict:
            f.write(f'{class_name}\n')
            for j in lezioni_dict[class_name]:
                f.write(j + '\n')
            f.write('\n\n')


if __name__ == '__main__':
    master_fun = tk.Tk()
    user_entry = tk.Entry(master_fun)
    pass_entry = tk.Entry(master_fun, show='*')
    materia_entry = tk.Entry(master_fun)
    classi_entry = tk.Entry(master_fun)
    user_label = tk.Label(master_fun, text='inserire username')
    pass_label = tk.Label(master_fun, text='inserire password')
    materia_label = tk.Label(master_fun, text='la tua materia')
    classi_label = tk.Label(master_fun, text='le tue classi')
    classi = '1A_CL,1CS,1DS,1ES,1NSU_ES,2A_CL,3A_CL,3ES,4A_CL,4AS,4BS,4CS,4DS,4ES'
    classi_entry.insert(0, classi)
    user_label.pack()
    user_entry.pack()
    pass_label.pack()
    pass_entry.pack()
    materia_label.pack()
    materia_entry.pack()
    classi_label.pack()
    classi_entry.pack()
    user_entry.focus_set()

    button = tk.Button(master_fun, text="download", width=50, command=downloader)
    button.pack()

    tk.mainloop()
