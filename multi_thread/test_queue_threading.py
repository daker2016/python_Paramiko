# ! encoding=utf-8

import queue
import threading
import time

exitFlag = 0


class myThread (threading.Thread):
    def __init__(self, threadID, name, q):
        threading.Thread.__init__(self)
        self.threadId = threadID
        self.name = name
        self.q = q

    def run(self):
        print("start thread:" + self.name)
        print_data(self.name, self.q)
        print("end thread:" + self.name)


def print_data(threadName, q):
    while not exitFlag:
        queueLock.acquire()
        if not workQueue.empty():
            data = q.get()
            queueLock.release()
            print("%s processing %s" % (threadName, data))
        else:
            queueLock.release()
        time.sleep(1)


threadList = ["Thread-1", "Thread-2", "Thread-3"]
nameList = ["One", "Two", "Three", "Four", "Five"]
queueLock = threading.Lock()
workQueue = queue.Queue(10)
threads = []
threadId = 1

for tName in threadList:
    thread = myThread(1, tName, workQueue)
    thread.start()
    threads.append(thread)
    threadId += 1

while not workQueue.empty():
    pass

exitFlag = 1

for t in threads:
    t.join()
print("exit main thread")
