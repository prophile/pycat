"""usage: pycat [options] <hostname> <port>

netcat, in Python

positional arguments:
  hostname    host to which to connect
  port        port number to which to connect

optional arguments:
  -h, --help   show this help message and exit
"""

from docopt import docopt
import sys
import socket
from .talk import talk


def main(args=None):
    """Run, as if from the command-line.

    args is a set of arguments to run with, defaulting to taking arguments from
    `sys.argv`. It should **not** include the name of the program as the first
    argument.
    """
    settings = docopt(__doc__, argv=args)
    try:
        sock = socket.create_connection((settings['<hostname>'],
                                         int(settings['<port>'])))
        sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        sock.setblocking(False)
        talk(sock)
    except KeyboardInterrupt:
        # Disregard Control-C, as this is probably how the user will exit.
        sock.close()
    except ConnectionError as e:
        print(str(e), file=sys.stderr)
