"""Module for converting html into markdown."""
from bs4 import BeautifulSoup


def find_images(content):
    soup = BeautifulSoup(content, 'html.parser')
    img = soup.find('img')
    return f'![{img["alt"]}]({img["src"]})'


def find_links(content):
    soup = BeautifulSoup(content, 'html.parser')
    anchor = soup.find('a')
    return f'[{anchor.text}]({anchor["href"]})'


def find_bold_text():
    pass


def find_italic_text():
    pass


def find_headers():
    pass


def find_lists():
    pass

