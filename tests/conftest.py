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

@pytest.fixture
def sample_link():
    return [
        'https://pl.wikipedia.org/wiki/Python',
        'https://realpython.com/python-type-checking/',
        'https://use-the-index-luke.com/sql/preface',
        'https://www.spidersweb.pl/2019/01/apple-abonament-na-gry-ipad-pro.html',
        'https://antyweb.pl/apple-vod-konkurenta-nowosc/',
        'https://www.cultofmac.com/603388/shark-tank-star-thinks-it-could-be-the-right-time-to-invest-in-apple/',
        'https://9to5mac.com/2019/01/29/aapl-q1-earnings/',
        'https://medium.com/s/story/if-you-only-read-a-few-books-in-2019-read-these-4533f41fe1d4',
    ]
