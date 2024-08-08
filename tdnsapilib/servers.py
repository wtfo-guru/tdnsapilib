"""Module userapi for package tdnsapilib."""

from typing import Optional

from pydantic import BaseModel, HttpUrl, SecretStr


class DnsServer(BaseModel):
    """This class contains server information for tdnsapilib."""

    name: str
    root: HttpUrl
    username: Optional[str] = None
    password: Optional[SecretStr] = None
    token: Optional[SecretStr] = None


tdns_servers: dict[str, DnsServer] = {}


def add_server(server: DnsServer) -> DnsServer:
    """Add a dns server to the tdns_servers dict.

    :param server: DnsServer to add
    :type server: DnsServer
    :raises ValueError: If server does not have a token or a username and password
    :return: The validated server object
    :rtype: DnsServer
    """
    if not server.token:
        if not server.username or not server.password:
            raise ValueError(
                "A server object must have a token or a username and password"
            )
    tdns_servers[server.name] = server
    return server


def get_server(name: str) -> DnsServer:
    """Retrieve a server from the tdns_servers dict.

    :param name: Name of the server to retrieve
    :type name: str
    :raises KeyError: If server not found
    :
    :return: DnsServer object
    :rtype: DnsServer
    """
    if tdns_servers:
        if not name:
            name = next(iter(tdns_servers))
        server = tdns_servers.get(name)
        if server is not None:
            return server
    raise KeyError("Server {0} not found!!!".format(name))
