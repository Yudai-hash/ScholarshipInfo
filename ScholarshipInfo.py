from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By

import pandas as pd
import urllib.request as req
import time
import datetime
import create_pdf
import textwrap

#GoogleChrome
browser = webdriver.Chrome(executable_path = '/cygdrive/g/マイドライブ/水内研究室関連/MyPandas/chromedriver.exe')
browser.implicitly_wait(3)

##アクセスするサイトのURL
url_login = "https://www.e-grant.jp/"
browser.get(url_login)
time.sleep(3)

print("ログインページにアクセスした")
print("")
#*公的機関向け情報*をクリック
frm = browser.find_element(By.XPATH,'//*[@id="container"]/div[1]/div/div[1]/div[1]/div[2]/div/div[2]/ul/li[2]/a')
time.sleep(1)
frm.click()
print('公的機関向け情報の取得')
print("")

#現在のURLを取得する
cur_url = browser.current_url
#1秒間待機
time.sleep(1)

#response = req.urlopen(cur_url)
#parse_html = BeautifulSoup(response,'html.parser')

#parse_htmlの中身の確認
#print(parse_html)
#print("")
#print("parse_html.li")
#print(parse_html.li)
#print("")n
#pnrint("parse_html.ul")
#print(parse_html.ul.li)
#print("")
#print("parse_html.div")
#print(parse_html.div)
#print(browser.find_element(By.CSS_SELECTOR,".page_list .article .txt"))

#####そのページごとの件数を取得する#####
Cases = browser.find_element(By.XPATH,'//*[@id="pager_box"]/p/span[2]').text
#time.sleep(1)
#print("Cases in this page")
#print(Cases)
Cases = Cases.replace('-',' ')
#print("Delete the hyphen")
#print(Cases)

target = ' '
Distance = Cases.find(target)
#print("Get the value before the empty")
#print(Cases[:Distance])
#print("Get the value after the empty")
#print(Cases[Distance+1:])
cases = Cases[Distance+1:]
########全体の件数を取得する##########
AllCases = browser.find_element(By.XPATH,'//*[@id="pager_box"]/p/span[1]').text
#print(AllCases)
#######商と余りを確認########
#print(int(AllCases)//int(cases))
#print(int(AllCases)%int(cases))


#全体の件数を各ページの件数で割ると、商とあまりが求める
#for文を2重で使う
#一番外のfor文は、商だけ
#一番内側のfor文は、そのページの件数の文だけ回す
#その後に,新たに一重のforをあまりだけ回す
#i.e)全体165件 1ページの件数が10件の場合
#165=10×16+5
#for in range(1,16+1):
#  for in range(1,10+1):
#    hogehoge
#for in range(1,5+1):
#  hogehoge

#3 should be replaced with int(int(AllCases)//int(cases))+1

#print(int(AllCases)) #310
#print(int(cases)) #10
#print(int(int(AllCases)//int(cases))) #31
userInput = input("入力してください:\n 電気・電子\n化学\n金属・機械\n食品・バイオ\n医療・介護\n環境・新エネルギー\n材料\nその他\n")
print("あなたは"+userInput+"を入力しました")

a_list = []
countNumber = 0
for j in range(1,int(int(AllCases)//int(cases))+1):
    for i in range(1,int(cases)+1):
        #a = browser.find_element(By.XPATH,'//*[@id="replaceContent"]/ul/li['+str(i)+']/div').text
        a = browser.find_element(By.XPATH,'/html/body/div[1]/div[3]/div/div[1]/div/ul/li['+str(i)+']/div/h2/a').text
        b = browser.find_element(By.XPATH,'/html/body/div[1]/div[3]/div/div[1]/div/ul/li['+str(i)+']/div/dl[2]/dd').text
        c = browser.find_element(By.XPATH,'/html/body/div[1]/div[3]/div/div[1]/div/ul/li['+str(i)+']/div/dl[3]/dd').text
        if browser.find_element(By.XPATH,'/html/body/div[1]/div[3]/div/div[1]/div/ul/li['+str(i)+']/div/ul/li[2]').text == str(userInput):
            #医療・介護
            a_list.append(a)
            a_list.append(b)
            a_list.append(c)
            print(a)
            print(b)
            print(c)
            countNumber = countNumber + 1
            print(countNumber)
        else:
            pass
    print("")

    if j <= int(int(AllCases)//int(cases))+1-1-1: #range(1,2)とすると1以上1未満であるので、さらに-1
        frm = browser.find_element(By.XPATH,'/html/body/div[1]/div[3]/div/div[1]/div/div[3]/ul/li[3]/a')
        #/html/body/div[1]/div[3]/div/div[1]/div/div[3]/ul/li[3]/a
        #//*[@id="pager_box"]/ul/li[3]/a

        time.sleep(1)
        frm.click()

        print("Move next page"+str(j))
        time.sleep(5)

    else:
        print("No move further")
#for k in range(1,(int(AllCases)%int(cases))+1):
#    a = browser.find_element(By.XPATH,'/html/body/div[1]/div[3]/div/div[1]/div/ul/l#i['+str(i)+']/div/h2/a').text
#    b = browser.find_element(By.XPATH,'/html/body/div[1]/div[3]/div/div[1]/div/ul/l#i['+str(i)+']/div/dl[2]/dd').text
#    c = browser.find_element(By.XPATH,'/html/body/div[1]/div[3]/div/div[1]/div/ul/l#i['+str(i)+']/div/dl[3]/dd').text
#    if browser.find_element(By.XPATH,'/html/body/div[1]/div[3]/div/div[1]/div/ul/li#['+str(i)+']/div/ul/li[2]').text == "医療・介護":
#        a_list.append(a)
#        a_list.append(b)
#        a_list.append(c)
#        print(a)
#        print(b)
#        print(c)
        
#最初からmain関数で書くとろくなこと(無茶苦茶時間かかる、一個一個確実にやったほうが良い)

#a_wrap_list = textwrap.wrap(a_list,40)
#a_wrap_after = '\n'.join(a_wrap_list)
print(countNumber)
create_pdf.create_pdf(a_list,countNumber,userInput)







 
