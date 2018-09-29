from articles import markdown


def test_markdown_image():
    uri = 'https://sample.com/wtf'
    html = '<img src="https://sample.com/img.jpg" alt="text"/>'
    result = markdown.parse_images(uri, html)
    md = '![text](https://sample.com/img.jpg)'
    assert result == md


def test_markdown_image_no_domain():
    uri = 'https://sample.com/wtf'
    html = '<img src="/img.jpg" alt="text"/>'
    result = markdown.parse_images(uri, html)
    md = '![text](https://sample.com/img.jpg)'
    assert result == md


def test_markdown_two_images():
    uri = 'https://sample.com/wtf'
    html = '<img src="/1.jpg" alt="text1"/>\n' \
           '<img src="https://sample.org/2.jpg" alt="text2"/>'
    result = markdown.parse_images(uri, html)
    md = '![text1](https://sample.com/1.jpg)\n' \
         '![text2](https://sample.org/2.jpg)'
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
