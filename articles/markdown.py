"""Creating markdown text from raw html"""
from html.parser import HTMLParser


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


class Node:
    """Represents an html node"""

    def __init__(self, name, attrs):
        self.name = name
        self.attrs = attrs
        self.parent = None
        self.content = None
        self.children = []
        self.level = 0

    def add_child(self, child):
        self.children.append(child)
        child.parent = self
        child.level += self.level + 1

    def __repr__(self):
        attrs = {'name': self.name,
                 'attrs': self.attrs,
                 'content': self.content,
                 'children': len(self.children)}
        return f"{self.__class__.__name__}('{attrs}')"

    def build_node_repr(self, node):
        indentation = '\t' * node.level
        text = f'\n{indentation}{node}'
        for child in node.children:
            text += self.build_node_repr(child)
        return text

    @property
    def tree_string(self):
        return self.build_node_repr(self)


class Parser(HTMLParser):
    """Parses html and creates markdown of of it"""

    def __init__(self, *args, **kwargs):
        HTMLParser.__init__(self, *args, **kwargs)
        self.content = ''
        self.open_tags = []
        self.root = None

    def handle_starttag(self, tag, attrs):
        current_node = Node(tag, dict(attrs))
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
        self.open_tags[-1].content = data

    def handle_endtag(self, tag):
        # print(self.root.print_tree())
        self.open_tags.pop()


html = open('sample.html').read()
parser = Parser()
parser.feed(html)
print(parser.root.tree_string)
