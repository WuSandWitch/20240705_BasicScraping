import requests

url = 'https://tcgbusfs.blob.core.windows.net/dotapp/news.json'

r = requests.get(url)

data = r.json()

print('更新時間', data['updateTime'])
print('新聞: ')
print('---')

for news in data['News']:
    print('標題: ',news['chtmessage'])
    print('內容: ', news['content'])
    print('---')