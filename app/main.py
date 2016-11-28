from flask import Flask, request, jsonify
from urllib.request import urlopen
from bs4 import BeautifulSoup

app = Flask(__name__)
app.config.update(
    DEBUG=True
)

@app.route("/collector")
def index():
    url = request.args.get('url', '')
    res = collecter(url)
    return jsonify(res)

if __name__ == "__main__":
    app.run()


def collecter(url:str)->list:
    """
    画像のスクレイピングを行い、結果をlistで返す
    @param url スクレイピングしたいURL
    @return スクレイピング結果のlist
    """
    if not url:
        return []
    
    pics = []

    html = urlopen(url)
    soup = BeautifulSoup(html, "html.parser")
    for a in soup.find_all("a"):
        text = str(a.string)
        if text.endswith(("jpg", "png")):
            pics.append({"src": text})

    return pics
