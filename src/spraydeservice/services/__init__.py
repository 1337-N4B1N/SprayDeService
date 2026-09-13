"""Service-specific credential check implementations."""
from spraydeservice.services.ssh_service import check_ssh
from spraydeservice.services.ftp_service import check_ftp
from spraydeservice.services.smb_service import check_smb
from spraydeservice.services.mysql_service import check_mysql
from spraydeservice.services.mssql_service import check_mssql
from spraydeservice.services.postgresql_service import check_postgresql
from spraydeservice.services.winrm_service import check_winrm,check_winrm_https
SERVICE_CHECKS = {
    "ssh": check_ssh,
    "ftp": check_ftp,
    "smb": check_smb,
    "mysql":check_mysql,
    "mssql": check_mssql,
    "postgresql": check_postgresql,
    "winrm": check_winrm,
    "winrm-https": check_winrm_https,
}