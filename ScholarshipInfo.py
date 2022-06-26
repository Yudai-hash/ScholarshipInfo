from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import time
import pandas as pd
import urllib.request as req

USER = "test_user"
PASS = "test_pw"

#GoogleChrome
browser = webdriver.Chrome(executable_path = '/cygdrive/g/マイドライブ/水内研究室関連/MyPandas/chromedriver.exe')
browser.implicitly_wait(3)

##アクセスするサイトのURL
url_login = "https://www.e-grant.jp/"
browser.get(url_login)
time.sleep(3)
print("ログインページにアクセスした")
print("")
#公的機関向け情報をクリック
frm = browser.find_element(By.XPATH,'//*[@id="container"]/div[1]/div/div[1]/div[1]/div[2]/div/div[2]/ul/li[2]/a')
time.sleep(1)
frm.click()
print('公的機関向け情報の取得')
print("")
#現在のURLを取得する
cur_url = browser.current_url
#1秒間待機
time.sleep(1)

response = req.urlopen(cur_url)
parse_html = BeautifulSoup(response,'html.parser')

#parse_htmlの中身の確認
#print(parse_html)
#print("")
#print("parse_html.li")
#print(parse_html.li)
#print("")
#print("parse_html.ul")
#print(parse_html.ul.li)
#print("")
#print("parse_html.div")
#print(parse_html.div)
#pr
#print(browser.find_element(By.CSS_SELECTOR,".page_list .article .txt"))
for i in range(1,11):
    print(browser.find_element(By.XPATH,'//*[@id="replaceContent"]/ul/li['+str(i)+']/div').text)
    print("")




#そのページごとの件数を取得する
Cases = browser.find_element(By.XPATH,'//*[@id="pager_box"]/p/span[2]').text
time.sleep(1)
print("Cases in this page")
print(Cases)
Cases = Cases.replace('-',' ')
print("Delete the hyphen")
print(Cases)

target = ' '
Distance = Cases.find(target)
print("Get the value before the empty")
print(Cases[:Distance])
print("Get the value after the empty")
print(Cases[Distance+1:])
#全体の件数を取得する
AllCases = browser.find_element(By.XPATH,'//*[@id="pager_box"]/p/span[1]').text
print(AllCases)


frm = browser.find_element(By.XPATH,'//*[@id="pager_box"]/ul/li[3]/a')
time.sleep(1)
frm.click()
print("Move next page")
time.sleep(5)
#ここは、いらない
#lists = browser.find_element(By.CLASS_NAME,"page_list")
#data = pd.read_html(cur_url)
#lists = []

##ここは、いらない
#lists.append(browser.find_element(By.XPATH,'//*[@id="replaceContent"]/ul/li[1]/div'))
#lists.append(browser.find_element(By.XPATH,'//*[@id="replaceContent"]/ul/li[2]/div'))

#print(lists)
#print("ページリスト取得")

##ここは、いらない
#parse_html = BeautifulSoup(cur_url,'html.parser')
#print(parse_html)
#print(parse_html.prettify())

##ここは、いらない
#print("parse_html.find_all(li)")
#print(parse_html.find_all('li'))
#print(parse_html.find_all(li))

##下は、div > liのスクレイピングができた例
#print(browser.find_element(By.XPATH,'//*[@id="replaceContent"]/ul/li[1]/div/h2').text)
#print("")
#print(browser.find_element(By.XPATH,'//*[@id="replaceContent"]/ul/li[1]/div/p').text)
#print("")
#print(browser.find_element(By.XPATH,'//*[@id="replaceContent"]/ul/li[2]/div').text)
#print("")
#print(browser.find_element(By.XPATH,'//*[@id="replaceContent"]/ul/li[2]/div/h2').text)
#print("")
#print(browser.find_element(By.XPATH,'//*[@id="replaceContent"]/ul/li[2]/div/p').text)
#print("")













