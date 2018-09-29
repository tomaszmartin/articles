"""Extracting articles from web pages."""
import re

FLAGS = re.MULTILINE | re.IGNORECASE | re.DOTALL


def extract_article(html):
    """Extract the title and content from the web page."""
    head = extract_head(html)
    body = extract_body(html)
    return head, body


def extract_head(html):
    h1 = re.compile(r'<h1>(.*)</h1>', FLAGS)
    head = re.search(h1, html)
    if head:
        return head.groups()[0]

    return None


def extract_body(html):
    article = re.compile(r'<div[^>]*class="article-main[^>]>(.*)</div>', FLAGS)
    body = re.search(article, html)
    if body:
        return body.groups()[0]

    return None
