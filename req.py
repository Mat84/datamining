import requests
from bs4 import BeautifulSoup

BASE_URL = "https://web.spaggiari.eu/cvv/app/default/gioprof.php?classe_id=&materia=203965&ope=LEZ&codocenza=1&gruppo_id=5DS_RELIGIONE"
response = requests.get(BASE_URL + "index.html")
html = response.content
soup = BeautifulSoup(html, 'html.parser')

r = soup.select('tbody tr td')





# row = r[0]
# name = row.select_one('.source-title').text.strip()
# print(name)




