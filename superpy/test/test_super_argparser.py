from superpy import SuperArgParser, ConfigFileAction

def test_basic():
    parser = SuperArgParser()

    with open('/tmp/foo', 'w') as f:
        f.write('test = 1')

    parser.add_argument('-c', action=ConfigFileAction)
    parser.add_argument('--test', type=int)
    out = parser.parse_args(['-c', '/tmp/foo'])

    assert out.test == 1
