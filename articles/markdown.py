"""Creating markdown text from raw html"""
from html.parser import HTMLParser


class Node:
    """Represents an html node"""

    def __init__(self, name, attrs, content='', parent=None, children=None):
        self.name = name
        self.attrs = attrs
        self.content = content
        self.parent = parent
        self.children = children


class Writer:
    """Responsible for writing html nodes as markdown"""

    ELEMENTS = {
        'a': '[{data}]({href})',
        'img': '![{alt}]({src})',
        'h1': '# {data}',
        'h2': '## {data}',
        'h3': '### {data}',
        'h4': '#### {data}',
        'li': '- {data}',
        'i': '*{data}*',
        'em': '*{data}*',
        'strong': '**{data}**',
        'b': '**{data}**',
        'blockquote': '> {data}',
        'q': '> {data}',
        'p': '{data}',
        'code': '`{data}`',
        'pre': '```\n{data}\n```',
        'ins': '{data}',
        'del': '',
    }

    def write(self, node):
        """Returns html node as markdown"""
        pass


class Parser(HTMLParser):
    """Parses html and creates markdown of of it"""

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
        if self.open_tags:
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
        self.parser = Parser()
        self.html = html
        self._raw = None

    @property
    def content(self):
        if not self._raw:
            self.parser.feed(self.html)
            self._raw = self.parser.content
        return self._raw


html = open('sample.html').read()
md = Markdown(html)
print(md.content)
