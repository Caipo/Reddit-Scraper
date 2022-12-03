from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
from time import sleep
from sys import exec_prefix
from os import getcwd

# Custom functions
from scrape_func import login, page_rip
from file_func import csv_write, make_file, make_folder

DATA_BASE_PATH = str(getcwd())

#Set true if you want to download images
download = False

# Everything were going to rip
subreddits = sorted({"195", "2meirl4meirl", "bikinibottomtwitter",
                     "kenm", "memeeconomy", "prequelmemes", "wackytictacs",
                     "adviceanimals", "animalswithoutnecks", "anime_irl",
                     "animememes", "antiboomershumor", "badmemes", "bee_irl",
                     "bertstrips", "bigbangedmemes", "birdswitharms",
                     "blackpeopletwitter", "bonehurtingjuice", "boomershumor",
                     "canadian_memes", "catfort", "christianmemes",
                     "classicalmemes", "coaxedintoasnafu", "comedycemetery",
                     "comedyheaven", "comedymassacre", "crappydesign",
                     "cringepics", "cutememe", "dankjewishmemes", "dankmemes",
                     "deepfriedmemes", "disneymemes", "dogfort",
                     "fffffffuuuuuuuuuuuu", "flirtymemes", "freefolk",
                     "fuckyoukaren", "furrymemes", "gamingmemes", "gymmemes",
                     "historyanimemes", "historymemes", "i_irl",
                     "imgoingtohellforthis", "indianpeoplefacebook", "inglip",
                     "leagueofmemes", "mathmemes", "me_irl", "memes99",
                     "metal_me_irl", "nolanbatmanmemes", "nukedmemes",
                     "okbuddyretard", "pepethefrog", "pewdiepiesubmissions",
                     "philosophymemes", "raimimemes", "rarepuppers",
                     "shakespearememes", "shittyadviceanimals", "starterpacks",
                     "surrealmemes", "theofficememes", "toosoon", "torridmemes",
                     "treecomics", "trippinthroughtime", "trumpmemes",
                     "unexpectedjihad", "watchpeopledieinside", "weebcringe",
                     "weirdmemes", "wheredidthesodago", "wholesomememes",
                     "youdontsurf"
                     })

if __name__ == "__main__":

    # selenium set up
    opts = webdriver.ChromeOptions()
    opts.add_argument('''user-agent = Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4)
                                      AppleWebKit/537.36 (KHTML, like Gecko)
                                      Chrome/81.0.4044.92 Safari/537.36''')
    driver = webdriver.Chrome(executable_path= str(os.cwd) + "\\chromedriver.exe", options=opts)

    login(driver)

    make_file(DATA_BASE_PATH + "\\data.csv")

    for sub in subreddits:
        # We will need a folder for each sub

        path = DATA_BASE_PATH + f'\\{sub}'
        if download:
            make_folder(path)

        # Next we now will specify where we want our images
        path = path + "\\"

        sleep(1)
        driver.get(f"https://old.reddit.com/r/{sub}/top/?sort=top&t=all")

        # We will use this loop to iterate pages until it breaks or we hit our limit
        while True:
            soup = BeautifulSoup(driver.page_source, features="html.parser")

            csv_write(page_rip(sub, soup), file_name=f"{DATA_BASE_PATH}\\data.csv")

            try:
                driver.find_element_by_class_name('next-button').click()

            # When we cannot find the next button we switch sub reddits
            except NoSuchElementException:
                break
