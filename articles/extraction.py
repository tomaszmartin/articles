"""Extracting articles from web pages."""
import re
from bs4 import BeautifulSoup
from articles.errors import BodyNotFoundError, HeaderNotFoundError
from typing import List
from urllib.parse import urlparse


FLAGS = re.MULTILINE | re.IGNORECASE | re.DOTALL


def extract_article(html: str, url: str):
    """Extract the title and content from the web page."""
    head = extract_head(html)
    body = extract_body(html, url)
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


def extract_body(html: str, url: str) -> str:
    """Extracts body from html."""
    if known_website(url):
        candidates = extract_body_from_known_website(html, url)
    else:
        candidates = extract_candidates_for_body(html)
    print(candidates)
    if not candidates:
        raise BodyNotFoundError
    body = choose_best_candidate_for_body(candidates)
    body = clean_body(body)
    return fix_relative_links(body, url)


KNOWN_DOMAINS = {
    'wikipedia.org': '.mw-parser-output',
}


def known_website(url: str) -> str:
    for domain in KNOWN_DOMAINS:
        if domain in url:
            return True


def extract_body_from_known_website(html: str, url: str) -> str:
    for domain, selector in KNOWN_DOMAINS.items():
        if domain in url:
            soup = BeautifulSoup(html, 'html.parser')
            return soup.select(selector)


def extract_candidates_for_body(html: str) -> List[str]:
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
        'div[class*="content"]',
    ]
    candidates = []
    for selector in selectors:
        bodies = soup.select(selector)
        for body in bodies:
            if body:
                candidates.append(body)
    if not candidates:
        bodies = soup.select('body')
        for boyd in bodies:
            if body:
                candidates.append(boyd)
    return candidates


def choose_best_candidate_for_body(candidates: List[str]) -> str:
    best = None
    if candidates:
        # Take the longest result based on natural text length
        for curr in candidates:
            if curr:
                if not best:
                    best = curr
                if len(curr.text) > len(best.text):
                    best = curr
        return best.decode_contents()
    raise BodyNotFoundError


def fix_relative_links(html: str, url: str) -> str:
    """
    Fixes issue with relative links, replaces
    '/index.html' with 'https://domain.com/index.html'
    """
    parsed_uri = urlparse(url)
    domain = '{uri.scheme}://{uri.netloc}'.format(uri=parsed_uri)
    soup = BeautifulSoup(html, 'html.parser')
    for a in soup.find_all('a'):
        if 'href' in a and is_relative(a['href']):
            a['href'] = url + a['href']
    for img in soup.find_all('img'):
        if is_relative(img['src']):
            img['src'] = domain + img['src']

    return soup.decode_contents()


def is_relative(url):
    """Checks whether url is relative or not."""
    return not bool(urlparse(url).netloc)


def clean_body(html: str) -> str:
    """Cleans html body from unneccesary elements."""
    soup = BeautifulSoup(html, 'html.parser')
    # Set of tags that should be removed
    to_remove = [
        'nav',
        'aside',
        'meta',
        'ins',
        'footer',
        'script',
        'table[class*="infobox"]',
        'div[class*="navigation"]',
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
        'div[class*="meta"]',
        'div[class*="noprint"]',
        'div[class*="nav"]',
        'div[id*="nav"]',
        'table[class*="nav"]',
        'span[class*="mw-editsection"]',
        'div[id*="author"]',
        'div[class*="author"]',
        'span[class*="dsq-postid"]'
    ]
    for selector in to_remove:
        for item in soup.select(selector):
            item.decompose()
    return soup.decode_contents()
