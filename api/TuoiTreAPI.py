class TuoiTreAPI:
    def __init__(self):
        self.url = "https://tuoitre.vn/timeline/{0}/trang-{1}.htm"
        self.pageurl = "https://tuoitre.vn{0}"
        self.page = {
            "thoi-su":{
                "xa-hoi": 200003,
                "phong-su": 89,
                "binh-luan": 87
            },
            "the-gioi":{
                "binh-luan": 94,
                "kieu-bao": 312,
                "muon-mau": 442,
                "ho-so": 20
            },
            "phap-luat":{
                "chuyen-phap-dinh": 266,
                "tu-van": 79,
                "phap-ly": 200005
            },
            "kinh-doanh":{
                "tai-chinh": 86,
                "doanh-nghiep": 775,
                "mua-sam": 200006,
                "dau-tu": 200007
            },
            "cong-nghe": {
                "nhip-song-so": 16,
            }
        }

    def createlink(self, code):
        return self.url.format(code,"{0}")

    def createinfo(self, category, code):
        return {
            "category": category,
            "link": self.createlink(code)
        }

    def getalllink(self, page):
        return [self.createinfo(key, value) for key, value in self.page[page].items()]
    