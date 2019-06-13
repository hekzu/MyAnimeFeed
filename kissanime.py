from lxml.etree import ParserError
from KissAnime import desktop


class KissAnimeResult(object):
    def __init__(self, raw):
        self.title = raw.title.decode('ascii')
        self.url = raw.url.decode('ascii')

    def __str__(self):
        return "{0} {1}".format(self.title, self.url)


class KissAnimeAPI(object):
    def __init__(self):
        self.desktop = desktop.KissAnime()

    def get_anime_info(self, anime):
        return self.desktop.get_anime_info(anime.url)

    def retry(self, title):
        for i in range(len(title)):
            if title[i].isdigit():
                digit = title[i]
                series_name = title[:i]
                result_list = self.search(series_name)
                for result in result_list:
                    if digit in result.title:
                        return [result]
        return []

    def search(self, title):
        try:
            result_list = self.desktop.search(title)
            parsed_results = []
            for result in result_list:
                parsed_results.append(KissAnimeResult(result))
            return parsed_results
        except ParserError:
            return self.retry(title)
