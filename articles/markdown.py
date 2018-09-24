"""Module for converting html into markdown."""
import re


def find_images(content):
    pattern = '<img[^>]+src="(.*)"[^>]+alt="(.*)"/>'
    return re.sub(pattern, r"![\2](\1)", content)


def find_links(content):
    pattern = '<a[^>]+href="(.*)">(.*)</a>'
    return re.sub(pattern, r"[\2](\1)", content)


def find_bold_text(content):
    patterns = ['<b[^>]*>(.*)</b>', '<strong[^>]*>(.*)</strong>']
    for pattern in patterns:
        content = re.sub(pattern, r"**\1**", content)
    return content


def find_italic_text(content):
    patterns = ['<i[^>]*>(.*)</i>', '<em[^>]*>(.*)</em>']
    for pattern in patterns:
        content = re.sub(pattern, r"*\1*", content)
    return content


def find_headers(content):
    patterns = {'\n#': '<h1[^>]*>(.*)</h1>', '\n##': '<h2[^>]*>(.*)</h2>',
                '\n###': '<h3[^>]*>(.*)</h3>', '\n####': '<h4[^>]*>(.*)</h4>'}
    for mark, pattern in patterns.items():
        content = re.sub(pattern, rf"{mark} \1\n", content)
    return content


def find_lists():
    pass

