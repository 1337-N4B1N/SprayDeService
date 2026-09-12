import socket
from dataclasses import dataclass
from enum import Enum

DEFAULT_TIMEOUT_SECONDS = 5
class ResultStatus(Enum):
    SUCCESS = "success"
    AUTH_FAILED = "auth_failed"
    NETWORK_ERROR = "network_error"

@dataclass
class SprayContext:
    host: str
    username: str
    password: str
    timeout: int = DEFAULT_TIMEOUT_SECONDS
@dataclass
class ServiceResult:
    service: str
    port: int
    status: ResultStatus
    detail: str = ""

def is_port_open(host: str, port: int, timeout: int = DEFAULT_TIMEOUT_SECONDS) -> bool:
    "Why to waste time checking credentials if the port itself is closed?So lets check if port is open or not at first."
    try:
        with socket.create_connection((host, port), timeout=timeout):
            return True
    except OSError:
        return False