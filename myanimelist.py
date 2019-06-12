from jikanpy import Jikan


class MyAnimeListAPI(object):
    def __init__(self, username):
        self._instance = Jikan()
        self._user = username

    @classmethod
    def extract_titles(cls, anime_list):
        titles = []
        for entry in anime_list:
            titles.append(entry['title'])
        return titles

    def currently_watching(self):
        response = self._instance.user(username=self._user, request="animelist", argument="watching")
        return response['anime']
