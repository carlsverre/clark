from clark import SuperPidfile
import os

def test_basic():
    pidfile = SuperPidfile('/tmp/foo')
    assert os.path.exists('/tmp/foo')

    with open('/tmp/foo') as f:
        assert f.read() == str(os.getpid())

    pidfile.close()
    assert not os.path.exists('/tmp/foo')
