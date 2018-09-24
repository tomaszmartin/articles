"""Module for converting html into markdown."""
import re


def find_images(content):
    pattern = '<img[^>]+src="(.*)"[^>]+alt="(.*)"/>'
    return re.sub(pattern, r"![\2](\1)", content)


def find_links(content):
    pattern = '<a[^>]+href="(.*)">(.*)</a>'
    return re.sub(pattern, r"[\2](\1)", content)


def find_bold_text(content):
    pattern = '<b[^>]*>(.*)</b>'
    return re.sub(pattern, r"**\1**", content)


def find_italic_text():
    pass


def find_headers():
    pass


def find_lists():
    pass

