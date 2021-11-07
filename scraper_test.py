from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
from urllib.error import URLError, HTTPError


class Scraper:

    def __init__(self, url):
        self.url = url
        self._headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:94.0) Gecko/20100101 Firefox/94.0'}


    def html_treatment(self, html):
        html = html.decode('utf-8')
        html = " ".join(html.split())
        html = html.replace('> <', '><')
        return html


    @property
    def http_response(self):
        content = []
        
        try:
            req = Request(self.url, headers = self._headers)
            response = urlopen(req)
            html = self.html_treatment(response.read())

        except HTTPError as e:
            return (e.status, e.reason)

        except URLError as e:
            return (e.reason)

        soup = BeautifulSoup(html, 'html.parser')


        content.append(soup.findAll('h3'))
        content.append(soup.findAll('img'))

        return content
