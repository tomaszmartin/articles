"""Extracting articles from web pages."""
import requests
from bs4 import BeautifulSoup


def extract_article(content):
    """Extract the title and content from the web page."""
    head = extract_head(content)
    body = extract_body(content)
    return head, body


def extract_head(content):
    soup = BeautifulSoup(content, 'html.parser')
    header = soup.find('h1')
    return header.text


def extract_body(content):
    soup = BeautifulSoup(content, 'html.parser')
    body = soup.find('div', {'class': 'article-main'})
    return body.text


if __name__ == '__main__':
    uri = 'https://www.spidersweb.pl/2018/09/nintendo-switch-direct-wrzesien.html'
    content = requests.get(uri).content
    print(extract_head(content))
    print(extract_body(content))
