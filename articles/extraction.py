"""Extracting articles from web pages."""
import re

import requests
import tomd as tomd

from bs4 import BeautifulSoup

from articles import markdown
from articles.errors import BodyNotFoundError, HeaderNotFoundError

FLAGS = re.MULTILINE | re.IGNORECASE | re.DOTALL


def extract_article(html):
    """Extract the title and content from the web page."""
    head = extract_head(html)
    body = extract_body(html)
    return head, body


def to_markdown(html):
    md = tomd.Tomd(html).markdown
    return md


def extract_head(html):
    soup = BeautifulSoup(html, 'html.parser')
    selectors = ['h1', 'header']
    for selector in selectors:
        heads = soup.select(selector)
        for head in heads:
            if head:
                return f'{head}'

    raise HeaderNotFoundError


def extract_body(html):
    soup = BeautifulSoup(html, 'html.parser')
    selectors = ['article', 'div[class*="article"]', 'section[class*="article"]',
                 'div[class*="pageContent"]', 'section[class*="pageContent"]',
                 'div[class*="post-body"]', 'div[class*="container"]',
                 'div[itemprop*="articleBody"]', 'div[class*="content"]']
    results = []
    for selector in selectors:
        bodies = soup.select(selector)
        for body in bodies:
            if body:
                results.append(body.decode_contents())
    if results:
        # Take the longest result
        return max(results, key=len)

    raise BodyNotFoundError


if __name__ == '__main__':
    url = 'https://antyweb.pl/kler-online-showmax-premiera-dvd-bluray/'
    resp = requests.get(url)
    html = extract_body(resp.text)
    md = markdown.parse(url, html)

