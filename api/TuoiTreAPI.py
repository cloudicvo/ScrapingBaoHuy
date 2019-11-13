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
            "cong-nghe":{
                "nhip-song-so": 16,
                "trai-nghiem": 557,
                "thi-truong": 547,
                "thu-thuat": 67,
                "gia-dinh-so": 200028,
                "nhip-cau": 297
            },
            "xe":{
                "xe": 659
            },
            "du-lich":{
                "co-hoi-du-lich": 100001,
                "di-choi": 100009,
                "an-gi": 100010,
                "mach-ban": 384,
                "que-huong": 100011
            },
            "nhip-song-tre": {
                "xu-huong": 200012,
                "theo-guong-bac": 1580,
                "kham-pha": 200013,
                "yeu": 194,
                "nhan-vat": 200014
            },
            "van-hoa":{
                "nhan-vat": 200050,
                "san-dien": 200051,
                "sach": 200051,
                "doi-song": 200018
            },
            "giai-tri":{
                "nghe-gi-hom-nay": 1581,
                "am-nhac": 58,
                "dien-anh": 57,
                "tv-show": 385,
                "thoi-trang": 919,
                "hau-truong": 922
            },
            "the-thao": {
                "tin-tuc": 200030,
                "cong-dong": 200031,
                "binh-luan": 200032,
                "the-thao-vui": 200034
            },
            "giao-duc":{
                "tuyen-sinh": 142,
                "hoc-duong": 1507,
                "bai-giai-dap-an": 200054,
                "du-hoc": 85,
                "cau-chuyen-giao-duc": 913
            },
            "khoa-hoc": {
                "thuong-thuc": 200010,
                "phat-minh": 200011
            },
            "suc-khoe":{
                "dinh-duong": 200008,
                "me-va-be": 197,
                "gioi-tinh": 241,
                "phong-mach": 231,
                "biet-de-khoe": 1465
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
    