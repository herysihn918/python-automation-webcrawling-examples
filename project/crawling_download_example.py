from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.parse import quote_plus

## on naver.com, search the images with the query word such as "apple" or "사과", and download all of them.
# make a URL
query_word = input('Please Input the Query Word:' )
url = f"https://search.naver.com/search.naver?where=image&sm=tab_jum&query={quote_plus(query_word)}"

print(url)

# get the HTML content of the URL
html = urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

# get the list of images
images = soup.find_all(class_="_img")

# download each images
print("Download Begun...")
print()
n = 1
for img in images:
    imgUrl = img['data-source']
    print(imgUrl)
    with urlopen(imgUrl) as f:
        with open('./../download/' + query_word + str(n) + '.jpg', 'wb') as i_f:
            img = f.read()
            i_f.write(img)
    n += 1
print()
print("Download Completed...")

# please run this file and have a fun.... (^ _ ^)

