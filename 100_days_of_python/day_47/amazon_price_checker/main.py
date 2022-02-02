import requests
from bs4 import BeautifulSoup
import pprint

URL = 'https://smile.amazon.com/AmazonBasics-Small-Carrying-GoPro-Accessories/dp/B00PMMBBSG/?_encoding=UTF8&pd_rd_w=O6hkf&pf_rd_p=fe5efc42-c863-409d-991f-f49517db3800&pf_rd_r=W5H3S790HC7979EYRYDS&pd_rd_r=97746fff-f478-4217-b555-bed02abd1cd1&pd_rd_wg=1d4EY&ref_=pd_gw_unk&th=1'

headers = {
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
}

response = requests.get(url=URL, headers=headers).text

soup = BeautifulSoup(response, 'html.parser')

price = soup.find(name='span', class_='a-offscreen').text

print(price)