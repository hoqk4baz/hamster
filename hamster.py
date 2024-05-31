import requests
import time

url = "https://api.hamsterkombat.io/clicker/tap"

headers = {
    "Host": "api.hamsterkombat.io",
    "Content-Length": "55",
    "Sec-Ch-Ua": '"Android WebView";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Sec-Ch-Ua-Mobile": "?1",
    "Authorization": "Bearer 1717116343708PAd1IgfKcPTkXFC465fcwfffbmiYRgfE9SfYQ1TSXZnBK1CzexcrIGpqCoDG9PSg6783938695",
    "User-Agent": "Mozilla/5.0 (Linux; Android 9; SM-N9788 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/125.0.6422.82 Mobile Safari/537.36",
    "Sec-Ch-Ua-Platform": '"Android"',
    "Origin": "https://hamsterkombat.io",
    "X-Requested-With": "org.telegram.messenger",
    "Sec-Fetch-Site": "same-site",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://hamsterkombat.io/",
    "Accept-Language": "tr,tr-TR;q=0.9,en-US;q=0.8,en;q=0.7",
    "Priority": "u=1, i",
    "Connection": "keep-alive"
}

data = {
    "count": 10000000000,
    "availableTaps": 300000000000000,
    "timestamp": 9717118869
}

while True:
    response = requests.post(url, headers=headers, json=data).json()["clickerUser"]["balanceCoins"]
    print(f"\r[+] Toplam Coin: {response}\r",end="")
    time.sleep(260)
