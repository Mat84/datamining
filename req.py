import requests
from bs4 import BeautifulSoup

BASE_URL = "https://web.spaggiari.eu/cvv/app/default/gioprof.php?classe_id=&materia=203965&ope=LEZ&codocenza=1&gruppo_id=5DS_RELIGIONE"
response = requests.get(BASE_URL + "index.html")
html = response.content
soup = BeautifulSoup(html, 'html.parser')

r = soup.select('tbody tr td')

span



# row = r[0]
# name = row.select_one('.source-title').text.strip()
# print(name)



















#title_descriptions = []
#
#articles = scraped.select(".product_pod")
#
#for article in articles:
#    title = article.h3.a["title"]
#    title_url = article.h3.a["href"]
#    
#    product_response = requests.get(BASE_URL + title_url)
#    product_html = product_response.content
#    product_scraped = BeautifulSoup(product_html, 'html.parser')
#    
#    description = product_scraped.find("div", id="product_description").next_sibling.next_sibling
#    
#    title_descriptions.append({title: description.text.strip()})
#    
#print(title_descriptions)