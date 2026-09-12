SERVICE_DEFAULTS = {
    # --- Remote Access & Shell Services ---
    'ssh': 22,             # Secure Shell
    'telnet': 23,          # Plaintext Remote Terminal
    'winrm': 5985,         # Windows Remote Management (HTTP)
    'winrm-https': 5986,   # Windows Remote Management (HTTPS)
    'rdp': 3389,           # Remote Desktop Protocol
    'vnc': 5900,           # Virtual Network Computing
    'psexec': 445,         # SMB-based execution (maps to SMB port)

    'mysql': 3306,         # MySQL / MariaDB
    'postgresql': 5432,    # PostgreSQL
    'mssql': 1433,         # Microsoft SQL Server
    'oracle': 1521,        # Oracle Database (TNS Listener)

    'redis': 6379,         # Redis (often has auth enabled)
    'mongodb': 27017,      # MongoDB

    'ftp': 21,             # File Transfer Protocol
    'smb': 445,            # Server Message Block
    'ldap': 389,           # Lightweight Directory Access Protocol
    'ldaps': 636,          # LDAP over SSL/TLS

    'smtp': 25,            # Simple Mail Transfer Protocol
    'pop3': 110,           # Post Office Protocol
    'imap': 143            # Internet Message Access Protocol
}


def resolve_service_to_ports(services: list[str], ports: list[int] | None) -> list[int]:
    """Map each service to its custom port or its standard default port."""
    unknown_services = [service for service in services if service not in SERVICE_DEFAULTS]
    if unknown_services:
        unknown = ", ".join(unknown_services)
        raise ValueError(f"Unknown service(s): {unknown}")

    custom_ports = ports or []
    return [
        custom_ports[index] if index < len(custom_ports) else SERVICE_DEFAULTS[service]
        for index, service in enumerate(services)
    ]

