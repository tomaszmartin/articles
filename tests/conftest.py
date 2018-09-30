import pytest


@pytest.fixture
def sample_html():
    return '<html>\n' \
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


@pytest.fixture
def sample_bodies():
    bodies = ['<html><body><section class="article-main">body</section></body></html>',
              '<html><body><section class="article">body</section></body></html>',
              '<html><body><section class="pageContent">body</section></body></html>',
              '<html><body><div class="article-main">body</div></body></html>',
              '<html><body><div class="article">body</div></body></html>',
              '<html><body><div class="pageContent">body</div></body></html>',
              '<html><body><div itemprop="articleBody">body</div></body></html>',
              '<html><body><div class="post-body">body</div></body></html>',
              '<html><body><article>body</article></body></html>']
    return bodies
