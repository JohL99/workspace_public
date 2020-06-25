import requests
import re
from bs4 import BeautifulSoup
import sys

def get_url():
    url = input("What website would you like to save?: ")
    print("url retrieved")
    return url

def get_html(url):
    filename = extract_domain(url)
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    with open("websites/"+filename+".html", "wb") as file:
        file.write(soup.prettify().encode(sys.stdout.encoding, errors='replace'))
    print("File written")

def extract_domain(url):
    return url.split("/")[2].split(".")[-2]


def main():
    get_html(get_url())

main()
