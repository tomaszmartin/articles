from articles.markdown import Markdown


def test_markdown_image():
    html = '<img src="https://ocs-pl.oktawave.com/iphone.jpg" ' \
           'alt="iPhone XS" ' \
           'data-pagespeed-url-hash=2676138789 ' \
           'onload="pagespeed()"/>'
    result = Markdown(html).content
    md = '![iPhone XS](https://ocs-pl.oktawave.com/iphone.jpg)'
    assert result == md


def test_markdown_image_with_params():
    html = '<img alt="Screen Shot" ' \
           'class="post-image-img attachment-large wp-post-image" ' \
           'data-ratio="1.7728531855956" ' \
           'src="https://cdn.cultofmac.com/Screen-Shot.jpg" ' \
           'title="5 reasons we expect an Apple October press event"/>'
    result = Markdown(html).content
    md = '![Screen Shot](https://cdn.cultofmac.com/Screen-Shot.jpg)'
    assert result == md


def test_markdown_image_no_domain():
    html = '<img src="/img.jpg" alt="text"/>'
    result = Markdown(html).content
    md = '![text](/img.jpg)'
    assert result == md


def test_markdown_two_images():
    html = '<img src="/1.jpg" alt="text1"/><br>' \
           '<img src="https://sample.org/2.jpg" alt="text2"/>'
    result = Markdown(html).content
    md = '![text1](/1.jpg)\n' \
         '![text2](https://sample.org/2.jpg)'
    assert result == md


def test_markdown_link():
    html = '<p>sample <a href="https://x.com/" itemprop="name">link</a></p>'
    result = Markdown(html).content
    md = 'sample [link](https://x.com/)\n'
    assert result == md


def test_markdown_hash_link():
    html = '<a href="/#disqus_thread"><span></span></a>' \
           '<a href="https://www.cultofmac.com/1">Leave a comment</a>'
    result = Markdown(html).content
    md = '[](/#disqus_thread)[Leave a comment](https://www.cultofmac.com/1)'
    assert result == md


def test_markdown_link_no_domain():
    html = '<p>sample <a href="/">link</a></p>'
    result = Markdown(html).content
    md = 'sample [link](/)\n'
    assert result == md


def test_markdown_links():
    html = '<a href="https://sample.com/first">first</a>' \
           '<a href="https://sample.com/second">second</a>'
    result = Markdown(html).content
    md = '[first](https://sample.com/first)' \
         '[second](https://sample.com/second)'
    assert result == md


def test_bold():
    html = '<div>sample <b>bold</b> <strong> again </strong></div>'
    result = Markdown(html).content
    md = 'sample **bold** ** again **'
    assert result == md


def test_italic():
    html = '<div>sample <i>bold</i> <em> again </em></div>'
    result = Markdown(html).content
    md = 'sample *bold* * again *'
    assert result == md


def test_markdown_header():
    html = '<h1>h1</h1>'
    result = Markdown(html).content
    md = '# h1\n\n'
    assert result == md


def test_markdown_headers():
    html = '<h1>h1</h1><h2>h2</h2>'
    md = Markdown(html)
    result = md.content
    print(md.tree)
    md = '# h1\n\n## h2\n\n'
    assert result == md


def test_markdown_second_header():
    html = '<h2>„Kler” na Showmax oraz DVD i Blu-Ray</h2>'
    result = Markdown(html).content
    md = '## „Kler” na Showmax oraz DVD i Blu-Ray\n\n'
    assert result == md


def test_markdown_unordered_lists():
    html = '<ul>\n<li>1</li>\n<li>2</li>\n<li>3</li>\n</ul>'
    actual = Markdown(html).content
    expected = '\n- 1\n- 2\n- 3\n'
    assert expected == actual


def test_markdown_ordered_lists():
    html = '<ol>\n<li>1</li>\n<li>2</li>\n<li>3</li>\n</ol>'
    actual = Markdown(html).content
    expected = '\n1. 1\n2. 2\n3. 3\n'
    assert expected == actual


def test_full_markdown(sample_html):
    md = Markdown(sample_html)
    actual = md.content
    expected = '**Bold text.**\n' \
               '# Header 1\n\n' \
               '## Header 2\n\n' \
               '### Header 3\n\n' \
               'Regular line\nAnother line\n' \
               'List:\n' \
               '\n' \
               '- **Bold list**\n' \
               '- Regular list\n' \
               '\n' \
               '![text](https://sample.com/img.jpg)\n' \
               '[link](/)\n'

    print(actual)
    assert expected == actual


def test_link_with_img():
    html = '<a href="https://x.com/wtf" itemprop="name">' \
           '<img alt="Author" src="https://x.com/wtf.jpg">Autor</a>'
    expected = '[![Author](https://x.com/wtf.jpg)](https://x.com/wtf)'
    actual = Markdown(html).content
    assert expected == actual
