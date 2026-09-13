"""Service-specific credential check implementations."""
from spraydeservice.services.ssh_service import check_ssh
from spraydeservice.services.ftp_service import check_ftp
from spraydeservice.services.smb_service import check_smb
from spraydeservice.services.mysql_service import check_mysql
SERVICE_CHECKS = {
    "ssh": check_ssh,
    "ftp": check_ftp,
    "smb": check_smb,
    "mysql":check_mysql,
}