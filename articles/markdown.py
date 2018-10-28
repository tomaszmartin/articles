"""Creating markdown text from raw html"""
from copy import deepcopy
from html.parser import HTMLParser


class Converter:
    """Responsible for converting html nodes into markdown"""

    ELEMENTS = {
        'h1': '# {data}\n\n',
        'h2': '## {data}\n\n',
        'h3': '### {data}\n\n',
        'h4': '#### {data}\n\n',
        'h5': '##### {data}\n\n',
        'h6': '###### {data}\n\n',
        'ul': '\n{data}',
        'ol': '\n{data}',
        'li': '- {data}\n',
        'i': '*{data}*',
        'em': '*{data}*',
        'strong': '**{data}**',
        'b': '**{data}**',
        'blockquote': '\n> {data}\n\n',
        'q': '\n> {data}\n\n',
        'p': '{data}\n',
        'code': '`{data}`',
        'pre': '\n```\n{data}\n```\n\n',
        'ins': '{data}',
        'del': '~~{data}~~',
        'a': '[{data}]({href})',
        'img': '![{alt}]({src})',
        'span': '{data}',
        'hr': '\n---\n\n',
        'th': '|{data}',
        'thead': '{data}',
        'tr': '\n{data}',
        'td': '|{data}',
    }

    def convert_node(self, node):
        md = self.ELEMENTS.get(node.name, '{data}')
        postfix = ''
        if node.name == 'thead':
            cols = len(node.children[0].children)
            postfix = '\n' + (cols * '|:-')
        elif node.name == 'code':
            if node.parent.name == 'pre':
                md = '{data}'
        elif node.name == 'li':
            if node.parent.name == 'ol':
                points = [n for n in node.parent.children if n.name == 'li']
                position = points.index(node) + 1
                md = f'{position}. ' + '{data}\n'
        attrs = deepcopy(node.attrs)
        attrs['data'] = node.content
        return f'{md.format(**attrs)}{postfix}'

    def convert(self, node):
        """Returns html node as markdown"""
        for child in node.children:
            node.content += self.convert(child)
        result = self.convert_node(node)
        return result


class Parser(HTMLParser):
    """Parses html and creates markdown of of it"""

    def __init__(self, *args, **kwargs):
        HTMLParser.__init__(self, *args, **kwargs)
        self.open_tags = []
        self.root = None
        self.just_opened = None

    @property
    def result(self):
        return self.root

    def handle_starttag(self, tag, attrs):
        current_node = Node(tag, dict(attrs))
        self.just_opened = True
        if not self.root:
            self.root = current_node
        else:
            self.open_tags[-1].add_child(current_node)
        self.open_tags.append(current_node)

    def handle_data(self, data):
        # When documents starts with pure text
        if not self.open_tags:
            current_node = Node('html', {})
            self.root = current_node
            self.open_tags.append(current_node)
        if self.just_opened:
            if True:  # data.strip():
                self.open_tags[-1].content += data
        else:
            if True:  # data.strip():
                current_node = Node('span', {})
                current_node.content += data
                self.open_tags[-1].add_child(current_node)

    def handle_endtag(self, tag):
        # print(self.root.print_tree())
        self.just_opened = False
        self.open_tags.pop()


class Node:
    """Represents an html node"""

    def __init__(self, name, attrs):
        self.name = name.lower()
        self.attrs = attrs
        self.parent = None
        self.content = ''
        self.children = []
        self.level = 0
        self.closed = False

    def __repr__(self):
        attrs = {'attrs': self.attrs, 'content': self.content}
        return f"{self.name} ({attrs})"

    def add_child(self, child):
        self.children.append(child)
        child.level += self.level + 1
        child.parent = self

    def build_tree(self, node=None):
        if not node:
            node = self
        indentation = '\t' * node.level
        text = f'\n{indentation}{node}'
        for child in node.children:
            text += self.build_tree(child)
        return text


html = open('sample.html').read()
parser = Parser()
converter = Converter()
parser.feed(html)
tree = parser.result.build_tree()
markdown = converter.convert(parser.result)
print(markdown)

