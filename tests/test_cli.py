import pycat.cli as cli
from unittest.mock import patch
from io import StringIO

@patch('sys.stdout', new_callable=StringIO)
def test_help(fake_stdout):
    try:
        cli.main(['-h'])
    except SystemExit:
        pass  # Disregard SystemExit from argparse
    assert "netcat" in fake_stdout.getvalue()
