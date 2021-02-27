import csv
import sys
import os
import time
import requests
from selenium import webdriver

class instascrape():
    def __init__(self):
        self.driver = None
        self.posts = []
        self.savedir = "C:\\Users\\inmyh\\mattyavlog\\static\\image\\instagram\\mattya_lab"
        self.exists = []
        self.cnt = 0

    def scrape(self):
        self.driver = webdriver.Chrome()
        self.login()
        self.collectlinks()
        self.makefile()
        self.downloadpics()
        self.driver.quit()
        self.driver = None

    def login(self):
        self.driver.get('https://www.instagram.com/accounts/login/')
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_name('username').send_keys('mattya_lab')
        self.driver.find_element_by_name('password').send_keys('is0378er')
        self.driver.find_element_by_class_name('L3NKy       ').click()
        self.driver.implicitly_wait(10)
        time.sleep(5)

    def collectlinks(self):
        self.driver.get('https://www.instagram.com/mattya_lab/')
        self.driver.implicitly_wait(10)
        lenOfPage = self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;"
        )
        match = False
        while (match == False):
            lastCount = lenOfPage
            time.sleep(3)
            lenOfPage = self.driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;"
            )
            if lastCount == lenOfPage:
                match = True

        links = self.driver.find_elements_by_tag_name('a')
        for link in links:
            post = link.get_attribute('href')
            if '/p/' in post:
                self.posts.append(post)

    def makefile(self):
        if not os.path.isdir(self.savedir):
            os.mkdir(self.savedir)

    def readexistfile(self):
        self.exists = []
        self.cnt = 0
        with open('exists.csv', 'r', newline='') as f:
            reader = f.readline().replace('\r\n', '')
            while reader:
                self.cnt = self.cnt + 1
                self.exists.append(reader)
                reader = f.readline().replace('\r\n', '')

    def writeexistfile(self):
        with open('exists.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            for row in range(len(self.exists)):
                writer.writerow([self.exists[row]])

    def downloadpics(self):
        self.readexistfile()
        img_src = []
        for post in self.posts:
            self.driver.get(post)
            self.driver.implicitly_wait(10)

            # Get shortcode
            shortcode = self.driver.current_url.split('/')[-2]
            f = True
            for i in range(len(self.exists)):
                if shortcode == self.exists[i]:
                    f = False
            if f:
                print(shortcode)
                self.exists.append(shortcode)
                for data in self.driver.find_elements_by_class_name('FFVAD'):
                    img_src.append(data.get_attribute('src'))

        for src in img_src:
            filepath = self.savedir + '\\' + str(self.cnt) + '.jpg'
            img = requests.get(src)
            with open(filepath, 'wb') as f:
                f.write(img.content)
            self.cnt = self.cnt + 1
        self.writeexistfile()