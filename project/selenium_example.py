from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver

# please download chrome driver from https://chromedriver.chromium.org/ and copy it to the /project folder.

# make URL
query_word = input('Please Input the Query Word:' )
url = f"https://www.google.com/search?q={quote_plus(query_word)}"

# open google chrome browser with selenium
driver = webdriver.Chrome()
# input URL on the browser's url input box
driver.get(url)

# get the html content of the browser
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

# get the list of necessary part of the html content
r_list = soup.select('.r')
for r in r_list:
    print('Title:',r.select_one('.LC20lb').text)
    print('Link:', r.select_one('a')['href'])
    print()

# close the browswer
driver.close()

# please run this file and have a fun... (^ _ ^)