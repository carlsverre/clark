from superpy import SuperArgParser, ConfigFileAction

def test_basic():
    parser = SuperArgParser()

    with open('/tmp/foo', 'w') as f:
        f.write('test = 1\n')
        f.write('debug\n')

    parser.add_argument('-c', action=ConfigFileAction)
    parser.add_argument('--test', type=int)
    parser.add_argument('--debug', action='store_true')
    out = parser.parse_args(['-c', '/tmp/foo'])

    assert out.test == 1
    assert out.debug is True
