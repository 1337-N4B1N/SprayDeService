from spraydeservice.services.base import ResultStatus,ServiceResult
RESET = "\033[0m"
GREEN = "\033[32m"
RED = "\033[31m"
YELLOW = "\033[33m"
CYAN = "\033[36m"
STATUS_STYLE = {
    ResultStatus.SUCCESS: (GREEN, "[+]"),
    ResultStatus.AUTH_FAILED: (RED, "[-]"),
    ResultStatus.NETWORK_ERROR: (YELLOW, "[!]"),
}

def format_result(result: ServiceResult) -> str:
    color, symbol = STATUS_STYLE[result.status]
    message = result.detail or "Credentials work" if result.status == ResultStatus.SUCCESS else result.detail or result.status.value
    return f"{color}{symbol} {result.service}:{result.port} - {message}{RESET}"


def format_not_implemented(service: str, port: int) -> str:
    return f"{CYAN}[?] {service}:{port} - not implemented yet{RESET}"