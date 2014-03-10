=====
Clark
=====

.. code:: bash

    pip install clark

Testing
=======

.. image:: https://travis-ci.org/carlsverre/clark.png
    :target: https://travis-ci.org/carlsverre/clark

Run tests by executing :code:`python setup.py test`.

Classes
=======

Super ArgParser
---------------
A nicer way to deal with config files and argparser:

config_file.cnf:

.. code:: text

    test = 1
    debug

Your app:

.. code:: python

    from clark import SuperArgParser, ConfigFileAction

    parser = SuperArgParser()

    parser.add_argument('-c', action=ConfigFileAction)
    parser.add_argument('--debug', action='store_true')
    parser.add_argument('--test', type=int)
    parser.add_argument('--engage')

    options = parser.parse_args([
        '--engage', 'foo',
        '-c', 'config_file.cnf'
    ])

    assert options.test == 1
    assert options.engage == 'foo'
    assert options.debug is True

Super Enum
---------------
A simple Enum class with lots of nice properties.

.. code:: python

    from clark import SuperEnum

    class Colors(SuperEnum):
        red = SuperEnum.E
        blue = SuperEnum.E
        green = SuperEnum.E

    class OtherColors(SuperEnum):
        yellow = SuperEnum.E
        red = SuperEnum.E

    red = Colors['red']
    red = Colors.red

    assert red in Colors

    assert str(red) == 'red'
    assert red == Colors.red

    assert Colors.red != OtherColors.red

    class Foo(object):
        class Colors(SuperEnum):
            blue = SuperEnum.Element

    assert Foo.Colors.blue != Colors.blue

Super JSON
----------
Make simplejson slightly better (don't crash on datetime objects)

.. code:: python

    from clark import super_json
    
    now = datetime.datetime.now()
    x = super_json.loads(super_json.dumps({ 'a': now }))
    assert x['a'] == now.isoformat()

Super PidFile
-------------
A simple PidFile class.  Instantiate when you boot up, and close it when you exit.

.. code:: python

    from clark import SuperPidFile
    
    pidfile = SuperPidFile()
    try:
        ... run your app ...
    finally:
        pidfile.close()

Super Thread
------------
Threads that terminate nicely and are awesome.

.. code:: python

    from clark import SuperThread
    
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
    
    time.sleep(1)
    
    t.terminate()
    t.join()
    
    assert not t.is_alive()
