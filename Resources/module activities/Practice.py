from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
#The preceding code imports your scraping tools: the Browser instance from Splinter, the Beautiful Soup object, and the driver object for Chrome (ChromeDriverManager). Notice that the code uses the soup alias so that later referencing the Beautiful Soup object will be simpler.

# Set up Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)
#The preceding code creates an instance of Splinter to prepare your automated browser. The ChromeDriverManager().install() code indicates that you'll use Chrome as your browser. And, the executable_path statement as a whole specifies that you’re installing ChromeDriver instead of manually downloading it. The headless=False argument means that all the browser's actions will display in a Chrome window so that you can observe them.

#Splinter is now controlling the browser.Although you can close the browser window at any time, it's generally best to leave it open until the session ends. Otherwise, your code might fail or generate an error.

# Visit the Quotes to Scrape site
url = 'http://quotes.toscrape.com/'
browser.visit(url)

# Parse the HTML
html = browser.html
html_soup = soup(html, 'html.parser')

# Scrape the Title
h2 = html_soup.find('h2')
title = h2.text
print(h2)
print(title)

# Scrape the top ten tags
tag_box = html_soup.find('div', class_='tags-box')
# tag_box
tags = tag_box.find_all('a', class_='tag')

for tag in tags:
    word = tag.text
    print(word)

browser.quit()