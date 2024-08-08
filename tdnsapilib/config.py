"""Module config for package tdnsapilib."""

from tdnsapilib.consts import VERSION

_user_agent = "technitium-api-client-lib-{0}".format(VERSION)


def user_agent() -> str:
    return _user_agent


def set_user_agent(agent: str) -> None:
    global _user_agent
    _user_agent = agent
