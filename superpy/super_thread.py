import threading

class SuperThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self._stop = threading.Event()

    def run(self):
        self.bootstrap()
        while not self.terminated():
            self.sleep()
            self.work()
        self.cleanup()

    def sleep(self):
        pass

    def bootstrap(self):
        pass

    def work(self):
        pass

    def cleanup(self):
        pass

    def terminated(self):
        return self._stop.isSet()

    def terminate(self):
        self._stop.set()
