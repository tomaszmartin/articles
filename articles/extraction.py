"""Extracting articles from web pages."""
import re

import requests
import tomd as tomd

from bs4 import BeautifulSoup
from articles.errors import BodyNotFoundError, HeaderNotFoundError

FLAGS = re.MULTILINE | re.IGNORECASE | re.DOTALL


def extract_article(html):
    """Extract the title and content from the web page."""
    head = extract_head(html)
    body = extract_body(html)
    return head, body


def to_markdown(html):
    md = tomd.Tomd(html).markdown
    # Fix img formatting
    img = re.compile(r'\[<img(.*?)alt="(.*?)"[^>]*>\]')
    md = re.sub(img, r'![\2]', md)
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
    url = 'https://www.spidersweb.pl/2018/09/iphone-xs-opinie-wrazenia.html'
    resp = requests.get(url)
    html = extract_body(resp.text)
    text = to_markdown(html)
    print(text)

