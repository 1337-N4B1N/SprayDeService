from winrm.exceptions import AuthenticationError, WinRMTransportError
from winrm.protocol import Protocol

from spraydeservice.services.base import (
    ResultStatus,
    ServiceResult,
    SprayContext,
    is_port_open,
)

def check_winrm(context: SprayContext, port: int) -> ServiceResult:
    return _check_winrm(context, port, use_https=False)


def check_winrm_https(context: SprayContext, port: int) -> ServiceResult:
    return _check_winrm(context, port, use_https=True)


def _check_winrm(
    context: SprayContext,
    port: int,
    use_https: bool,
) -> ServiceResult:
    service_name = "winrm-https" if use_https else "winrm"

    def result(status: ResultStatus, detail: str = "") -> ServiceResult:
        return ServiceResult(
            service=service_name,
            port=port,
            status=status,
            detail=detail,
        )

    if not is_port_open(context.host, port, context.timeout):
        return result(ResultStatus.NETWORK_ERROR, "Port is closed or unreachable")

    scheme = "https" if use_https else "http"
    endpoint = f"{scheme}://{context.host}:{port}/wsman"
    protocol = None
    shell_id = None

    try:
        protocol = Protocol(
            endpoint=endpoint,
            transport="ntlm",
            username=context.username,
            password=context.password,
            operation_timeout_sec=context.timeout,
            read_timeout_sec=context.timeout + 1,
            server_cert_validation="ignore",
        )
        shell_id = protocol.open_shell()
        return result(ResultStatus.SUCCESS)
    except AuthenticationError:
        return result(ResultStatus.AUTH_FAILED, "Authentication failed")
    except (WinRMTransportError, OSError) as error:
        return result(ResultStatus.NETWORK_ERROR, str(error))
    except Exception as error:
        return result(ResultStatus.NETWORK_ERROR, f"Unexpected error: {error}")
    finally:
        if protocol is not None and shell_id is not None:
            try:
                protocol.close_shell(shell_id)
            except Exception:
                pass
