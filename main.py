from articles.errors import BodyNotFoundError, HeaderNotFoundError
from articles import markdown
from articles.extraction import extract_body, extract_article
import requests
from flask import Flask, request, Response, jsonify


app = Flask(__name__)


@app.route('/api/markdown', methods=['GET'])
def get_markdown():
    url = request.args.get('url')
    html = requests.get(url).text
    head, body = extract_article(html, url)
    md_body = markdown.from_html(body)
    md_head = markdown.from_html(head)
    if request.args.get('format') == 'json':
        return jsonify({'head': md_head, 'body': md_body})
    return Response(md_head + md_body, mimetype='text/plain')

if __name__ == '__main__':
    app.run(debug=True)
