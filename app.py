from myanimelist import MyAnimeListAPI
from argparse import ArgumentParser
from kissanime import KissAnimeAPI
from config import ARGUMENT_LIST, ACTIONS
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


def ptw_by_score(mal):
    ptw_list = []
    anime_list = mal.plan_to_watch()
    for anime in anime_list:
        global_anime_ref = mal.search(anime.title)[0]
        ptw_list.append(global_anime_ref)

    ptw_list.sort(key=lambda x: x.score, reverse=True)
    avg_score = 0.0
    rated_count = 0

    for anime in ptw_list:
        if anime.score != 0:
            avg_score += anime.score
            rated_count += 1
        print(anime.title, anime.score)
    avg_score /= rated_count

    print("Average anime rating: {0:.2f}".format(avg_score))


def new_episode_list(mal, ka):
    anime_list = mal.currently_watching()
    for anime in anime_list:
        results = ka.search(anime.title)
        selected = select_result(mal, results, anime)
        anime_info = ka.get_anime_info(selected)
        latest_episode = anime_info.episodes[anime.watched_episodes]
        latest_episode_number = latest_episode.get_episode_number()
        print("\"{0}\": Watched {1}, latest {2}\n{3}".format(
            anime.title,
            anime.watched_episodes,
            latest_episode_number,
            latest_episode.url.decode('ascii')
        ))


def main():
    arg_parser = ArgumentParser()
    for arg in ARGUMENT_LIST:
        arg_parser.add_argument(arg)
    args = arg_parser.parse_args()

    mal = MyAnimeListAPI(args.username)
    ka = KissAnimeAPI()

    action = args.action
    if action == ACTIONS["UNWATCHED_EPOISODES"]:
        new_episode_list(mal, ka)
    elif action == ACTIONS["RATE_PTW_ANIME"]:
        ptw_by_score(mal)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print()
