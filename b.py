import threading
import time
from queue import Queue

import requests


class GThread(threading.Thread):

    def __init__(self, i, q):
        super(GThread, self).__init__()
        self.i = i
        self.que = q

    def run(self):
        u = requests.get('http://118.126.104.198:9755/login')
        self.que.put((self.i, len(u.content)))


t1 = time.clock()
que = Queue(500)

threads = []
for x in range(500):
    threads.append(GThread(x, que))

for t in threads:
    t.start()

while True:
    if que.full():
        break

print(time.clock() - t1)

