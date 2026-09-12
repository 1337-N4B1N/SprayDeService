import ipaddress
import socket


def resolve_target(target: str) -> str:
    try:
        return str(ipaddress.ip_address(target))
    except ValueError:
        return socket.gethostbyname(target)