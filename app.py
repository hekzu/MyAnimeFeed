from myanimelist import MyAnimeListAPI
from kissanime import KissAnimeAPI


def main():
    mal = MyAnimeListAPI("hekzu")
    ka = KissAnimeAPI()
    titles = MyAnimeListAPI.extract_titles(mal.currently_watching())

    for title in titles:
        results = ka.search(title)
        if results:
            for result in results:
                print(result)


if __name__ == "__main__":
    main()
