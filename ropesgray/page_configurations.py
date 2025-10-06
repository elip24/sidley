import urllib
from urllib.parse import urlparse
from urllib.parse import urljoin
base_url = "https://www.ropesgray.com/en/news-and-events"
header={
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9,es-AR;q=0.8,es;q=0.7,de;q=0.6",
    "Priority": "u=0, i",
    "Referer":base_url,
    "Sec-Ch-Ua":'"Chromium";v="140", "Not=A?Brand";v="24", "Microsoft Edge";v="140"',
    "Sec-Ch-Ua-Mobile":"?0",
    "Sec-Ch-Ua-Platform":'"Windows"',
    "Sec-Fetch-Dest":None,
    "Sec-Fetch-Mode":"cors",
    "Sec-Fetch-Site":"same-origin",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36 Edg/140.0.0.0",
}
def make_news_paylaod(page:int):
    payload= {
        "insighttypes":"ee165152-e323-43c6-842f-4f261d772231",
        "page":page,
        "take":100,
        "sc_lang":"en",
        "sc_site":"main"
    }
    return payload

payload = make_news_paylaod(page=1)
url=urllib.parse.urlencode(payload)
actual_url = f"{base_url}?{url}"
print(actual_url)

publishedDate=row["displayDate"]
id=row["id"]
title=row["title"]
url=row["url"]




def make_payload(letter:str,page:int)->dict:
    payload=  {
    "lastnameletter":letter,
    "page":page,
    "take":"12",
    "sc_lang":"en",
    "sc_site":"main"
    }
    return payload

"""
email=get["email"],
id=get["id"],
name=get["name"],
position=get["title"],
url=get["url"],
https://www.ropesgray.com/en/news-and-events?insighttypes=ee165152-e323-43c6-842f-4f261d772231&insighttypes=faf49d78-dd29-4ca3-ba91-1abb1077dc94&insighttypes=c3656807-5bf0-4bf7-bc1b-494e6025d34e&associations=0be571f2-bdad-4449-9ca9-973394e242b3


[
  {
    "text": "Hong Kong",
    "url": "/en/locations/hong-kong"
  },
  {
    "text": "Boston",
    "url": "/en/locations/boston"
  }
]
[
  "+852 3664 6319",
  "+1 617 235 4865"
]

"""