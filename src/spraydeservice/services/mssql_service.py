import pytds

from spraydeservice.services.base import (
    ResultStatus,
    ServiceResult,
    SprayContext,
    is_port_open,
)

SERVICE_NAME = "mssql"


def check_mssql(context: SprayContext, port: int) -> ServiceResult:
    def result(status: ResultStatus, detail: str = "") -> ServiceResult:
        return ServiceResult(
            service=SERVICE_NAME,
            port=port,
            status=status,
            detail=detail,
        )

    if not is_port_open(context.host, port, context.timeout):
        return result(ResultStatus.NETWORK_ERROR, "Port is closed or unreachable")

    connection = None
    try:
        connection = pytds.connect(
            dsn=context.host,
            database="master",
            user=context.username,
            password=context.password,
            port=port,
            timeout=context.timeout,
            login_timeout=context.timeout,
        )
        return result(ResultStatus.SUCCESS)
    except pytds.tds_base.OperationalError as error:
        return result(ResultStatus.AUTH_FAILED, str(error))
    except (OSError, pytds.tds_base.Error) as error:
        return result(ResultStatus.NETWORK_ERROR, str(error))
    except Exception as error:
        return result(ResultStatus.NETWORK_ERROR, f"Unexpected error: {error}")
    finally:
        if connection is not None:
            try:
                connection.close()
            except Exception:
                pass
