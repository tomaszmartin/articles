"""Extracting articles from web pages."""
import re
from bs4 import BeautifulSoup
from articles.errors import BodyNotFoundError, HeaderNotFoundError
from articles import markdown
import argparse
import requests

FLAGS = re.MULTILINE | re.IGNORECASE | re.DOTALL


def extract_article(html):
    """Extract the title and content from the web page."""
    head = extract_head(html)
    body = extract_body(html)
    return head, body


def extract_head(html):
    """Extracts head from html."""
    soup = BeautifulSoup(html, 'html.parser')
    selectors = ['h1', 'header']
    for selector in selectors:
        heads = soup.select(selector)
        for head in heads:
            if head:
                return f'{head}'

    raise HeaderNotFoundError


def extract_body(html):
    """Extracts body from html."""
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
                results.append(body)
    body = None
    if results:
        # Take the longest result based on natural text length
        for result in results:
            if body:
                if len(body.text) < len(result.text):
                    body = result
            else:
                body = result
    
        return body.decode_contents()

    raise BodyNotFoundError


def clean_body(html):
    """Cleans html body from unneccesary elements."""
    soup = BeautifulSoup(html, 'html.parser')
    # Set of tags that should be removed
    to_remove = [
        'nav', 
        'aside', 
        'footer',
        'div[class*="footer"]', 
        'div[class*="social-container"]',
        'div[class*="Left"]', 
        'div[class*="Share"]',
        'div[class*="embed"]',
        'div[class*="crumb"]', 
        'div[class*="sharing"]',
        'div[class*="related"]', 
        'div[class*="comments"]',
        'div[class*="widget"]', 
        'div[class*="meta"]'
    ]
    for selector in to_remove:
        for item in soup.select(selector):
            item.decompose()
    return soup.decode_contents()
