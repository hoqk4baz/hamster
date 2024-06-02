import requests
import json
import time
import os
#import console
headers = {
    "Accept-Language": "tr-TR,tr;q=0.9",
    "Connection": "keep-alive",
    "Sec-Fetch-Site": "cross-site",
    "x-cv": "612",
    "Accept": "*/*",
    "x-app": "tapswap_server",
    #"Content-Id": "6783647361", # neye göre belirleniyor bilmiyorum kendi content id ile değiltirirsin
    #"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOjY3ODM5Mzg2OTUsImlhdCI6MTcxNzM1NDkwOSwiZXhwIjoxNzE3MzU4NTA5fQ.baJiKCLj2TYYHXVsRtUpliKVeJMmahe1rojAnVIsHaU",
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 17_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148",
    "Content-Type": "application/json",
    "Accept-Encoding": "gzip, deflate, br",
    "Sec-Fetch-Dest": "empty",
    "Origin": "https://app.tapswap.club",
    "Sec-Fetch-Mode": "cors",
    "Referer": "https://app.tapswap.club/",
    "Host": "api.tapswap.ai",
    "x-bot": "no",
    #"Content-Length": "32"
}

login_data = {
  "init_data": "query_id=AAGHsFoUAwAAAIewWhR6jwBI&user=%7B%22id%22%3A6783938695%2C%22first_name%22%3A%22Kimse%20Bilmez%22%2C%22last_name%22%3A%22%22%2C%22username%22%3A%22SikimdeDeil%22%2C%22language_code%22%3A%22tr%22%2C%22is_premium%22%3Atrue%2C%22allows_write_to_pm%22%3Atrue%7D&auth_date=1717341524&hash=80c99922dbf30f09afa36473d59117f82527c0d098a8e888f146d2f01c9ecab3",
  "referrer": "",
  "bot_key": "app_bot_1" # telegram data
}
login_url = "https://api.tapswap.ai/api/account/login"
api_url = 'https://api.tapswap.ai/api/player/submit_taps'


while True:
    # start_time = int(time.time() * 1000)
    
    rr = requests.post(login_url, headers=headers, data=json.dumps(login_data)).json()["access_token"]
    tokens = rr
    
    time.sleep(2)
    os.system("clear")
    while True:
        headers2 = {
            "Accept-Language": "tr-TR,tr;q=0.9",
            "Connection": "keep-alive",
            "Sec-Fetch-Site": "cross-site",
            "x-cv": "612",
            "Accept": "*/*",
            "x-app": "tapswap_server",
            "Content-Id": "6783647361", # neye göre belirleniyor bilmiyorum, kendi content id ile değiştirirsin
            "Authorization": f"Bearer {tokens}",
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 17_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148",
            "Content-Type": "application/json",
            "Accept-Encoding": "gzip, deflate, br",
            "Sec-Fetch-Dest": "empty",
            "Origin": "https://app.tapswap.club",
            "Sec-Fetch-Mode": "cors",
            "Referer": "https://app.tapswap.club/",
            "Host": "api.tapswap.ai",
            "x-bot": "no",
            # "Content-Length": "32"
        }

        request_data = {
            "taps": 100000,
            "time": 1717341584714
        }

        response = requests.post(api_url, data=json.dumps(request_data), headers=headers2).json()
        if "player" in response:
        	print(f"\r[+] {response['player']['shares']} Coin Toplandi\r", end='')
        	time.sleep(260)
        else:
        	print("[x] Token Suresi Doldu Yenileniyor...")
        	break
        
