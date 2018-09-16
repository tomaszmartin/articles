from articles import markdown


def test_markdown_images():
    html = '<p><a href="/"><img src="https://sample/img.jpg" alt="text"/></a></p>'
    result = markdown.find_images(html)
    md = '![text](https://sample/img.jpg)'
    assert result == md


def test_markdown_links():
    html = '<p><a href="/">link</a></p>'
    result = markdown.find_links(html)
    md = '[link](/)'
    assert result == md
