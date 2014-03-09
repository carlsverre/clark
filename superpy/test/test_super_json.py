from superpy import super_json
import datetime

def test_basic():
    x = { 'a': 1 }
    assert x == super_json.loads(super_json.dumps(x))

def test_datetime():
    now = datetime.datetime.now()
    x = super_json.loads(super_json.dumps({ 'a': now }))
    assert x['a'] == now.isoformat()
