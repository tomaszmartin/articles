from html.parser import HTMLParser
from html.entities import name2codepoint


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


class Tag:
    """Single HTML tag."""

    def __init__(self, name, attrs, children):
        self.name = name
        self.attrs = attrs
        self.children = children


class Markdown(HTMLParser):
    """Converting html text to markdown"""

    def __init__(self, *args, **kwargs):
        HTMLParser.__init__(self, *args, **kwargs)
        self.sc = 0
        self.ec = 0
        self.tags = []

    def handle_starttag(self, tag, attrs):
        self.sc += 1
        print(f"{self.sc} Start tag:", tag)

    def handle_endtag(self, tag):
        self.ec += 1
        print(f"{self.ec} End tag    :", tag)

    def handle_data(self, data):
        print("Data      :", data)

    def handle_comment(self, data):
        print("Comment   :", data)

    def handle_entityref(self, name):
        print("Named ent :", name)

    def handle_charref(self, name):
        print("Num ent   :", name)

    def handle_decl(self, data):
        print("Decl      :", data)


parser = Markdown()
parser.feed(sample)
