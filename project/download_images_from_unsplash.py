import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
import time

# the script to download high resoultion nature background images from unsplash.com
root_url = "https://unsplash.com" 
# load the selenium chrome webdriver
driver = webdriver.Chrome()


# the function to get the list of image of the given category link
def get_image_links_from_category(link):
    driver.get(root_url + link)
    
    # emulate the action of scrolling
    pos = 500
    while pos < int(driver.execute_script("return document.documentElement.scrollHeight")) and pos < 100000:
        driver.execute_script("console.log(document.body.scrollHeight);window.scrollTo(0, "+str(pos)+")")
        time.sleep(0.2)
        pos += 500 
    time.sleep(1)
    # get the list of images
    elements = driver.find_elements_by_tag_name('figure')
    links = []
    for el in elements:
        if el.get_attribute("innerHTML") != "null":
            soup = BeautifulSoup(el.get_attribute("innerHTML"), 'html.parser')
            lnk = soup.find("a", {"class": "_2Mc8_"})
            links.append(lnk['href'])

    return links

def get_categories():
    html = urllib.request.urlopen(root_url + "/backgrounds/nature/").read()
    soup = BeautifulSoup(html, 'html.parser')

    categories_uls = soup.find_all("ul", {"class": "_2eKZl _1q1NK _2Y-QM _1eXFm"})
    categories_links = []
    for ul in categories_uls:
        links = ul.find_all("a")
        categories_links += links
    
    return categories_links 

# from here, main code
categories_links = get_categories()
download_links = []
for cat_lnk in categories_links:
    download_links += get_image_links_from_category(cat_lnk['href'])

# download part
print('download start')
print('---------------------------------------------------------------------------')
print()
for down_lnk in download_links:
    print('download:', root_url + down_lnk)
    try:
        with urllib.request.urlopen(root_url + down_lnk +'/download?force=true') as f:
            with open('./download/' + down_lnk + '.jpg', 'wb') as i_f:
                img = f.read()
                i_f.write(img)
    except:
        pass
    print()

driver.close()

print('---------------------------------------------------------------------------')
print('download completed')
