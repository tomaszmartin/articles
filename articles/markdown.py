"""Module for converting html into markdown."""
import re
from urllib.parse import urlparse


flags = re.MULTILINE | re.IGNORECASE | re.DOTALL


def get_domain(url):
    parsed = urlparse(url)
    return f'{parsed.scheme}://{parsed.netloc}'


def parse_images(url, html):
    domain = get_domain(url)
    html = re.sub(r'src=(["\'])/(.*?)(\1)', rf'src="{domain}/\2"', html)
    img = re.compile(r'<img[^>]+src=(["\'])([^\1]+?)(\1)[^>]*alt=(["\'])([^\3]+?)(\3)[^>]*/>')
    html = re.sub(img, r'![\5](\2)', html)
    return html


def parse_links(url, html):
    domain = get_domain(url)
    html = re.sub(r'href="/(.*?)"', rf'href="{domain}/\1"', html)
    anchor = re.compile(r'<a[^>]*href="(.*?)"[^>]*>([^<]*?)</a>')
    if re.search(anchor, html):
        html = re.sub(anchor, r'[\2](\1)', html)
        return parse_links(url, html)
    return html


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


def parse_unordered_lists(html):
    ul = re.compile(r'<ul[^>]*>(.*?)</ul>', flags)
    li = re.compile(r'<li[^>]*>(.*?)</li>', flags)
    html = re.sub(ul, r'\1', html)
    html = re.sub(li, r'* \1', html)
    return html


def parse_ordered_lists(html):
    ol = re.compile(r'<ol[^>]*>(.*?)</ol>', flags)
    if re.match(ol, html):
        html = re.sub(ol, r'\1', html)
        elements = re.findall(r'<li>(.*?)</li>', html)
        for i, element in enumerate(elements, 1):
            html = html.replace(f'<li>{element}</li>', f'{i}. {element}')
    return html


def remove_empty_tags(html):
    # Remove scripts with content
    script = re.compile(r'<script[^>]*>(\s?)(.*?)</script[^>]*>', flags)
    html = re.sub(script, r'', html)
    # Remove other tags and extract their content
    pattern = re.compile(r'<(\w+)[^>]*>(\s?)(.*?)</(\1)[^>]*>', flags)
    if re.search(pattern, html):
        html = re.sub(pattern, r'\3', html)
        return remove_empty_tags(html)
    return html


def remove_excessive_newline(html):
    script = re.compile(r'\n\n+', flags)
    html = re.sub(script, r'\n\n', html)
    return html


def parse(url, html):
    html = parse_images(url, html)
    html = parse_bolds(html)
    html = parse_headers(html)
    html = parse_unordered_lists(html)
    html = parse_ordered_lists(html)
    html = parse_links(url, html)
    html = remove_empty_tags(html)
    html = remove_excessive_newline(html)
    return html
