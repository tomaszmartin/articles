from articles import markdown


def test_markdown_images():
    html = '<img src="https://sample/img.jpg" alt="text"/>'
    result = markdown.find_images(html)
    md = '![text](https://sample/img.jpg)'
    assert result == md


def test_markdown_links():
    html = '<p>sample <a href="/">link</a></p>'
    result = markdown.find_links(html)
    md = '<p>sample [link](/)</p>'
    assert result == md


def test_markdown_bold():
    html = '<div>sample <b>bold</b> <strong> again </strong></div>'
    result = markdown.find_bold_text(html)
    md = '<div>sample **bold** ** again **</div>'
    assert result == md


def test_markdown_italic():
    html = '<div>sample <i>bold</i> <em> again </em></div>'
    result = markdown.find_italic_text(html)
    md = '<div>sample *bold* * again *</div>'
    assert result == md


def test_markdown_header():
    html = '<h1>h1</h1>'
    result = markdown.find_headers(html)
    md = '\n# h1\n'
    assert result == md


def test_markdown_headers():
    html = '<h1>h1</h1><h2>h2</h2>'
    result = markdown.find_headers(html)
    md = '\n# h1\n\n## h2\n'
    assert result == md

def test_headers_add_newlines():
    html = 'sample <h1>h1</h1> sth'
    result = markdown.find_headers(html)
    md = 'sample \n# h1\n sth'
    assert result == md