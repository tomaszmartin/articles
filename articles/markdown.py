"""Module for converting html into markdown."""
import re
from urllib.parse import urlparse


def parse_images(url, html):
    parsed = urlparse(url)
    domain = f'{parsed.scheme}://{parsed.netloc}'
    html = re.sub(r'src="/(.*?)"', rf'src="{domain}/\1"', html)
    html = re.sub(r'<img[^>]+src="(.*)"[^>]+alt="(.*)"/>',
                  r'![\2](\1)', html)
    return html


def parse_links(content):
    return re.sub(r'<a[^>]+href="(.*)">(.*)</a>',
                  r'[\2](\1)',
                  content)


def parse_bolds(content):
    patterns = [r'<b[^>]*>(.*)</b>', r'<strong[^>]*>(.*)</strong>']
    for pattern in patterns:
        content = re.sub(pattern, r'**\1**', content)
    return content


def parse_italics(content):
    patterns = [r'<i[^>]*>(.*)</i>', r'<em[^>]*>(.*)</em>']
    for pattern in patterns:
        content = re.sub(pattern, r'*\1*', content)
    return content


def parse_headers(content):
    patterns = {'#': r'<h1[^>]*>(.*)</h1>',
                '##': r'<h2[^>]*>(.*)</h2>',
                '###': r'<h3[^>]*>(.*)</h3>',
                '####': r'<h4[^>]*>(.*)</h4>'}
    for mark, pattern in patterns.items():
        content = re.sub(pattern, rf'{mark} \1', content)
    return content


def parse_unordered_lists(content):
    content = re.sub(r'<ul[^>]*>(.*?)</ul>', r'\1', content)
    content = re.sub(r'<li>(.*?)</li>', r'* \1\n', content)
    return content


def parse_ordered_lists(content):
    content = re.sub(r'<ol[^>]*>(.*?)</ol>', r'\1', content)
    elements = re.findall(r'<li>(.*?)</li>', content)
    result = ''
    for i, element in enumerate(elements, 1):
        result += f'{i}. {element}\n'
    return result
