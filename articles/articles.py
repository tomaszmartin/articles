"""Extracting articles fromweb pages."""
import requests

def extract_article(uri):
    """Extract the title and content from the web page."""
    content = requests.get(uri).content
    head = extract_head(content)
    body = extract_body(content)
    return head, body


def extract_head(content):
    return None


def extract_body(content):
    return None
