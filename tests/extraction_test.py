from unittest import mock

from articles import extraction


@mock.patch('articles.extraction.extract_head')
@mock.patch('articles.extraction.extract_body')
def test_articles_extraction(mock_body, mock_head):
    mock_head.return_value = 'head'
    mock_body.return_value = 'body'
    result = extraction.extract_article('')
    assert result == ('head', 'body')
