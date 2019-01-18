"""Creating markdown text from raw html"""
from copy import deepcopy
from html.parser import HTMLParser
import re


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
        'br': '\n{data}',
    }

    def _convert_single_node(self, node):
        """Converts html node into markdown text."""
        markdown = self.ELEMENTS.get(node.name, '{data}')
        # Column separators after head
        if node.name == 'thead':
            for child in node.children:
                if child.name == 'tr':
                    cols = [c for c in child.children
                            if c.name == 'th']
                    markdown = '{data}\n' + (len(cols) * '|:-')
        # Inline code inside multiline code
        elif node.name == 'code':
            if node.parent.name == 'pre':
                markdown = '{data}'
        # Numbering ordered lists
        elif node.name == 'li':
            if node.parent.name == 'ol':
                points = [n for n in node.parent.children
                          if n.name == 'li']
                position = points.index(node) + 1
                markdown = f'{position}. ' + '{data}\n'
        attrs = deepcopy(node.attrs)
        attrs['data'] = node.content
        formatted = f'{markdown.format(**attrs)}'
        # Strip new line with space
        formatted = re.sub(r'\n ', '\n', formatted)
        return formatted

    def convert(self, node):
        """Returns html node as markdown"""
        for child in node.children:
            child_content = self.convert(child)
            node.content += child_content
        result = self._convert_single_node(node)
        return result


class Parser(HTMLParser):
    """Parses html and creates markdown of of it"""

    def __init__(self, *args, **kwargs):
        HTMLParser.__init__(self, *args, **kwargs)
        self.root = Node('html', {})
        self.open_tags = [self.root]

    def remove_whitespace(self, data):
        spaces = re.compile(r' +', re.M)
        newlines = re.compile(r'\n+', re.M)

        stripped = re.sub(spaces, ' ', data)
        stripped = re.sub(newlines, '', stripped)
        return stripped

    def handle_starttag(self, tag, attrs):
        """Handle tag beginning."""
        current_node = Node(tag, dict(attrs))
        try:
            self.open_tags[-1].add_child(current_node)
        except Exception as e:
            print(self.open_tags)
            raise e
        self.open_tags.append(current_node)

    def handle_data(self, data):
        """Handle tag data."""
        # When documents starts with pure text
        current_node = Node('span', {})
        if data:
            stripped = self.remove_whitespace(data)
            current_node.content += stripped
        self.open_tags[-1].add_child(current_node)

    def handle_endtag(self, tag):
        """Handle tag end."""
        if self.open_tags:
            if self.open_tags[-1].name == tag:
                self.open_tags.pop()


class Node:
    """Represents an html node"""

    def __init__(self, name, attrs):
        self.name = name.lower()
        self.attrs = attrs
        self.content = ''
        self.parent = None
        self.children = []
        self.level = 0

    def __repr__(self):
        attrs = {'attrs': self.attrs, 'content': self.content}
        return f"{self.name} ({attrs})"

    def add_child(self, child):
        """Adds a child for."""
        self.children.append(child)
        child.level += self.level + 1
        child.parent = self

    def build_tree(self, node=None):
        """Builds tree for inspecting nodes tree."""
        if not node:
            node = self
        indentation = '\t' * node.level
        text = f'\n{indentation}{node}'
        for child in node.children:
            text += self.build_tree(child)
        return text


def from_html(html: str) -> str:
    """
    Converts html text into markdown.
    :param html: html string
    :return: markdown string
    """
    parser = Parser()
    parser.feed(html)
    tree = parser.root.build_tree()
    md = Converter().convert(parser.root)
    return md
