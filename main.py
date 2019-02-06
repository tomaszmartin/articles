from articles.errors import BodyNotFoundError, HeaderNotFoundError
from articles import markdown
from articles.extraction import extract_article
import requests
from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/api/markdown', methods=['GET'])
def hello():
    url = request.args.get('url')
    html = requests.get(url).text
    head, body = extract_article(html, url)
    md = markdown.from_html(body)
    # return Response(body, mimetype='text/plain')
    return Response(md, mimetype='text/plain')

if __name__ == '__main__':
    app.run(debug=True)
