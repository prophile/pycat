"""Communication link driver."""

import sys
import select


def talk(socket, source=sys.stdin.buffer, sink=sys.stdout.buffer):
    """Run communication, in a loop. Input from `source` is sent on `socket`,
    and data received on `socket` is forwarded to `sink`.

    All file descriptors must be non-blocking.
    """

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
