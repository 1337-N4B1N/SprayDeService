import paramiko

from spraydeservice.services.base import (
    DEFAULT_TIMEOUT_SECONDS,
    ResultStatus,
    ServiceResult,
    SprayContext,
    is_port_open,
)
SERVICE_NAME="ssh"

def check_ssh(
        context:SprayContext,
        port:int,
        
)->ServiceResult:
    def result(status:ResultStatus,detail:str="")->ServiceResult:
        return ServiceResult(service=SERVICE_NAME,port=port,status=status,detail=detail)
    # print(f"--------------------------------------------------------")
    # print(f"Checking SSH :")
    if not is_port_open(context.host,port,context.timeout):
        return result(ResultStatus.NETWORK_ERROR,"Port is closed or unreachable")
    
    client=paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        client.connect(
            hostname=context.host,
            port=port,
            username=context.username,
            password=context.password,
            timeout=context.timeout,
        )
        return result(ResultStatus.SUCCESS)
    except paramiko.AuthenticationException:
        return result(ResultStatus.AUTH_FAILED,"Authentication Failed")
    except(paramiko.SSHException,OSError)as error:
        return result(ResultStatus.NETWORK_ERROR,str(error))
    except Exception as error:
        return result(ResultStatus.NETWORK_ERROR, f"Unexpected error: {error}")
    finally:
      try:
        client.close()
      except Exception:
          pass
 