import requests
from bs4 import BeautifulSoup

# using requests module we use the get function
# provided to access the webpage provided as an argument to the is function
result = requests.get('https://www.google.com/')

# to make sure that the website is accessible, we can ensure that
# print(result.status_code)
# we can check HTTP header of the website to verify that we have indeed accessed the correct page
# print(result.headers)
# to extract the content of the page
# print(result.content)
src = result.content
#Now that we have the page source stored, we will use the
# Beautifulsoup module to parse and process the source
#pip install lxml
#What is lxml used for?
#lxml is a Python library which allows for easy handling of XML and HTML files, and can also be used for web scraping.
soup = BeautifulSoup(src,'lxml')
# print(soup.prettify())
# now the page source has been processed via Beautifulsoup
# we can access specific information directly from it
# for eg: if we want to see a list of all the links on the page

links = soup.find_all('a')
# print(links)
# if we just want to extract the link that has contains the text
# "About" on the pafe instead of every link.
# we can use the built-in "text function" to access the text content between <a> </a> tags
for link in links:
    if "About" in link.text:
        print(link)
        print(link.attrs['href'])

