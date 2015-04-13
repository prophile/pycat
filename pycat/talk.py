"""Communication link driver."""

import sys
import selectors


CLIENT_TO_SERVER = object()
SERVER_TO_CLIENT = object()


def talk(socket, source=sys.stdin.buffer, sink=sys.stdout.buffer):
    """Run communication, in a loop. Input from `source` is sent on `socket`,
    and data received on `socket` is forwarded to `sink`.

    All file descriptors must be non-blocking.
    """

    OUTPUT_BUFFER_SIZE = 1024

    with selectors.DefaultSelector() as selector:
        selector.register(source, selectors.EVENT_READ, CLIENT_TO_SERVER)
        selector.register(socket, selectors.EVENT_READ, SERVER_TO_CLIENT)
        while True:
            for key, events in selector.select():
                if key.data is CLIENT_TO_SERVER:
                    data = source.readline()
                    socket.send(data)
                elif key.data is SERVER_TO_CLIENT:
                    data = socket.recv(OUTPUT_BUFFER_SIZE)
                    sink.write(data)
                    sink.flush()
