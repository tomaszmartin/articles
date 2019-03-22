"""
Creating markdown text from raw html.
"""
from copy import deepcopy
from html.parser import HTMLParser
import re


class Converter:
    """
    Responsible for converting html into markdown.
    """

    ELEMENTS = {
        'a': '[{data}]({href})',
        'abbr': '{data}',
        'address': '',
        'article': '{data}',
        'aside': '',
        'audio': '',
        'b': '**{data}**',
        # Not sure how to handle this
        'bdi': '{data}',
        # Not sure how to handle this
        'bdo': '{data}',
        'blockquote': '\n> {data}\n\n',
        'body': '{data}',
        'br': '\n{data}',
        # Not sure how to handle this
        'button': '',
        'canvas': '',
        # Not sure how to handle this
        'caption': '{data}',
        'cite': '*{data}*',
        'code': '`{data}`',
        # Not sure how to handle this
        'col': '{data}',
        # Not sure how to handle this
        'colgroup': '{data}',
        'data': '{data}',
        # Not sure how to handle this
        'dd': '{data}',
        # Not sure how to handle this
        'del': '~~{data}~~',
        # Not sure how to handle this
        'details': '',
        'dfn': '{data}',
        'dialog': '',
        'div': '{data}\n',
        # Not sure how to handle this
        'dl': '{data}',
        'dt': '{data}',
        'em': '*{data}*',
        'embed': '',
        'fieldset': '',
        'figcaption': '',
        'figure': '',
        'font': '{data}',
        'footer': '',
        'form': '',
        'frame': '',
        'frameset': '',
        'h1': '# {data}\n\n',
        'h2': '## {data}\n\n',
        'h3': '### {data}\n\n',
        'h4': '#### {data}\n\n',
        'h5': '##### {data}\n\n',
        'h6': '###### {data}\n\n',
        'head': '{data}',
        'header': '{data}',
        'hr': '\n---\n\n{data}',
        'html': '{data}',
        'i': '*{data}*',
        'iframe': '',
        'img': '![]({src})\n\n',
        'ins': '{data}',
        'kbd': '',
        'label': '',
        'legend': '',
        'li': '- {data}\n',
        'link': '',
        'main': '{data}',
        'map': '',
        'mark': '{data}',
        'meta': '',
        'meter': '',
        'nav': '',
        'noscript': '',
        'object': '',
        'ol': '\n{data}\n',
        'optgroup': '',
        'option': '',
        'output': '',
        'p': '{data}\n',
        'param': '',
        'picture': '',
        'pre': '\n```\n{data}\n```\n\n',
        'progress': '',
        'q': '\n> {data}\n\n',
        'rp': '',
        'rt': '',
        'ruby': '',
        's': '~~{data}~~',
        'samp': '\n```\n{data}\n```\n\n',
        'script': '',
        'section': '{data}',
        'select': '',
        'small': '{data}',
        'source': '',
        'span': '{data}',
        'strong': '**{data}**',
        'style': '',
        'sub': '{data}',
        'summary': '',
        'sup': '{data}',
        'svg': '',
        'table': '\n{data}\n\n',
        'tbody': '{data}',
        'td': '|{data}',
        'template': '',
        'textarea': '',
        'tfoot': '',
        'th': '|{data}',
        'thead': '{data}',
        'time': '{data}',
        'title': '{data}',
        'tr': '\n{data}',
        'track': '',
        'u': '{data}',
        'ul': '\n{data}\n',
        'var': '`{data}`',
        'video': '',
        'wbr': '{data}',
    }

    def convert(self, node):
        """
        Returns html node as markdown.
        """
        for child in node.children:
            child_content = self.convert(child)
            node.content += child_content
        result = self._convert_single_node(node)
        return result

    def _convert_single_node(self, node):
        """
        Converts single html node into markdown text.
        """
        markdown = self.ELEMENTS.get(node.name, '{data}')
        if node.name == 'a':
            node.content = re.sub(r'\n', '', node.content)
        # Column separators after head
        if node.name == 'tr':
            cols = [col for col in node.children if col.name == 'th']
            if cols:
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
        args = {'data': node.content, 'href': '', 'src': ''}
        args.update(attrs)
        # TODO: What if node has some data but not all of it
        formatted = f'{markdown.format(**args)}'
        if self._contains_information(node, formatted):
            if node.name != 'pre':
                # Strip new line with space to just newline
                formatted = re.sub(r'\n ', '\n', formatted)
                # Replace more than two newlines with single one
                formatted = re.sub(r'\n\n+', '\n\n', formatted)
            return formatted
        else:
            return ''

    def _contains_information(self, node, formatted):
        if node.name == 'br':
            return True
        markdown = self.ELEMENTS.get(node.name, '{data}')
        args = {'data': '', 'href': '', 'src': ''}
        empty = f'{markdown.format(**args)}'
        return empty != formatted


class Parser(HTMLParser):
    """Parses html and creates markdown of of it"""

    def __init__(self, *args, **kwargs):
        HTMLParser.__init__(self, *args, **kwargs)
        self.root = Node('html', {})
        self.open_tags = [self.root]

    def handle_starttag(self, tag, attrs):
        """
        Handle opening tag.
        """
        current_node = Node(tag, dict(attrs))
        try:
            self.open_tags[-1].add_child(current_node)
        except Exception as e:
            print(self.open_tags)
            raise e
        self.open_tags.append(current_node)

    def handle_data(self, data):
        """
        Handle tag data.
        """
        # When documents starts with pure text
        current_node = Node('span', {})
        if data:
            stripped = self._remove_whitespace(data)
            current_node.content += stripped
        self.open_tags[-1].add_child(current_node)

    def handle_endtag(self, tag):
        """
        Handle closing tag.
        """
        if self.open_tags:
            if self.open_tags[-1].name == tag:
                self.open_tags.pop()
    
    def _remove_whitespace(self, data):
        """
        Removes multiple whitespace from data.
        """
        spaces = re.compile(r' +', re.M)
        newlines = re.compile(r'\n+', re.M)

        stripped = re.sub(spaces, ' ', data)
        stripped = re.sub(newlines, '', stripped)
        return stripped


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
        """
        Adds a child to the node.
        """
        self.children.append(child)
        child.level += self.level + 1
        child.parent = self

    def build_tree(self, node=None):
        """
        Builds document tree for easy inspecting.
        """
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
    if not html:
        raise ValueError("Cannot create markdown from empty html.")
    parser = Parser()
    parser.feed(html)
    md = Converter().convert(parser.root)
    return md
