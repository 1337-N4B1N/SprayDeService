import sys

from spraydeservice.parse_arguments import parse_arguments
from spraydeservice.resolve_target import resolve_target
from spraydeservice.services.base import SprayContext,ServiceResult
from spraydeservice.services.ssh_service import check_ssh
from spraydeservice.services.ftp_service import check_ftp 
from spraydeservice.services.smb_service import check_smb
from spraydeservice.output import format_result
def main() -> None:
    args = parse_arguments()
    
    try:
        ip = resolve_target(args.host)
    except ValueError as error:
        print(f"Error: {error}")
        sys.exit(1)

    print(f"Target: {args.host}")
    print(f"The ip address of target is: {ip}")
    print(
        f"Scanning {args.services or 'all'} services on ports "
        f"{args.ports or 'default'} of target {args.host} "
        f"with username: {args.username}"
    )
    context=SprayContext(
        host=ip,
        username=args.username,
        password=args.password,
    
    )

   

    for service, port in zip(args.services, args.ports):
        if service == "ssh":
            result = check_ssh(context, port)
            print(format_result(result))
        elif service=="ftp":
            result=check_ftp(context,port)
            print(format_result(result))
        elif service=="smb":
            result=check_smb(context,port)
            print(format_result(result))
        else:
            print(f"[skipped] {service}:{port} — not implemented yet")



if __name__ == "__main__":
    main()