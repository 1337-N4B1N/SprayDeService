import ipaddress
import socket


def resolve_target(target: str) -> str:
    """Return an IP address for either an IP literal or a hostname."""
    try:
        return str(ipaddress.ip_address(target))
    except ValueError:
        return socket.gethostbyname(target)