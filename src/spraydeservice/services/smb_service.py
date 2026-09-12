from smb.SMBConnection import SMBConnection
from smb.base import  SMBTimeout

from spraydeservice.services.base import(
    ResultStatus,
    ServiceResult,
    SprayContext,
    is_port_open,
)
SERVICE_NAME="smb"
def check_smb(context:SprayContext,port:int)->ServiceResult:
    def result(status:ResultStatus,detail:str="")->ServiceResult:
        return ServiceResult(service=SERVICE_NAME,port=port,status=status,detail=detail)
    print(f"--------------------------------------------------------")
    print(f"Checking SMB:")

    if not is_port_open(context.host,port,context.timeout):
        return result(ResultStatus.NETWORK_ERROR,"Port closed or unreachable")

    conn=SMBConnection(
        context.username,
        context.password,
        "spraydeservice",
        context.host,
        use_ntlm_v2=True,
        is_direct_tcp=True,
    )
    try:
        connected=conn.connect(context.host,port,timeout=context.timeout)
        if connected:
            return result(ResultStatus.SUCCESS)
        return result(ResultStatus.AUTH_FAILED,"Authentication failed")
    except SMBTimeout as error:
        return result(ResultStatus.NETWORK_ERROR,str(error))
    except OSError as error:
        return result(ResultStatus.NETWORK_ERROR,str(error))
    finally:
        conn.close()
  