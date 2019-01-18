"""Extracting articles from web pages."""
import re
from bs4 import BeautifulSoup
from articles.errors import BodyNotFoundError, HeaderNotFoundError
from articles import markdown


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


def extract_candidates_for_body(html):
    soup = BeautifulSoup(html, 'html.parser')
    selectors = [
        'article',
        'div[class*="article"]',
        'section[class*="article"]',
        'div[class*="pageContent"]',
        'section[class*="pageContent"]',
        'div[class*="post-body"]',
        'div[class*="container"]',
        'div[itemprop*="articleBody"]',
        'div[class*="content"]'
    ]
    candidates = []
    for selector in selectors:
        bodies = soup.select(selector)
        for body in bodies:
            if body:
                candidates.append(body)
    return candidates

def choose_best_candidate_for_body(candidates):
    best = None
    if candidates:
        # Take the longest result based on natural text length
        for curr in candidates:
            if curr:
                if len(curr.text) < len(best.text):
                    best = curr
            else:
                best = curr
        return best.decode_contents()
    raise BodyNotFoundError


def extract_body(html: str) - str:
    """Extracts body from html."""
    candidates = extract_candidates_for_body(html)
    return choose_best_candidate_for_body(candidates)


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
