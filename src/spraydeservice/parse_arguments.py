import argparse

from spraydeservice.parse_services import SERVICE_DEFAULTS, resolve_service_to_ports


def _validate_service_port_pairing(parser: argparse.ArgumentParser, args: argparse.Namespace) -> None:
   #  Validates there are no more ports then the services specified.
   # Remember if there are more services less ports, than remaining services goes to default ports.However if more ports, less services we throw error.
    if args.ports and not args.services:
        parser.error("--port requires --service to also be specified")

    if args.services and args.ports and len(args.ports) > len(args.services):
        parser.error(
            f"Got {len(args.ports)} ports but only {len(args.services)} services — "
            "extra ports with no matching service are not allowed"
        )
def _split_csv(value: str)->list[str]:
    raw_items = value.split(",")
    
    cleaned_items = []
    for item in raw_items:
        trimmed = item.strip()
        if trimmed:
            cleaned_items.append(trimmed)
    return cleaned_items 

def _parse_ports(value:str)->list[int]:
    raw_ports=_split_csv(value)
    ports=[]
    for raw in raw_ports:
     if not raw.isdigit():
        raise argparse.ArgumentTypeError(f"Invalid port:`{raw}` is not a number")
     port=int(raw)
     if not(1<=port<=65535):
        raise argparse.ArgumentTypeError(f"Invalid port: `{port}` is out of range (1-65535)")
     ports.append(port)
    
    return ports     

def parse_arguments()->argparse.Namespace:
   parser=argparse.ArgumentParser( prog="spraydeservice",
         description="Credentials spray against common services"
    )
   parser.add_argument(
      "-H",
      "--host",
      required=True,
      help="Target Ip address or domain name (eg. 10.10.2.34 or target.com)"
   )
   parser.add_argument(
      "-u",
      "--username",
      required=True,
      help="Username to test",
   )
   parser.add_argument(
      "-p",
      "--password",
      required=True,
      help="Password to test"
   )
   parser.add_argument(
      "-s",
      "--service",
      dest="services",
      type=_split_csv,
      default=None,
      help="Comma-se"
   )
   parser.add_argument(
      "--port",
      dest="ports",
      type=_parse_ports,
      default=None,
      help="Comma-separated list of ports, mapped positionnaly to --service"
   )
   args=parser.parse_args()
   _validate_service_port_pairing(parser,args)
   if args.services is None:
         args.services = list(SERVICE_DEFAULTS)
         args.ports = resolve_service_to_ports(args.services, None)
   elif not args.services:
         parser.error("--service must contain at least one service")
   else:
         try:
            args.ports = resolve_service_to_ports(args.services, args.ports)
         except ValueError as error:
            parser.error(str(error))
   return args