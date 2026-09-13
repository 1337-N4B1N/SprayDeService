import psycopg

from spraydeservice.services.base import (
    ResultStatus,
    ServiceResult,
    SprayContext,
    is_port_open,
)

SERVICE_NAME = "postgresql"


def check_postgresql(context: SprayContext, port: int) -> ServiceResult:
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
        connection = psycopg.connect(
            host=context.host,
            port=port,
            user=context.username,
            password=context.password,
            dbname="postgres",
            connect_timeout=context.timeout,
        )
        return result(ResultStatus.SUCCESS)
    except psycopg.OperationalError as error:
        return result(ResultStatus.AUTH_FAILED, str(error))
    except (OSError, psycopg.Error) as error:
        return result(ResultStatus.NETWORK_ERROR, str(error))
    except Exception as error:
        return result(ResultStatus.NETWORK_ERROR, f"Unexpected error: {error}")
    finally:
        if connection is not None:
            try:
                connection.close()
            except Exception:
                pass
