import requests
from bs4 import BeautifulSoup
import time

TOKEN = "8765922287:AAHPV6G2nYEWFNvaJpPb5AvATbDevexQLfY"
CHAT_ID = "8629265835"

URL = "https://boardlife.co.kr/board/used/board_used/1"

keywords = [
"스피크이지",
"스피크 이지",
"speakeasy",
"바이마르",
"weimar"
]

seen = set()

send("봇 연결 테스트 성공")

def send(msg):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, data={
        "chat_id": CHAT_ID,
        "text": msg
    })

while True:

    res = requests.get(URL)
    soup = BeautifulSoup(res.text, "html.parser")

    posts = soup.select("a")

    for p in posts:

        title = p.text.strip()
        link = p.get("href")

        if not link:
            continue

        if "bbs_detail" not in link:
            continue

        if link.startswith("/"):
            link = "https://boardlife.co.kr" + link

        if link in seen:
            continue

        if "[판매]" not in title:
            continue

        for k in keywords:

            if k.lower() in title.lower():

                msg = f"[보드라이프 중고장터]\n\n{title}\n\n{link}"
                send(msg)

                seen.add(link)

                break

    time.sleep(300)
