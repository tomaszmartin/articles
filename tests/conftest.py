import pytest
from pathlib import Path


@pytest.fixture
def sample_html():
  main = Path(__file__).parent
  return open(main / 'sample.html').read()


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
