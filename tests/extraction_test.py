from unittest import mock

from articles import extraction


@mock.patch('articles.extraction.extract_head')
@mock.patch('articles.extraction.extract_body')
def test_articles_extraction(mock_body, mock_head):
    mock_head.return_value = 'head'
    mock_body.return_value = 'body'
    result = extraction.extract_article('')
    assert result == ('head', 'body')


def test_head_extraction():
    sample = '<html><body><h1>head</h1></body></html>'
    result = extraction.extract_head(sample)
    assert result == 'head'


def test_body_extraction():
    sample = '<html><body><div class="article-main">body</div></body></html>'
    result = extraction.extract_body(sample)
    assert result == 'body'