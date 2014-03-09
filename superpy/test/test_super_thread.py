from superpy import SuperThread
import time

def test_basic():

    class T(SuperThread):
        def bootstrap(self):
            self.i = 0

        def sleep(self):
            time.sleep(0.01)

        def work(self):
            self.i += 1

        def cleanup(self):
            assert self.i > 0

    t = T()
    t.start()
    time.sleep(0.1)
    t.terminate()

    assert t.terminated()
    t.join()
    assert not t.is_alive()
