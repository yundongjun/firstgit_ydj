import requests
from bs4 import BeautifulSoup

url = "https://search.daum.net/search?nil_suggest=btn&w=tot&DA=SBC&q=%ED%97%AC%EB%A6%AC%EC%98%A4%EC%8B%9C%ED%8B%B0"
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text,"lxml")

# with open("quiz.html","w",encoding="utf8")as f:
#     f.write(soup.prettify())

data_rows = soup.find("table",attrs={"class":"tbl"}).find("tbody").find_all("tr")
for index,row in enumerate(data_rows):
    columns = row.find_all("td")

    print("========= 매물 {} =========".format(index+1))
    print("거래 :", columns[0].get_text())
    print("면적 :", columns[1].get_text(),"(공급/전용)")
    print("가격 :", columns[2].get_text(),"(만원)")
    print("동 :", columns[3].get_text())
    print("층 :", columns[4].get_text())

