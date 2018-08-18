import requests
from bs4 import BeautifulSoup

r = requests.get('http://b.hatena.ne.jp/')
content = r.content
soup = BeautifulSoup(content, 'html.parser')

for div in soup.select("div.entrylist-contents-main"):
    title = div.h3
    url = div.a
    user = div.span
    user_num = user.getText().split(" ")
    description = div.p
    date = div.li

    if int(user_num[0]) >= 20:
        print(title.getText(),end="")
        print(url.get('href'),end="")
        print(user.getText(),end="")
        print(description.getText(),end="")
        print(date.getText(),end="")
    else:
        next
