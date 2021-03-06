import asyncio
import unittest

from juju.client.connection import Connection
from ..base import bootstrapped


@bootstrapped
class FunctionalConnectionTest(unittest.TestCase):
    def test_connect_current(self):
        loop = asyncio.get_event_loop()
        conn = loop.run_until_complete(
            Connection.connect_current())

        self.assertIsInstance(conn, Connection)
