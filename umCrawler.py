from utils import HTMLoader
from utils import findAllHyperlink
import json
import os


loader = HTMLoader()
initUrl = 'https://www.fst.um.edu.mo/'
if os.path.isfile('urlSet.json'):
    with open('urlSet.json', 'r') as f:
        urlSet = json.load(f)
else:
    urlSet = {initUrl:0}

if os.path.isfile('urlQueue.json'):
    with open('urlQueue.json', 'r') as f:
        urlQueue = json.load(f)
else:
    urlQueue = [initUrl]

while(len(urlQueue)):
    url = urlQueue.pop(0)
    print(url)
    allHyperLinks = findAllHyperlink(loader, url)
    for hl in allHyperLinks:
        if hl in urlSet:
            pass
        else:
            urlSet[hl] = 0
            urlQueue.append(hl)
    
    with open('urlSet.json', 'w') as f:
        json.dump(urlSet, f)
    with open('urlQueue.json', 'w') as f:
        json.dump(urlQueue, f)

urlList = list(urlSet.keys())
print(len(urlList))
with open('output.txt', 'w') as f:
    for url in urlList:
        f.write(url + '\n')