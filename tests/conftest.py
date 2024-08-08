"""Module conftest for package tdnsapilib.tests."""

import pytest
import requests

from tdnsapilib.servers import DnsServer, add_server

TEST_SERVER = "http://localhost:5380"


def pytest_configure(config):
    try:
        requests.head(TEST_SERVER)
    except requests.exceptions.ConnectionError:
        msg = "FATAL. Connection refused: technitium dns server does not appear to be installed as a service (localhost port 5380)"  # noqa: E501
        pytest.exit(msg)


@pytest.fixture()
def login_server() -> DnsServer:
    server = add_server(
        DnsServer(name="test", root=TEST_SERVER, username="admin", password="testing")
    )
    return server
