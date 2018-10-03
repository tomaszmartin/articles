
"""Module for converting html into markdown."""
import re
from urllib.parse import urlparse


flags = re.MULTILINE | re.IGNORECASE | re.DOTALL
attribute_pattern = r'{0}=(["\'])(?P<{0}>[^\1]*?)(\1)[^>]*'


def get_domain(url):
    parsed = urlparse(url)
    return f'{parsed.scheme}://{parsed.netloc}'


def parse_images(url, html):
    domain = get_domain(url)
    # Substitute relative urls with a full ones
    html = re.sub(r'src=(["\'])/(.*?)(\1)', rf'src="{domain}/\2"', html)
    # Define needed attributes
    src = attribute_pattern.format('src')
    alt = attribute_pattern.format('alt')
    # Check regardless of position
    for pattern in (rf'<img[^>]+{src}{alt}/?>', rf'<img[^>]+{alt}{src}/?>'):
        html = re.sub(pattern, r'![\g<alt>](\g<src>)', html)

    return html


def parse_links(url, html):
    domain = get_domain(url)
    # Remove empty links
    html = re.sub(r'(<a[^>]*><(\w+)[^>]*></(\2)></a>)', r'', html)
    html = re.sub(r'href="/(.*?)"', rf'href="{domain}/\1"', html)
    parsed_img = r'(!\[(?P<alt>[^\]]+)\]\((?P<src>[^\)]*)\))'
    anchor_with_img = re.compile(rf'<a[^>]*href="(?P<href>[^"]*?)"[^>]*>{parsed_img}(?P<text>[^<]*)</a>')
    html = re.sub(anchor_with_img, r'[![\g<text>](\g<src>)](\g<href>)', html)
    anchor = re.compile(r'<a[^>]*href="([^"]*?)"[^>]*>([^<]*?)</a>')
    html = re.sub(anchor, r'[\2](\1)', html)
    return html


def parse_bolds(content):
    patterns = [r'<b[^>]*>([^<]*)</b>', r'<strong[^>]*>([^<]*)</strong>']
    for pattern in patterns:
        patt = re.compile(pattern, flags)
        content = re.sub(patt, r'**\1**', content)
    return content


def parse_italics(content):
    patterns = [r'<i[^>]*>(.*)</i>', r'<em[^>]*>(.*)</em>']
    for pattern in patterns:
        content = re.sub(pattern, r'*\1*', content)
    return content


def parse_headers(content):
    patterns = {'#': r'<h1[^>]*>(\s*)?(.*?)</h1>',
                '##': r'<h2[^>]*>(\s*)?(.*?)</h2>',
                '###': r'<h3[^>]*>(\s*)?(.*?)</h3>',
                '####': r'<h4[^>]*>(\s*)?(.*?)</h4>'}
    for mark, pattern in patterns.items():
        patt = re.compile(pattern, flags)
        content = re.sub(patt, rf'{mark} \2', content)
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


def remove_script_tags(html):
    # Remove scripts with content
    script = re.compile(r'<script[^>]*>(.*?)</script[^>]*>', flags)
    html = re.sub(script, r'', html)
    script = re.compile(r'<style[^>]*>(.*?)</style[^>]*>', flags)
    html = re.sub(script, r'', html)
    return html


def remove_empty_tags(html):
    # Remove other tags and extract their content
    pattern = re.compile(r'<(\w+)[^>]*>(\s?)(.*?)</(\1)[^>]*>', flags)
    if re.search(pattern, html):
        html = re.sub(pattern, r'\3', html)
        return remove_empty_tags(html)
    return html


def remove_single_tags(html):
    # Remove other tags and extract their content
    pattern = re.compile(r'<(\w+)[^>]*>[^\S\n]*')
    html = re.sub(pattern, r'', html)
    pattern = re.compile(r'</(\w+)[^>]*>[^\S\n]*', flags)
    html = re.sub(pattern, r'', html)
    return html


def remove_excessive_whitespace(html):
    script = re.compile(r'(\s\s)(\s*)([^\s])', re.MULTILINE)
    html = re.sub(script, r'\n\n\3', html)
    return html


def remove_comments(html):
    comment = re.compile(r'<!--(.*?)-->', flags)
    html = re.sub(comment, r'', html)
    return html


def remove_captions(html):
    caption = re.compile(r'<figcaption[^>]*>(.*?)</figcaption[^>]*>', flags)
    html = re.sub(caption, r'', html)
    return html


def parse(url, html):
    html = remove_script_tags(html)
    html = parse_images(url, html)
    html = parse_links(url, html)
    html = parse_bolds(html)
    html = parse_headers(html)
    html = parse_unordered_lists(html)
    html = parse_ordered_lists(html)
    html = remove_comments(html)
    html = remove_captions(html)
    html = remove_single_tags(html)
    html = remove_empty_tags(html)
    html = remove_excessive_whitespace(html)
    return html.strip()