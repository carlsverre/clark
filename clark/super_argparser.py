import argparse
import re
import sys

_re_equals = re.compile(r'\s*=\s*')
_re_comment = re.compile(r'^\s*#.*$')

class _ConfigFilePending(object):
    def __init__(self, config_path):
        self.path = config_path

class ConfigFileAction(argparse.Action):
    def __call__(self, parser, namespace, config_file_path, option_string=None):
        setattr(namespace, self.dest, _ConfigFilePending(config_file_path))

class SuperArgParser(argparse.ArgumentParser):
    def __init__(self, *args, **kwargs):
        kwargs['fromfile_prefix_chars'] = '@'
        super(SuperArgParser, self).__init__(*args, **kwargs)

    def convert_arg_line_to_args(self, arg_line):
        arg_line = arg_line.strip()

        if _re_comment.match(arg_line) or not arg_line.strip():
            return

        # cleanup whitespace around equals
        arg_line = re.sub(_re_equals, '=', arg_line)

        # magic! no positionals allowed in config file
        if not arg_line.startswith('-'):
            arg_line = '--' + arg_line

        for arg in arg_line.split():
            yield arg

    def parse_args(self, args=None):
        args = sys.argv[1:] if args is None else args
        options = super(SuperArgParser, self).parse_args(args)

        # collectd pending config files
        config_files = [v.path for v in vars(options).values() if isinstance(v, _ConfigFilePending)]

        if config_files:
            args = ["@%s" % path for path in config_files] + args
            options = super(SuperArgParser, self).parse_args(args)

        return options
