import pytest


@pytest.fixture
def sample_html():
    return '<html>\n' \
           '<p><span><strong>Bold text.</strong></span></p>\n' \
           '<h1>Header 1</h1>\n' \
           '<h2>Header 2</h2>\n' \
           '<h3>Header 3</h3>\n' \
           '<p>List:</p>\n' \
           '<ul>\n' \
           '<li><strong>Bold list</strong></li>\n' \
           '<li>Regular list</li>\n' \
           '</ul>\n' \
           '<p><img src="https://sample.com/img.jpg" alt="text"/></p>\n' \
           '<p><a href="/">link</a></p>\n' \
           '</html>'
