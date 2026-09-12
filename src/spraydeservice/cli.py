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

if __name__=="__main__":
    main()