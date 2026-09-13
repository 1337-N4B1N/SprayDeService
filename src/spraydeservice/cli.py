import sys

from concurrent.futures import ThreadPoolExecutor, as_completed
from spraydeservice.parse_arguments import parse_arguments
from spraydeservice.resolve_target import resolve_target
from spraydeservice.services.base import SprayContext,ServiceResult
from spraydeservice.services.ssh_service import check_ssh
from spraydeservice.services.ftp_service import check_ftp 
from spraydeservice.services.smb_service import check_smb
from spraydeservice.output import format_result,format_not_implemented
from spraydeservice.services import SERVICE_CHECKS


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

    with ThreadPoolExecutor(max_workers=len(args.services)) as executor:
        jobs = []
        for service, port in zip(args.services, args.ports):
            check_function = SERVICE_CHECKS.get(service)
            future = executor.submit(check_function, context, port) if check_function else None
            jobs.append((service, port, future))

        for service, port, future in jobs:
            print("-" * 58)
            print(f"Checking {service.upper()}:")
            if future is None:
                print(format_not_implemented(service,port))
                continue
            result = future.result()
            print(format_result(result))

if __name__ == "__main__":
    main()