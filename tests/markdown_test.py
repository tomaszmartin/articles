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
    html = '<div>sample <b>bold</b></div>'
    result = markdown.find_bold_text(html)
    md = '<div>sample **bold**</div>'
    assert result == md