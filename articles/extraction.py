"""Extracting articles from web pages."""


def extract_article(content):
    """Extract the title and content from the web page."""
    head = extract_head(content)
    body = extract_body(content)
    return head, body


def extract_head(content):
    return None


def extract_body(content):
    return None
