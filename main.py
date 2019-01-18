from articles.errors import BodyNotFoundError, HeaderNotFoundError
from articles import markdown
from articles.extraction import extract_article
import argparse
import requests

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert web page into markdown article.')
    parser.add_argument('--url', type=str, help='Url address of the web page.')

    args = parser.parse_args()
    html = requests.get(args.url).content
    head, body = extract_article(html)
    md = markdown.from_html(body)
    print(md)
