"""Module userapi for package tdnsapilib."""

from typing import Any

from api_client.endpoint import Endpoint, HTTPMethod

from tdnsapilib.reqresp import rest_request
from tdnsapilib.servers import get_server


def login(server: str = "", **kwargs: bool) -> dict[str, Any]:
    o_svr = get_server(server)
    if not o_svr.username or not o_svr.password:
        raise ValueError(
            "Server {0} is missing username or password property".format(o_svr.name)
        )

    if "includeInfo" in kwargs.keys():
        query_parameters.append("includeInfo")
    endpoint = Endpoint(
        name="login",
        path="/api/user",
        request_method=HTTPMethod.GET,
        query_parameters=["user", "pass"],
    )
    req = rest_request(o_svr, endpoint)
    q_args = {"user": o_svr.username, "pass": o_svr.password, "includeInfo":
    resp = req.call_endpoint("login", user=o_svr.username, pass=o_svr.)


def logout(server: str = "") -> None:
    o_svr = get_server(server)
    if not o_svr.token:
        raise ValueError("Server {0} has no token to logout with.".format(o_svr.name))
