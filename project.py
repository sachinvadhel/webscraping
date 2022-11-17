import requests
from bs4 import BeautifulSoup

def get_price(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    price = soup.find('span', {'itemprop': 'price'})['content']
    return price 

def add_price(p1, p2, p3):
    totel = (float(p1) + float(p2) + float(p3))
    return totel

iphone14 : get_price('https://www.ebay.de/itm/144748008541?epid=10056260189&hash=item21b3a7545d:g:VBMAAOSw03tjJtJl&amdata=enc%3AAQAHAAAAoLnVGllgnZK7tsUTBVUfPHzzeh8aMp2M8WUtp1pxms3ZUYFPSU633f3T4kxWx60xy045uazXvp1Y4898S1HmSrvZCmKlp%2F1qbAAqQZ84So2iGsvn4Of%2FAbv%2FBd%2BcCoHNOlHeTOM%2BhG2TFdLpAZYZkVgbA2sqvdZweIh8rIEn2e%2FK5FjEpajlWAxi%2BQQ%2Feg14KLrkAswvzwWNRx29USNrMPc%3D%7Ctkp%3ABk9SR6KRwLGQYQ')
iphone13promax : get_price('https://www.ebay.de/itm/134201328565?_trkparms=amclksrc%3DITM%26aid%3D1110006%26algo%3DHOMESPLICE.SIM%26ao%3D1%26asc%3D243418%26meid%3Dfd3b6eb67cb9464f9ec0434e7c29bd06%26pid%3D101195%26rk%3D4%26rkt%3D12%26sd%3D144748008541%26itm%3D134201328565%26pmt%3D1%26noa%3D0%26pg%3D2047675%26algv%3DSimplAMLv11WebTrimmedV3MskuWithRevOptLambda90KnnRecallV1LesShipping%26brand%3DApple&_trksid=p2047675.c101195.m1851&amdata=cksum%3A134201328565fd3b6eb67cb9464f9ec0434e7c29bd06%7Cenc%3AAQAHAAABIFWRPpf%252FDa5vn4SEuceq169ve1nVKV2UcyqVYubu5TTZcmr03O0GOPfaRlPO9XKtRm3lzz2HvRlCfhvplQfG5wRloozh3DKzvzF5RJEp6%252FKLto6N3LEsDlsw1cFikCsLYfctGh98CZZRgCw%252BldhAWD24IYQ1jaeOnwRyKOhQYBYvmBtIZnmLu9pdtPWs9c2vjmo%252Fukn%252B3zM5uyhzUQ9tCYOQXF%252BI8HRaGCAQAaITsPjxBwZRFp%252FyaKfi3042mFlRtMJ5VyQkRyVOrd3CLgqRrkvFp%252F%252F5TUxVFpxpuKVmF%252FEfxr228eskcXpT1%252FRioZYZzi4nYObxAuavH3X3nDI1jLuoz3Q3oSCO3XM%252FR8koythvqYAxo6ymfwJ4Dd8kW7w%252FTg%253D%253D%7Campid%3APL_CLK%7Cclp%3A2047675')
iphone12mini : get_price('https://www.ebay.de/itm/193848189519?epid=24042292582&hash=item2d2240a24f:g:puIAAOSwIJ9jcznx&amdata=enc%3AAQAHAAAA4GhSYoKWw0NGhsV9wH2QeUSYohw8Z%2BE5xIFyBO9HJrAW1PNQYEh0TXp7ZL52adA2GSg1k48KHefQo%2F59OMjHvA5789hn2q3RBcLr0N9y759vjJoQGhE0XQTxuc%2BDiao3Pw8r%2F5F2THz%2Bg6cCykOH92w4IDoXNfq3mN0KjQsvgKdUDIQDm3yiVUrrcaDnJtblYXsCutrbmwu5smfhKisEdPjTMDY0vXmo%2B74YwuM0bXX2TSpNlyQbDCJoplxJLdOo5V580NoO7i9zMcyNKPA0ulu1DPX1xyjMa9D2wtrVZqN4%7Ctkp%3ABFBMnrGdtJBh')

total_price = add_price(iphone14, iphone13promax, iphone12mini)

print(total_price)