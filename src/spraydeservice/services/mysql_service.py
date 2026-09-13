
import pymysql
from spraydeservice.services.base import (
    DEFAULT_TIMEOUT_SECONDS,
    ResultStatus,
    ServiceResult,
    SprayContext,
    is_port_open,
)
SERVICE_NAME="mysql"

def check_mysql(context:SprayContext,port:int)->ServiceResult:
    def result(status:ResultStatus,detail:str="")->ServiceResult:
            return ServiceResult(service=SERVICE_NAME,port=port,status=status,detail=detail)

    if not is_port_open(context.host,port,context.timeout):
        return result(ResultStatus.NETWORK_ERROR,"Port closed or unreachable")

    connection=None
    try:
         connection=pymysql.connect(
            host=context.host,
            port=port,
            user=context.username,
            password=context.password,
            connect_timeout=context.timeout,
          )
         return result(ResultStatus.SUCCESS)
    
    except pymysql.err.OperationalError as error:
         error_code=error.args[0] if error.args else None
         if error_code in (1045,1044):
              return result(ResultStatus.AUTH_FAILED,str(error))
         return result(ResultStatus.NETWORK_ERROR,str(error))

    except OSError as error:
         return result(ResultStatus.NETWORK_ERROR,str(error))
    
    except Exception as error:
        return result(ResultStatus.NETWORK_ERROR, f"Unexpected error: {error}")

    finally:
         if connection is not None:
              try:
                connection.close
              except Exception:
                pass



        
        
             
            
         

