import requests
import re
import time


class Coordinate(object):
    def __init__(self):
        self.baseurl = "https://tj.lianjia.com/zufang/"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"
        }

    # 对链家的租房页面进行请求，并返回页面内容
    def first_get_page(self, params):
        res = requests.get(url=self.baseurl, params=params, headers=self.headers)
        res.encoding = 'utf-8'
        first_restext = res.text
        return first_restext


    def second_get_page(self, first_url):
        url = "https://tj.lianjia.com" + first_url
        print(url, '这是第二页')
        res = requests.get(url=url, headers=self.headers)
        res.encoding = 'utf-8'
        second_restext = res.text
        return second_restext

    def first_prase_page(self, first_restext):
        first_regurla = """class="content__list--item--main">.*?class="content__list--item--title twoline">.*?href="(.*?)">"""
        p = re.compile(first_regurla, re.S)
        first_html = p.findall(first_restext)
        return first_html

    def second_prase_page(self, second_restext):
        second_regula = """longitude: '(.*?)'.*?latitude: '(.*?)'"""
        p = re.compile(second_regula, re.S)
        second_html = p.findall(second_restext)
        return second_html

    def write_page(self, second_html):
        with open('coordinate.txt', 'a') as f:
            longitude = second_html[0][0]
            latitude = second_html[0][1]
            coor = longitude + ':' + latitude + '\n'
            f.write(coor)

    def main(self):
        pg = 0
        while True:
            pg += 1
            params = {
                "pg": pg
            }
            first_restext = self.first_get_page(params)
            first_html = self.first_prase_page(first_restext)
            print(first_html, '这是第一页')
            for first_url in first_html:
                second_restext = self.second_get_page(first_url)
                time.sleep(1)
                second_html = self.second_prase_page(second_restext)
                self.write_page(second_html)
                time.sleep(1)


if __name__ == '__main__':
    coordinate = Coordinate()
    coordinate.main()