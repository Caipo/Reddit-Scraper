from urllib.request import Request, urlopen, urlretrieve

'''
- logs into reddit
- You may have to provide you own info into the keys section
'''
def login(driver):
    driver.get('https://old.reddit.com/login/')
    driver.find_element_by_id("user_login").send_keys("likeasirXx")
    driver.find_element_by_id("passwd_login").send_keys("starcraft")
    driver.find_element_by_xpath('//*[@id="login-form"]/div[5]/button').click()


'''downloads our file to hard drive and gives it the name of the local index'''
def download(link, path, id):
    print("blap" + link)
    if link[-5] == '.':
        urlretrieve(link, path + str(id) + link[-5:])

    elif link[-4] == '.':
        urlretrieve(link, path + str(id) + link[-4:])


''' for each reddit page this will give us the data we need '''
def page_rip(sub, soup, save_img = False, path = ""):
    soup.encode("utf-8")

    # This will give us all the reddit links we want  for some reason they designated it with thing
    tags = soup.find_all(lambda tag: tag.name == "div"
                                     and tag.get("class") is not None
                                     and "thing" in tag.get("class") and "locked" not in tag.get("class")
                         )
    page_data = list()

    for element in tags:

        # This is where we get all the data
        # For some reason its hit or miss if reddit includes author / score so we use the get method on these
        page_data.append({"id": element["class"][1].replace("id-", ""), "sub": sub,
                          "title": element.find_all("a")[0].contents[0],
                          "rank": element["data-rank"], "image_link": element["data-url"],
                          "permalink": f"https://www.old.reddit.com//" + element["data-permalink"],
                          "score": element.get("data-score"), "author": element.get("data-author"),
                          "time": element["data-timestamp"], "nsfw": element["data-nsfw"]
                          })

        if save_img:
            download(path, page_data[-1]["image_link"], page_data[-1]["id"])


    return page_data
