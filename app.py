from PyQt5.QtWidgets import QApplication
from myanimelist import MyAnimeListAPI
from argparse import ArgumentParser
from kissanime import KissAnimeAPI
from messagebox import MessageBox
from config import ARGUMENT_LIST
import sys


def select_result(mal, result_list, anime):
    shortest_result = None
    for result in result_list:
        if shortest_result is None:
            shortest_result = result
        else:
            if len(shortest_result.title) >= len(result.title):
                if len(result_list) > 1:
                    if "Sub" in result.title:
                        shortest_result = result
                else:
                    shortest_result = result

    mal_results = mal.search(shortest_result.title)
    for mal_res in mal_results:
        if mal_res.title == anime.title:
            return shortest_result


def create_popup(message_list):
    text = "\n".join(message_list)
    app = QApplication(sys.argv)
    MessageBox("MyAnimeFeed", text)
    app.exec_()


def main():
    arg_parser = ArgumentParser()
    for arg in ARGUMENT_LIST:
        arg_parser.add_argument(arg)
    args = arg_parser.parse_args()

    mal = MyAnimeListAPI(args.username)
    ka = KissAnimeAPI()

    currently_watching = mal.currently_watching()
    message_list = []

    for anime in currently_watching:
        results = ka.search(anime.title)
        selected = select_result(mal, results, anime)
        anime_info = ka.get_anime_info(selected)
        latest_episode = anime_info.episodes[0]
        latest_episode_number = latest_episode.get_episode_number()
        message_list.append("\"{0}\": Watched {1}, latest {2}\n{3}".format(anime.title,
                                                                           anime.watched_episodes,
                                                                           latest_episode_number,
                                                                           latest_episode.url.decode('ascii')))

    create_popup(message_list)


if __name__ == "__main__":
    main()
