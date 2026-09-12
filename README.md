## spraydeservice

### Problem

During a CTF, valid credentials often need to be tested against several
services on the same target. SSH, FTP, SMB, and MySQL each require different
commands and tools, which makes this process repetitive and easy to get wrong.
### Problem

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
