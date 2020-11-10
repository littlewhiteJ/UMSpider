import json

with open('urlSet.json', 'r') as f:
    urlSet = json.load(f)

urlList = list(urlSet.keys())

with open('urlList.txt', 'w') as f:
    for url in urlList:
        f.write(url + '\n')