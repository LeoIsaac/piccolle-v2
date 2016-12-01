from urllib.request import urlopen
from bs4 import BeautifulSoup

class Board():
    def getList(self) -> list:
        """
        掲示板のリストをlistにして返す
        @return list
        """
        url = "https://2ch.sc/bbstable.html"
        pics = []

        html = urlopen(url)
        soup = BeautifulSoup(html, "html.parser")
        json = []
        count = 0

        for b in soup.find_all('b'):
            json.append({"category": b.text, "boards": []})
            for a in b.find_next_siblings():
                if a.name == 'b': break
                json[count]["boards"].append({"url": a.get("href"), "board": a.text})
            count += 1

        return json