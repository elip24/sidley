
prefix='https://www.paulweiss.com/'
API_URL='https://www.kirkland.com/api/sitecore/ProfessionalsApi/Lawyers?letter=A'
header={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36 Edg/139.0.0.0",
        "Accept-Language": "es,es-ES;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,es-AR;q=0.5",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Priority": "u=0, i",
        "Cache-Control": "max-age=0",
        "Pragma": "no-cache",
        "Upgrade-Insecure-Requests": "1",
}

def make_payload(page:int)->dict:
    payload=  {
    "PageId": "2907",
    "pageSize":100,
    "pagingNumber":page,
    "industries":"All",
    "lawyerName":"All",
    "type":"client News",
    "practices":"All",
    "dateRange": 0,
    "searchText": "All"
    }
    return payload
#mas o menos 1150

def make_payload_profiles(page:int)->dict:
    payload=  {
    "PageId": "1492",
    "pageSize":100,
    "pagingNumber":page,
    "position":"All",
    "practices":"All",
    "industries":"All",
    "offices":"All",
    "schools": "All",
    "lastname":"All",
    "searchText": "All"
    }
    return payload
#mas o menos 1497


https://www.paulweiss.com/insights/client-news?PageId=2907&pageSize=1000&pagingNumber=1&industries=All&lawyerName=All&type=client%20News&practices=All&dateRange=0&searchText=All
