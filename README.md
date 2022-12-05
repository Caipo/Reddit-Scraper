# Reddit Scraper
Simple python app based on selinum to download/catalog all your favorite subreddits.


## Scope 
This is used as an introduction to webscraping and data collection.


## Set Up
1. Ensure python is at leat version 3.10 ```python3 --version```
2. Install selinum, and beautifulsoup ```python3 -m pip install selinum beautifulsoup4 ```
3. Make sure chrome is installed and get the version ```three dots > help > about chrome ```
4. Download the chrome drivers that match your chrome version ```https://chromedriver.chromium.org/downloads```
5. Move the chromedrive in the project folder
6. Make an .env file in the project folder with your reddit username and password. (Im not reposibul if reddit decides to ban you) ```touch .env```
7. Eddit the .env file and add ```REDDIT_NAME= '<here>'``` and ```REDDIT_PASSWORD='here'```
9. run main.py ```python3 main.py```

## To do 
* test the download feature.
* implement SQL connecter for a proper data base (csv has its limitations).
* test on windows 


## data.csv format
id | subreddit | title | rank | image_link | permalink | score (int) | author | timestamp | nsfw(boolean)
















