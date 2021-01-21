import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")
# print(soup.title)
# print(soup.title.get_text())
# print(soup.a)
# print(soup.a.attrs)
# print(soup.a["href"])

# print(soup.find("a",attrs={"class":"Nbtn_upload"}))

# rank1 = (soup.find("li",attrs={"class":"rank01"}))
# print(rank1.a.get_text())
# print(rank1.next_sibling.next_sibling.a.get_text())
# rank2=rank1.next_sibling.next_sibling
# rank1 = rank2.previous_sibling.previous_sibling
# print(rank1.parent)
# rank2 = rank1.find_next_sibling("li")
# print(rank2.a.get_text())
# rank1 = rank2.find_previous_sibling("li")
# print(rank1.a.get_text())

# print(rank1.find_next_siblings("li"))

webtoon = soup.find("a",text="힙한남자-4. 힙한출시")
print(webtoon)

