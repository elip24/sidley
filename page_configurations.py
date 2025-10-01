
prefix='https://www.velaw.com//'
API_URL='https://www.velaw.com/api/news?page=3&sort=newest&category=news-787'
header={
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "en-US,en;q=0.5",
        "Priority": "u=1, i",
        "Referer": "https://www.velaw.com/",
        "Sec-Ch-Ua": '"Chromium";v="140", "Not=A?Brand";v="24", "Microsoft Edge";v="140"',
        "Sec-Ch-Ua-Mobile":"?0",
        "Sec-Ch-Ua-Platform":"Windows",
        "Sec-Fetch-Dest": None,
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36 Edg/140.0.0.0",
}

def make_payload(page:int):
    page=1
    size=12 #Static due to site
    payload={
        'page':page,
        'sort':'newest',
        'category':'news-787',
    }

def api_con
