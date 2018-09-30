"""Extracting articles from web pages."""
import re

import requests
import tomd as tomd

from articles import markdown
from bs4 import BeautifulSoup
from articles.errors import BodyNotFoundError, HeaderNotFoundError

FLAGS = re.MULTILINE | re.IGNORECASE | re.DOTALL


def extract_article(html):
    """Extract the title and content from the web page."""
    head = extract_head(html)
    body = extract_body(html)
    return head, body


def extract_head(html):
    soup = BeautifulSoup(html, 'html.parser')
    selectors = [{'element': 'h1', 'condition': None},
                 {'element': 'header', 'condition': None}]
    for selector in selectors:
        head = soup.find(selector['element'], selector['condition'])
        if head:
            return head.prettify()

    raise HeaderNotFoundError


def extract_body(html):
    soup = BeautifulSoup(html, 'html.parser')
    selectors = ['article', 'div[class*="article"]',
                 'div[class*="pageContent"]', 'div[class*="post-body"]',
                 'div[class*="container"]', 'div[class*="content"]']
    for selector in selectors:
        body = soup.select(selector)
        if body:
            return f'{body}'

    raise BodyNotFoundError


if __name__ == '__main__':
    url = 'http://wiadomosci.gazeta.pl/wiadomosci/7,114881,23986910,indonezja-po-przejsciu-tsunami-zdesperowani-ludzie-pladruja.html'
    resp = requests.get(url)
    html = extract_body(resp.text)
    md = markdown.parse(url, html)
    print(md)
