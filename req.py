import requests
from bs4 import BeautifulSoup

s = requests.Session()

headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
}


login_data = {
    'name': 'username',
    'pass': 'password',
    'o' : 'L2N2di9hcHAvZGVmYXVsdC9naW9wcm9mLnBocD9jbGFzc2VfaWQ9Jm1hdGVyaWE9MjAzOTY1Jm9wZT1MRVomY29kb2NlbnphPTEmZ3J1cHBvX2lkPTFBQ19SRUxJR0lPTkU='
}

#response = s.post('https://web.spaggiari.eu/home/app/default/menu_classevivadocente.php', data=login_data)
r = s.get('https://web.spaggiari.eu/cvv/app/default/gioprof.php?classe_id=&materia=203965&ope=LEZ&codocenza=1&gruppo_id=1AC_RELIGIONE')
#print(r)

import pandas as pd

df = pd.read_html('https://web.spaggiari.eu/cvv/app/default/gioprof.php?classe_id=&materia=203965&ope=LEZ&codocenza=1&gruppo_id=1AC_RELIGIONE')

print(df)


html = r.content
soup = BeautifulSoup(html, 'html.parser')

j = soup.find_all('a')


#print(j)


