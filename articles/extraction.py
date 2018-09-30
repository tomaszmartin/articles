"""Extracting articles from web pages."""
import re

import requests

from articles import markdown
from articles.errors import BodyNotFoundError, HeaderNotFoundError

FLAGS = re.MULTILINE | re.IGNORECASE | re.DOTALL


def extract_article(html):
    """Extract the title and content from the web page."""
    head = extract_head(html)
    body = extract_body(html)
    return head, body


def extract_head(html):
    patterns = [r'<h1>(.*)</h1>',
                r'<header>(.*)</header>']
    for pattern in patterns:
        h1 = re.compile(pattern, FLAGS)
        head = re.search(h1, html)
        if head:
            return head.groups()[0]

    raise HeaderNotFoundError


def extract_body(html):
    patterns = [r'<section[^>]*class="article-main"[^>]*>(.*)</section>',
                r'<section[^>]*class="article"[^>]*>(.*)</section>',
                r'<section[^>]*class="pageContent"[^>]*>(.*)</section>',
                r'<div[^>]*class="article-main"[^>]*>(.*)</div>',
                r'<div[^>]*class="article"[^>]*>(.*)</div>',
                r'<div[^>]*class="pageContent"[^>]*>(.*)</div>',
                r'<div[^>]*itemprop="articleBody"[^>]*>(.*)</div>',
                r'<div[^>]*class="post-body"[^>]*>(.*)</div>',
                r'<article[^>]*>(.*)</article>']
    for pattern in patterns:
        article = re.compile(pattern, FLAGS)
        body = re.search(article, html)
        if body:
            return body.groups()[0]

    raise BodyNotFoundError


if __name__ == '__main__':
    url = 'https://www.spidersweb.pl/2018/09/iphone-xs-opinie-wrazenia.html'
    resp = requests.get(url)
    body = extract_body(resp.text)
    md = markdown.parse(url, body)
    print(md)
