from html.parser import HTMLParser

from data import sample_html


class MarkdownParser(HTMLParser):
    """Converting html text to markdown"""

    __tags__ = {
        'h1': ('# ', ''),
        'h2': ('## ', ''),
        'h3': ('### ', ''),
        'h4': ('#### ', ''),
        'li': ('* ', ''),
        'strong': ('**', '**'),
    }

    def __init__(self, *args, **kwargs):
        HTMLParser.__init__(self, *args, **kwargs)
        self.md = ''

    def handle_starttag(self, tag, attrs):
        sign = self.__tags__.get(tag, ('', ''))[0]
        self.md += sign

    def handle_endtag(self, tag):
        sign = self.__tags__.get(tag, ('', ''))[1]
        self.md += sign

    def handle_data(self, data):
        self.md += data


class Markdown:

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


md = Markdown(sample_html)
print(md.content)
