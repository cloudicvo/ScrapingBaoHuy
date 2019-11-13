from  api.TuoiTreAPI import TuoiTreAPI
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import json
from fake_useragent import UserAgent
class TuoiTre:

    def __init__(self, times, f):
        self.times = times
        self.titleclass = "title-news"
        self.contentid = "main-detail-body"
        self.api = TuoiTreAPI()
        self.file = f
        self.useragent = UserAgent()

    def fake(self, url):
        return Request(url, headers={
            'User-Agent': self.useragent.random
        })

    def create(self, title, content, category, page):
        return{
            "title": title,
            "content": content,
            "category": category,
            "page": page
        }

    def store(self, ldata):
        for data in ldata:
            json.dump(data, self.file, ensure_ascii=False, indent=4)
            self.file.write(",")

    def scrapting(self):
        for page in self.api.page:
            lcategory = self.api.getalllink(page)
            for spage in lcategory:
                category = spage["category"]
                link = spage["link"]
                for i in range(1, self.times):
                    try:
                        print(link.format(i))
                        content = urlopen(self.fake(link.format(i)))
                        soup = BeautifulSoup(content, "lxml")
                        record = soup.findAll('h3', {
                            "class": self.titleclass
                        })
                        ldata = []
                        for r in record:
                            gettag = r.find("a")
                            title = gettag.get("title")
                            plink = self.api.pageurl.format(gettag.get("href"))
                            print(plink)
                            paragraph = urlopen(self.fake(plink))
                            psoup = BeautifulSoup(paragraph, "lxml")
                            paragraph =  psoup.find("div", {
                                "id": self.contentid
                            })

                            try:
                                cparagraph = paragraph.find("p").text
                            except Exception:
                                cparagraph = ""

                            try:
                                cparagraph += paragraph.find("span").text
                            except Exception:
                                pass

                            if cparagraph != "":
                                ldata.append(self.create(title, cparagraph, category, page))

                        self.store(ldata)
                    except Exception as e:
                        break