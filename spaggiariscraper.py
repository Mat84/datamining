import selenium
import selenium.webdriver.common.keys
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType
from bs4 import BeautifulSoup
import tkinter as tk
#############################################################################

def login(browser,username,password):
    url      = 'https://web.spaggiari.eu/home/app/default/login.php?custcode='
    browser.get(url)
    browser.find_element_by_id('login').send_keys(username)
    browser.find_element_by_id('password').send_keys(password)
    browser.find_element_by_class_name('accedi.btn.btn-primary').click()


def inside(browser,class_name):
    url2 = 'https://web.spaggiari.eu/cvv/app/default/gioprof.php?classe_id=&materia=203965&ope=LEZ&codocenza=1&gruppo_id={}_RELIGIONE'.format(class_name)
    browser.get(url2)


def downloader():
    username=user_entry.get()
    password=pass_entry.get()
    classi=classi_entry.get()
    classi=classi.split(',')
    class_list=[j.strip() for j in classi]
    master_fun.destroy()

    browser = webdriver.Chrome(ChromeDriverManager().install())
    # Executable part
    login(browser,username,password)
    time.sleep(5)

    lezioni_dict={}
    # Cycle all classes    
    for class_name in class_list:
        print(class_name)
        inside(browser,class_name)
        time.sleep(5)

        html = browser.page_source
        soup = BeautifulSoup(html, 'html.parser')
        lezioni = soup.find_all("span",{"class":"nota_1"})
        lezioni_clean=[str(i).replace('<span class="nota_1">','').replace('</span>','') for i in lezioni]
        lezioni_clean.reverse()
        lezioni_dict[class_name]=lezioni_clean


    print(lezioni_dict)
    # One file per class
    for class_name in class_list:
        with open('lezioni_{}.txt'.format(class_name),'w+', encoding='utf-8') as f:
            for j in lezioni_dict[class_name]:
                f.write(j)
    # All classes in one file
    with open('lezioni.txt','w+', encoding='utf-8') as f:
        for class_name in lezioni_dict:
            f.write('{}\n'.format(class_name))
            for j in lezioni_dict[class_name]:
                f.write(j)
            f.write('\n\n')


if __name__ == '__main__':
    master_fun = tk.Tk()
    user_entry = tk.Entry(master_fun)
    pass_entry = tk.Entry(master_fun)
    classi_entry = tk.Entry(master_fun)
    user_label=tk.Label(master_fun, text = 'inserire username')
    pass_label=tk.Label(master_fun, text = 'inserire password')
    classi_label=tk.Label(master_fun, text = 'scegli le tue classi')
    classi='1AC,1AS,1BS,1DS,1ES,2AC,2AS,2AS,2DS,3AC,3AS,3BS,4AC,4AS,4BS,4DS,5AC,5BS,5DS'
    classi_entry.insert(0,classi)
    user_label.pack()
    user_entry.pack()
    pass_label.pack()
    pass_entry.pack()
    classi_label.pack()
    classi_entry.pack()
    user_entry.focus_set()

    button = tk.Button(master_fun, text = "download", width = 15, command = downloader)
    button.pack()

    tk.mainloop()




