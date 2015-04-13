"""Communication link driver."""

import sys
import select


def talk(socket, source=None, sink=None):
    """Run communication, in a loop. Input from `source` is sent on `socket`,
    and data received on `socket` is forwarded to `sink`.

    If `source` or `sink` are not provided, sys.stdin and sys.stdout are used.

    All file descriptors must be non-blocking.
    """

    # Query these here, rather than in the arguments, to appease nose.
    # Nose, through its mechanism for capturing stdout, doesn't have a .buffer
    # on sys.stdout, so this causes an error when the module is imported.
    if source is None:
        source = sys.stdin.buffer
    if sink is None:
        sink = sys.stdout.buffer

    OUTPUT_BUFFER_SIZE = 1024

    while True:
        readable, writable, exceptional = select.select((socket, source),
                                                        (),
                                                        (socket, source, sink))
        if exceptional:
            break  # Leave in case of closed sockets and such
        if source in readable:
            socket.send(source.readline())
        if socket in readable:
            sink.write(socket.recv(OUTPUT_BUFFER_SIZE))
            sink.flush()
