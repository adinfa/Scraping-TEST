import requests
import pymongo
from pymongo import MongoClient
from bs4 import BeautifulSoup as bs

cluster = MongoClient("mongodb+srv://user:12345@cluster0.o3amh.mongodb.net/<dbname>?retryWrites=true&w=majority")
db = cluster["ScrapingResult"]
collection = db["TestCollection"]



class BBC:
    def __init__(self, url:str):
        article = requests.get(url)
        self.soup = bs(article.content, "html.parser")
        self.body = self.get_body()
        self.title = self.get_title()
        self.author = self.get_author()
        
    def get_body(self) -> str:
        body = self.soup.find(class_="qa-story-body story-body gel-pica gel-10/12@m gel-7/8@l gs-u-ml0@l gs-u-pb++")
        a=[p.text for p in body.find_all("p")]
        bodystr = ''.join(a)
        return bodystr
    
    def get_title(self) -> str:
        return self.soup.find(class_="gel-trafalgar-bold qa-story-headline gs-u-mv+").text
    
    def get_author(self) -> str:
        return self.soup.find(class_='qa-contributor-name gel-long-primer').text
    
    
LINK = BBC("https://www.bbc.com/sport/football/55436136")

BODY = LINK.body
TITLE = LINK.title
AUTHOR = LINK.author

post = {"_Author": AUTHOR, "_Title": TITLE , "_Body": BODY }



collection.insert_one(post)

BODY

