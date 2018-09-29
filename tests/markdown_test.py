from articles import markdown


def test_markdown_images():
    html = '<img src="https://sample/img.jpg" alt="text"/>'
    result = markdown.parse_images(html)
    md = '![text](https://sample/img.jpg)'
    assert result == md


def test_markdown_links():
    html = '<p>sample <a href="/">link</a></p>'
    result = markdown.parse_links(html)
    md = '<p>sample [link](/)</p>'
    assert result == md


def test_markdown_bold():
    html = '<div>sample <b>bold</b> <strong> again </strong></div>'
    result = markdown.parse_bolds(html)
    md = '<div>sample **bold** ** again **</div>'
    assert result == md


def test_markdown_italic():
    html = '<div>sample <i>bold</i> <em> again </em></div>'
    result = markdown.parse_italics(html)
    md = '<div>sample *bold* * again *</div>'
    assert result == md


def test_markdown_header():
    html = '<h1>h1</h1>'
    result = markdown.parse_headers(html)
    md = '# h1'
    assert result == md


def test_markdown_headers():
    html = '<h1>h1</h1>\n<h2>h2</h2>'
    result = markdown.parse_headers(html)
    md = '# h1\n## h2'
    assert result == md


def test_markdown_unordered_lists():
    html = '<ul><li>1</li><li>2</li><li>3</li></ul>'
    result = markdown.parse_unordered_lists(html)
    md = '* 1\n* 2\n* 3\n'
    assert result == md


def test_markdown_ordered_lists():
    html = '<ul><li>1</li><li>2</li><li>3</li></ul>'
    result = markdown.parse_ordered_lists(html)
    md = '1. 1\n2. 2\n3. 3\n'
    assert result == md
