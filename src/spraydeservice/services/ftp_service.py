from ftplib import FTP,error_perm
from spraydeservice.services.base import(
    ResultStatus,
    SprayContext,
    ServiceResult,
    is_port_open,
)
SERVICE_NAME="ftp"
def check_ftp(context:SprayContext,port:int)->ServiceResult:
    def result(status:ResultStatus,detail:str="")->ServiceResult:
        return ServiceResult(service=SERVICE_NAME,port=port,
        status=status,detail=detail)
    # print(f"--------------------------------------------------------")
    # print(f"Checking FTP:")
    if not is_port_open(context.host,port,context.timeout):
        return result(ResultStatus.NETWORK_ERROR,"Port is closed or unreachable")

    ftp=FTP()
    try:
        ftp.connect(host=context.host,port=port,timeout=context.timeout)
        ftp.login(user=context.username,passwd=context.password)
        return result(ResultStatus.SUCCESS)
    except error_perm as error:
        return result(ResultStatus.AUTH_FAILED,str(error))
    except OSError as error:
        return result(ResultStatus.NETWORK_ERROR,str(error))
    finally:
        ftp.close()
       
    