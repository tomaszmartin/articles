"""Creating markdown text from raw html"""
from html.parser import HTMLParser


class MarkdownParser(HTMLParser):
    """Parses html and creates markdown of of it"""

    __defaults = ('', '')
    __to_replace = {
        'h1': ('# ', ''),
        'h2': ('## ', ''),
        'h3': ('### ', ''),
        'h4': ('#### ', ''),
        'li': ('* ', ''),
        'i': ('*', '*'),
        'em': ('*', '*'),
        'strong': ('**', '**'),
        'b': ('**', '**'),
        'blockquote': ('>', ''),
        'q': ('>', ''),
    }
    __to_skip = [
        'style',
        'script',
    ]

    def __init__(self, *args, **kwargs):
        HTMLParser.__init__(self, *args, **kwargs)
        self.skip = False
        self.md = ''

    def handle_starttag(self, tag, attrs):
        sign = self.__to_replace.get(tag, self.__defaults)[0]
        self.md += sign
        if tag in self.__to_skip:
            self.skip = True

    def handle_endtag(self, tag):
        sign = self.__to_replace.get(tag, self.__defaults)[1]
        self.md += sign
        if tag in self.__to_skip:
            self.skip = False

    def handle_data(self, data):
        if not self.skip:
            self.md += data


class Markdown:
    """Creates markdown from html"""

    def __init__(self, html):
        self.parser = MarkdownParser()
        self.html = html
        self._raw = None

    @property
    def content(self):
        if not self._raw:
            self.parser.feed(self.html)
            self._raw = self.parser.md
        return self._raw
