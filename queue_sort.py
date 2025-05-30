import threading
from queue import Queue

started = False
running = True

class producer(threading.Thread):

    def __init__(self, list_of_numbers):
        threading.Thread.__init__(self)
        self.list_items = list_of_numbers

    def run(self):
        started = True
        for i in self.list_items:
            queue.put(str(i))
            print("Число отправлено")
        running = False

class consumer(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        started = True
        while started:
            queue_ret = queue.get()
            print("Число", queue_ret, "принято")
            
queue = Queue()