"""Module response for package tdnsapilib."""

from api_client.endpoint import Endpoint
from api_client.request import RestRequest

from tdnsapilib.config import user_agent
from tdnsapilib.servers import DnsServer


def rest_request(
    server: DnsServer,
    endpoints: Endpoint | list[Endpoint],
) -> RestRequest:
    return RestRequest(
        endpoints=endpoints,
        api_root=str(server.root),
        user_agent=user_agent(),
    )
