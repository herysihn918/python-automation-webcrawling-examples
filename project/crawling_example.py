import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
## on blog.naver.com, crawl the article list of the first page of search result.
# make a URL
query_word = input('Please Input the Query Word:' )
url = f"https://search.naver.com/search.naver?where=post&sm=tab_jum&query={urllib.parse.quote_plus(query_word)}"

# get the HTML content of the URL
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

# get only <a> tags which includes title and link URL.
blog_articles = soup.find_all("a", {"class": "sh_blog_title"})
for article in blog_articles:
    print(article['title'])
    print(article['href'])
    print()

# please run this file and have a fun.... (^ _ ^)
