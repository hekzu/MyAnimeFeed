from jikanpy import Jikan


class AnimeEntry(object):
    def __init__(self, raw):
        self.id = raw['mal_id']
        self.title = raw['title']
        try:
            self.watched_episodes = raw['watched_episodes']
        except KeyError:
            self.watched_episodes = 0

    def __str__(self):
        return "{0} \"{1}\" {2}".format(self.id, self.title, self.watched_episodes)


class MyAnimeListAPI(object):
    def __init__(self, username):
        self._instance = Jikan()
        self._user = username

    def search(self, title):
        search_results = self._instance.search('anime', title)['results']
        entries = []

        for result in search_results:
            entries.append(AnimeEntry(result))

        return entries

    def currently_watching(self):
        response = self._instance.user(username=self._user, request="animelist", argument="watching")
        anime_list = []
        for anime in response['anime']:
            anime_list.append(AnimeEntry(anime))

        return anime_list
