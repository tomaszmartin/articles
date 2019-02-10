from unittest import mock

import pytest

from articles import extraction
from articles.errors import HeaderNotFoundError, BodyNotFoundError


@mock.patch('articles.extraction.extract_head')
@mock.patch('articles.extraction.extract_body')
def test_articles_extraction(mock_body, mock_head):
    mock_head.return_value = 'head'
    mock_body.return_value = 'body'
    result = extraction.extract_article('', url='')
    assert result == ('head', 'body')


def test_head_extraction():
    sample = '<html><body><h1>head</h1></body></html>'
    actual = extraction.extract_head(sample)
    assert '<h1>head</h1>' == actual


def test_empty_head_extraction():
    with pytest.raises(HeaderNotFoundError):
        extraction.extract_head('')


def test_body_extraction(sample_bodies):
    for sample in sample_bodies:
        actual = extraction.extract_body(sample, url='')
        assert 'body' == actual


def test_empty_body_extraction():
    with pytest.raises(BodyNotFoundError):
        extraction.extract_body('', url='')
