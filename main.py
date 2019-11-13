from page.TuoiTre import TuoiTre

if __name__ == "__main__":
    f = open("./data/tuoitre/tuoitre.json", "a")
    f.write("[")
    number = 10 # 10*15 page
    tuoitre = TuoiTre(number, f)
    tuoitre.scrapting()
    f.write("{}]")
    f.close()