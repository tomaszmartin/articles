"""Extracting articles from web pages."""
from bs4 import BeautifulSoup


def extract_article(content):
    """Extract the title and content from the web page."""
    head = extract_head(content)
    body = extract_body(content)
    return head, body


def extract_head(content):
    soup = BeautifulSoup(content, 'lxml')
    header = soup.find('h1')
    return header.text


def extract_body(content):
    soup = BeautifulSoup(content, 'lxml')
    header = soup.find('div', {'class': 'article-main'})
    return header.text
