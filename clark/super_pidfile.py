import os

class SuperPidfile(object):
    def __init__(self, path):
        self._path = path
        with open(self._path, 'w') as f:
            f.write(str(os.getpid()))

    def __del__(self):
        self.close()

    def close(self):
        os.remove(self._path)
