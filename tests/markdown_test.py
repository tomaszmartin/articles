from articles import markdown


def test_domain():
    url = 'https://sample.com/wtf'
    assert markdown.get_domain(url) == 'https://sample.com'


def test_markdown_image():
    url = 'https://sample.com/wtf'
    html = '<img src="https://sample.com/img.jpg" alt="text"/>'
    result = markdown.parse_images(url, html)
    md = '![text](https://sample.com/img.jpg)'
    assert result == md


def test_markdown_image_no_domain():
    url = 'https://sample.com/wtf'
    html = '<img src="/img.jpg" alt="text"/>'
    result = markdown.parse_images(url, html)
    md = '![text](https://sample.com/img.jpg)'
    assert result == md


def test_markdown_two_images():
    url = 'https://sample.com/wtf'
    html = '<img src="/1.jpg" alt="text1"/>\n' \
           '<img src="https://sample.org/2.jpg" alt="text2"/>'
    result = markdown.parse_images(url, html)
    md = '![text1](https://sample.com/1.jpg)\n' \
         '![text2](https://sample.org/2.jpg)'
    assert result == md


def test_markdown_link():
    url = 'https://sample.com/wtf'
    html = '<p>sample <a href="https://sample.com/">link</a></p>'
    result = markdown.parse_links(url, html)
    md = '<p>sample [link](https://sample.com/)</p>'
    assert result == md


def test_markdown_link_no_domain():
    url = 'https://sample.com/wtf'
    html = '<p>sample <a href="/">link</a></p>'
    result = markdown.parse_links(url, html)
    md = '<p>sample [link](https://sample.com/)</p>'
    assert result == md


def test_markdown_links():
    url = 'https://sample.com/wtf'
    html = '<p>sample <a href="/">link1</a></p>\n' \
           '<a href="https://sample.org/">link2</a></p>'
    result = markdown.parse_links(url, html)
    md = '<p>sample [link1](https://sample.com/)</p>\n' \
         '[link2](https://sample.org/)</p>'
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
    html = '<ul>\n<li>1</li>\n<li>2</li>\n<li>3</li>\n</ul>'
    actual = markdown.parse_unordered_lists(html)
    expected = '\n* 1\n* 2\n* 3\n'
    assert expected == actual


def test_markdown_ordered_lists():
    html = '<ol>\n<li>1</li>\n<li>2</li>\n<li>3</li>\n</ol>'
    actual = markdown.parse_ordered_lists(html)
    expected = '\n1. 1\n2. 2\n3. 3\n'
    assert expected == actual


def test_full_markdown(sample_html):
    url = 'https://sample.com/wtf'
    actual = markdown.parse(url, sample_html)
    expected = '**Bold text.**\n' \
               '# Header 1\n' \
               '## Header 2\n' \
               '### Header 3\n' \
               'List:\n' \
               '\n' \
               '* **Bold list**\n' \
               '* Regular list\n' \
               '\n' \
               '![text](https://sample.com/img.jpg)\n' \
               '[link](https://sample.com/)\n'
    assert expected == actual
