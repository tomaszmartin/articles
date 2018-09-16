"""Extracting articles fromweb pages."""
import requests

def extract_article(uri):
    """Extract the title and content from the web page."""
    content = requests.get(uri).content
