from pynput import keyboard
from utils import HTMLoader
from utils import findAllHyperlink
import json
import os
import re

class keyboardControl:
    def __init__(self):
        self.keyboardListener = None
        self.initUrls = ['https://www.fst.um.edu.mo/']
        if os.path.isfile('urlSet.json'):
            with open('urlSet.json', 'r') as f:
                self.urlSet = json.load(f)
        else:
            self.urlSet = {u:0 for u in self.initUrls}

        if os.path.isfile('urlQueue.json'):
            with open('urlQueue.json', 'r') as f:
                self.urlQueue = json.load(f)
        else:
            self.urlQueue = self.initUrls.copy()

    def onPress(self, key):
        if key == keyboard.Key.esc:
            # Stop listener
            self.keyboardListener.stop()
            print('saving...')
            with open('urlSet.json', 'w') as f:
                json.dump(self.urlSet, f)
            with open('urlQueue.json', 'w') as f:
                json.dump(self.urlQueue, f)
            os._exit(0)

    def startListener(self):
        self.keyboardListener = keyboard.Listener(on_press=self.onPress)
        self.keyboardListener.start()
        print(self.keyboardListener) 
        # self.keyboardListener.join()

ExList = ['.pdf', '.ppt', '.zip', '.rar', '.doc', '.mp3', '.mp4', '.avi', '.jpg', '.gif', '.png']
loader = HTMLoader()
kc = keyboardControl()
kc.startListener()

while(len(kc.urlQueue)):
    url = kc.urlQueue.pop(0)
    print(url)
    allHyperLinks = findAllHyperlink(loader, url)
    for hl in allHyperLinks:
        if hl.find('?') != -1:
            continue
        if hl in kc.urlSet:
            pass
        else:
            kc.urlSet[hl] = 0
            if hl[-4:] not in ExList:
                kc.urlQueue.append(hl)
            else:
                print(hl[-4:])
    print(len(kc.urlQueue))
    
