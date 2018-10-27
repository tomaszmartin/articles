"""Creating markdown text from raw html"""
from html.parser import HTMLParser

sample = '<html>\n' \
           '<p><span><strong>Bold text.</strong></span></p>\n' \
           '<h1>Header 1</h1>\n' \
           '<h2>Header 2</h2>\n' \
           '<h3>Header 3</h3>\n' \
           '<p>Regular line\n' \
           'Another line</p>\n' \
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

    ELEMENTS = {
        'a': '[{data}]({href})',
        'img': '![{alt}]({src})',
        'h1': '# {data}',
        'h2': '## {data}',
        'h3': '### {data}',
        'h4': '### {data}',
        'li': '* {data}',
        'i': '*{data}*',
        'em': '*{data}*',
        'strong': '**{data}**',
        'b': '**{data}**',
        'blockquote': '> {data}',
        'q': '> {data}',
        'p': '{data}',
    }

    def __init__(self, *args, **kwargs):
        HTMLParser.__init__(self, *args, **kwargs)
        self.content = ''
        self.open_tags = []
        self.tree = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        attrs['data'] = ''
        self.open_tags.append({'name': tag, 'attrs': attrs})

    def handle_data(self, data):
        self.open_tags[-1]['attrs']['data'] = data

    def handle_endtag(self, tag):
        data = self.open_tags.pop()
        self.convert_tag(data)

    def convert_tag(self, element):
        markdown = self.ELEMENTS.get(element['name'], '')
        self.content += markdown.format(**element['attrs'])


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
