from lxml.etree import ParserError
from KissAnime import desktop


class KissAnimeAPI(object):
    def __init__(self):
        self.desktop = desktop.KissAnime()

    def search(self, title):
        try:
            return self.desktop.search(title)
        except ParserError as e:
            return []
