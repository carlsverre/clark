===========
SuperPy
===========

Testing
=======

.. image:: https://travis-ci.org/carlsverre/superpy.png
    :target: https://travis-ci.org/carlsverre/superpy

Run tests by executing :code:`python setup.py test`.

Classes
=======

Super Argparser
---------------
A nicer way to deal with config files and argparser:

config_file.cnf:

.. code:: text

    test = 1
    debug

Your app:

.. code:: python

    from superpy import SuperArgParser, ConfigFileAction

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
