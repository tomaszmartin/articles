"""Creating markdown text from raw html"""
from html.parser import HTMLParser

sample = '<html>\n' \
           '<p><span><strong>Bold text.</strong></span></p>\n' \
           '<h1>Header 1</h1>\n' \
           '<h2>Header 2</h2>\n' \
           '<h3>Header 3</h3>\n' \
           '<p>Regular line\n' \
           'Another line\n</p>' \
           '<p>List:</p>\n' \
           '<ul>\n' \
           '<li><strong>Bold list</strong></li>\n' \
           '<li>Regular list</li>\n' \
           '</ul>\n' \
           '<p><img src="https://sample.com/img.jpg" alt="text"/></p>\n' \
           '<p><a href="/">link</a></p>\n' \
           '</html>'

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
        'q': ('> ', ''),
    }
    __to_skip = [
        'style',
        'script',
    ]
    __to_extract = {
        'a': '[{data}]({link})'
    }

    def __init__(self, *args, **kwargs):
        HTMLParser.__init__(self, *args, **kwargs)
        self.content = ''
        self.open_tags = []
        self.tree = []

    def handle_starttag(self, tag, attrs):
        self.open_tags.append({'name': tag, 'attrs': attrs})

    def handle_data(self, data):
        self.open_tags[-1]['data'] = data

    def handle_endtag(self, tag):
        data = self.open_tags.pop()
        self.convert_tag(data)

    def convert_tag(self, tag):
        print(tag)


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
            self._raw = self.parser.content
        return self._raw


md = Markdown(sample)
print(md.content)
