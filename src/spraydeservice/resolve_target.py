import ipaddress
import socket


def resolve_target(target: str) -> str:
    """Return a valid IPv4 address for an IPv4 literal or hostname."""
    target = target.strip()
    if not target:
        raise ValueError("Target cannot be empty")

    if ":" in target:
        raise ValueError(f"IPv6 addresses are not supported: {target}")

    try:
        address = ipaddress.IPv4Address(target)
        return str(address)
    except ValueError:
        pass  # not a valid IPv4 literal — fall through below

    if _looks_like_ipv4(target):
        raise ValueError(f"Invalid IPv4 address: {target}")

    try:
        return socket.gethostbyname(target)
    except socket.gaierror:
        raise ValueError(f"Could not resolve hostname: {target}")


def _looks_like_ipv4(target: str) -> bool:
    """Check if a string is shaped like a dotted-quad IPv4 address, valid or not."""
    parts = target.split(".")
    return len(parts) == 4 and all(part.isdigit() for part in parts)