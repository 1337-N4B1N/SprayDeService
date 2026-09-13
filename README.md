## spraydeservice
*Note: Use the `continue` branch as its latest as of now.*

### How to use

### Installation

From the project directory, install the tool with uv:

```bash
uv tool install . --force
```

After installation, use the `spraydeservice` command from any directory.

### Command-line usage

The basic syntax is:

```bash
spraydeservice -u <username> -p <password> -H <host>
```

When no service is specified, the command checks every service in the default
service list. Implemented services are checked against their default ports;
services that are not implemented yet are reported as `not implemented`.

For example:

```bash
spraydeservice -u alice -p password -H 192.168.1.10
```

To select specific services, use `-s` or `--service` with a comma-separated
list:

```bash
spraydeservice -u alice -p password -H 192.168.1.10 -s ssh,ftp,smb
```

Custom ports are mapped positionally to the selected services. Services after
the supplied ports use their default ports:

```bash
spraydeservice -u alice -p password -H 192.168.1.10 \
  -s ssh,ftp,smb --port 2000,2121
```

This checks SSH on port `2000`, FTP on port `2121`, and SMB on its default port
`445`.

Press `Ctrl+C` once to cancel a running scan and exit.

### Problem Statement

During a CTF, valid credentials often need to be tested against several
services on the same target. SSH, FTP, SMB, and MySQL each require different
commands and tools, which makes this process repetitive and easy to get wrong.

### What this project solves

`spraydeservice` provides one CLI for checking a username and password against
common network services. The user supplies one target, which may be an IP
address or a hostname, together with the credentials to test. Hostnames are
resolved before the service checks run.

The tool reports the result separately for every service. Valid credentials,
invalid credentials, timeouts, unavailable services, and other connection
errors remain distinguishable in the CLI output.

### Current scope

- One target per command.
- Credential checking only; no shell access yet.
- Supported service definitions currently include SSH, FTP, SMB, and MySQL.
- Default ports are used unless custom ports are supplied.
- Custom ports map positionally to the services listed with `--service`.
- Services without a custom port use their default port.

Example:

```bash
spraydeservice -H 192.168.1.10 -u alice -p password -s ssh,smb --port 2000
```

This maps SSH to port `2000` and SMB to its default port `445`.

### Future plans

- Add `--shell <service_name>` to open a shell through a service after valid
  credentials are found.
- Add support for checking multiple targets in one command.
