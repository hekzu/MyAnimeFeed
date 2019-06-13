from myanimelist import MyAnimeListAPI
from argparse import ArgumentParser
from kissanime import KissAnimeAPI
from config import ARGUMENT_LIST


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


def main():
    arg_parser = ArgumentParser()
    for arg in ARGUMENT_LIST:
        arg_parser.add_argument(arg)
    args = arg_parser.parse_args()

    mal = MyAnimeListAPI(args.username)
    ka = KissAnimeAPI()

    currently_watching = mal.currently_watching()
    for anime in currently_watching:
        results = ka.search(anime.title)
        selected = select_result(mal, results, anime)
        anime_info = ka.get_anime_info(selected)
        latest_episode_number = anime_info.episodes[0].get_episode_number()
        print("\"{0}\": Watched {1}, latest {2}".format(anime.title, anime.watched_episodes, latest_episode_number))


if __name__ == "__main__":
    main()
