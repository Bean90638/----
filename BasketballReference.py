import requests
from bs4 import BeautifulSoup

# r = requests.get("https://www.ptt.cc/bbs/MobileComm/index.html") #將網頁資料GET下來
# soup = BeautifulSoup(r.text,"html.parser") #將網頁資料以html.parser
# sel = soup.select("div.title a") #取HTML標中的 <div class="title"></div> 中的<a>標籤存入sel
# for s in sel:
#     print(s["href"], s.text) 

SStr = "-pt "
EStr = " from"

# 判斷td標籤內有沒有指定字串，有的話顯示指定的td標籤
def RowsGetTd(rows_td,i):
    if len(rows_td)<i: return

    SFind = rows_td[i].text.find(SStr)
    EFind = rows_td[i].text.find(EStr)
    if SFind>=0 and EFind>=0:
        print(rows_td[0].text+'\t'+rows_td[i].text[SFind+len(SStr):EFind])

# 帶入該場比賽URL，顯示全部投球時間&投球方式
def basketball_GetTdData(url):
    r = requests.get(url) #將網頁資料GET下來
    soup = BeautifulSoup(r.text,"html.parser") #將網頁資料以html.parser
    sel = soup.select("div.table_container tr") #取HTML標中的 <div class="title"></div> 中的<a>標籤存入sel
    rows = soup.find('table', class_='suppress_all sortable stats_table').find_all('tr')

    for s in rows:
        rows_td = s.find_all('td')
        if len(rows_td)>=5:
            RowsGetTd(rows_td,1)
            RowsGetTd(rows_td,5)

basketball_GetTdData("https://www.basketball-reference.com/boxscores/pbp/201810160BOS.html")

