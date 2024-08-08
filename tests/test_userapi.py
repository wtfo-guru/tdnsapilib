from tdnsapilib.userapi import login, logout


def test_login_logout(login_server) -> None:
    res = login(login_server.name)
    assert res.get("status", "nobueno") == "ok"
    res = logout(login_server.name)
    assert res.get("status", "nobueno") == "ok"
