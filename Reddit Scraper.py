from urllib.request import Request, urlopen, urlretrieve
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
import os
import shutil

#option = webdriver.ChromeOptions()
#chrome_prefs = {}
#option.experimental_options["prefs"] = chrome_prefs
#chrome_prefs["profile.default_content_settings"] = {"images": 2}
#chrome_prefs["profile.managed_default_content_settings"] = {"images": 2}


filename = "D:\\Memes\\" + "Database" + ".csv"


opts = webdriver.ChromeOptions()
opts.add_argument("user-agent = Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36 ")

driver = webdriver.Chrome(executable_path = "C:\\Users\\Caipo\\Desktop\\chromedriver.exe" , options = opts)

i = 0
j = 0


def login():
    driver.get('https://www.reddit.com/login/')
    driver.find_element_by_id("loginUsername").send_keys("LikeasirXx")
    driver.find_element_by_id ("loginPassword").send_keys("starcraft")
    driver.find_element_by_class_name("AnimatedForm__submitButton").click()



def crawler():
    global driver
    global i
    global j


    
    makeFile()
    csvWrite(  ["Global Index", "local Index", "Subreddit", "Rank", "Imagelink", "Permalink", "Score", "Author", "Time Stamp", "Nsfw"] )

    
    for sub in subreddits:
        
       
        path = 'D:\\Memes\\' + sub
        if not os.path.exists(path):
            os.makedirs(path)
            
        else:
            shutil.rmtree(path)
            os.makedirs(path)

  
    
        path = path + "\\"
        site = "https://old.reddit.com/r/" + str(sub) + "/top/?sort=top&t=all"
        driver.get(site)
        
        while True:
            try:
                
                soup = BeautifulSoup(driver.page_source, features="html.parser")
                    
                pageData = pageRip(sub , soup)


                for array in pageData:
                    csvWrite( array )

                '''
                site = ""
                #Finding the next button
                for thing in str(soup.find("span", {"class" : "next-button"} )).split(" "):
                    if "href=" in thing:
                        site = thing.replace("href=","").replace("\"" , "")
                '''

                #Decides when to move on 
                if site == "" or j >= 2000:
                    break

                driver.find_element_by_class_name('next-button').click()
            
            except Exception as err:
                 print(err)
                 print("Reddit mad")
                 break
                 
                 


        j = 0




def pageRip( sub, soup ):
    global i
    global j
    
    soup.encode("utf-8")
    
    tags = soup.findAll("div")    
    pageData = list()
    rankHistory = list()
    
    if "<button class=\"c-btn c-btn-primary\" type=\"submit\" name=\"over18\" value=\"yes\">continue</button>" in soup:
        print("fdafs")
    
    
    for content in tags:

        
        if not ("data-url=" in str(content)  and "data-permalink=" in str(content)  and "data-nsfw=" in str(content)  and "data-author=" in str(content) and "data-score" in str(content) and "data-timestamp=" in str(content) and "data-rank=" in str(content) ) or "data-promoted=\"true\"" in str(content):
            continue

        
        
        array = str(content).split(" ")
        imagelink,permalink,nsfw,author,score,time,rank = "","","","","","",""
        duplicate = False
        
    
        for element in array:


            if "data-url=" in element:
                imagelink = element.replace("data-url=", "").replace("\"", "")

            elif "data-permalink=" in element:
                permalink = element.replace("data-permalink=", "").replace("\"", "")
                    
            elif "data-nsfw=" in element:
                nsfw = element.replace("data-nsfw=", "").replace("\"", "")
                       
            elif "data-author=" in element:
                author  = element.replace("data-author=", "").replace("\"", "")
                       
            elif "data-score" in element:
                score = element.replace("data-score=", "").replace("\"", "")

            elif "data-timestamp=" in element:
                time = element.replace("data-timestamp=", "").replace("\"", "")

            elif "data-rank=" in element:
                rank = element.replace("data-rank=", "").replace("\"", "")

                if rank in rankHistory:
                    duplicate = True
                    continue


        i += 1
        j += 1
        
        if not duplicate:
            pageData.append([i, j, sub, rank, imagelink, "https://www.old.reddit.com" + permalink, score, author, time, nsfw])
            rankHistory.append(rank)
            download(imagelink, "D:\\Memes\\" + sub  + "\\")


    return pageData    
            

        
def csvWrite(fields):
    with open(filename, 'a', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(fields)
        f.close()
  



def makeFile():
    global filename
    if os.path.exists(filename):
        append_write = 'w' # append if already exists
    else:
        append_write = 'w' # make a new file if not

    file = open(filename,append_write)
    file.write("")
    file.close()

    print(filename)


def download( link, path):

        

        if link[-5] == '.':
            urlretrieve(link, path + str(i) + link[-5:] )
            
        elif link[-4] == '.':
            urlretrieve(link, path + str(i)+ link[-4:] )

                




subreddits = sorted({
"195",
"2meirl4meirl",
"bikinibottomtwitter",
"kenm",
"memeeconomy",
"prequelmemes",
"wackytictacs",
"adviceanimals",
"animalswithoutnecks",
"anime_irl",
"animememes",
"antiboomershumor",
"badmemes",
"bee_irl",
"bertstrips",
"bigbangedmemes",
"birdswitharms",
"blackpeopletwitter",
"bonehurtingjuice",
"boomershumor",
"canadian_memes",
"catfort",
"christianmemes",
"classicalmemes",
"coaxedintoasnafu",
"comedycemetery",
"comedyheaven",
"comedymassacre",
"crappydesign",
"cringepics",
"cutememe",
"dankjewishmemes",
"dankmemes",
"deepfriedmemes",
"disneymemes",
"dogfort",
"fffffffuuuuuuuuuuuu",
"flirtymemes",
"freefolk",
"fuckyoukaren",
"furrymemes",
"gamingmemes",
"gymmemes",
"historyanimemes",
"historymemes",
"i_irl",
"imgoingtohellforthis",
"indianpeoplefacebook",
"inglip",
"leagueofmemes",
"mathmemes",
"me_irl",
"memes99",
"metal_me_irl",
"nolanbatmanmemes",
"nukedmemes",
"okbuddyretard",
"pepethefrog",
"pewdiepiesubmissions",
"philosophymemes",
"raimimemes",
"rarepuppers",
"shakespearememes",
"shittyadviceanimals",
"starterpacks",
"surrealmemes",
"theofficememes",
"toosoon",
"torridmemes",
"treecomics",
"trippinthroughtime",
"trumpmemes",
"unexpectedjihad",
"watchpeopledieinside",
"weebcringe",
"weirdmemes",
"wheredidthesodago",
"wholesomememes",
"youdontsurf",
})


login()
crawler( )
