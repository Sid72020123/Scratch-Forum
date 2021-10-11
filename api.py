import requests
from bs4 import BeautifulSoup


def get_posts(topic_id, page=1):
    try:
        POSTS = []
        URL = f"https://scratch.mit.edu/discuss/topic/{topic_id}/?page={page}"
        resopnse = requests.get(URL)

        soup = BeautifulSoup(resopnse.content, 'html.parser')
        page = soup.find_all("div", {"class": "blockpost roweven firstpost"})
        for data in page:
            POST_ID = data.find("a")['name']  # POST ID
            POST_TIME = data.find_all("a")[1].contents[0]  # POST TIME
            USER = data.find("a", {"class": "black username"}).text  # USER
            USER_AVATAR = "https:" + data.find("dd", {
                "class": "postavatar"
            }).find("img")['src']  # USER AVATAR
            CONTENT = data.find("div", {
                "class": "post_body_html"
            }).text  # CONTENT
            json = {
                'Post ID': POST_ID,
                'Post Time': POST_TIME,
                'User': USER,
                'UserAvatar': USER_AVATAR,
                'Content': CONTENT
            }
            POSTS.append(json)
        if POSTS == []:
            return {'Error': 'Topic/Page Not Found'}
        return POSTS
    except:
        return {'Error': 'An Error Occured!'}
