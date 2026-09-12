from spraydeservice.parse_arguments import parse_arguments
from spraydeservice.resolve_domain import resolve_target
def main() -> None:
    print(f"Hello world!")
    args = parse_arguments()
    print(f"Target: {args.host}")
    print(f"The ip address of target is: {resolve_target(args.host)}")
    print(f"Username: {args.username}")
    print(f"Services: {args.services or 'all'}")
    print(f"Ports: {args.ports or 'defaults'}")
    print(f"Scanning {args.services or 'all'} services on {args.ports or 'default'} ports of target {args.host} with username:{args.username} and password:{args.password}")
if __name__=="__main__":
    main()