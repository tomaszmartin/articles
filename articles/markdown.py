"""Module for converting html into markdown."""
import re


def parse_images(content):
    pattern = '<img[^>]+src="(.*)"[^>]+alt="(.*)"/>'
    return re.sub(pattern, r'![\2](\1)', content)


def parse_links(content):
    pattern = '<a[^>]+href="(.*)">(.*)</a>'
    return re.sub(pattern, r'[\2](\1)', content)


def parse_bolds(content):
    patterns = ['<b[^>]*>(.*)</b>', '<strong[^>]*>(.*)</strong>']
    for pattern in patterns:
        content = re.sub(pattern, r'**\1**', content)
    return content


def parse_italics(content):
    patterns = ['<i[^>]*>(.*)</i>', '<em[^>]*>(.*)</em>']
    for pattern in patterns:
        content = re.sub(pattern, r'*\1*', content)
    return content


def parse_headers(content):
    patterns = {'#': '<h1[^>]*>(.*)</h1>',
                '##': '<h2[^>]*>(.*)</h2>',
                '###': '<h3[^>]*>(.*)</h3>',
                '####': '<h4[^>]*>(.*)</h4>'}
    for mark, pattern in patterns.items():
        content = re.sub(pattern, rf'{mark} \1', content)
    return content


def find_lists():
    pass

