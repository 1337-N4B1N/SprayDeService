**PROBLEM STATEMENT**
- So when doing ctfs, we often find credentials but we need to check it on every service.
- This is kind of time consuming as well as boring because we need to use different tools for each.SSH FTP psexec, mysql and syntax of everything is just different.
- So what this tool tries to do is get username and password and try it on all common services.So we just need to remember one syntax now.

**Kind of algroithm how this works**
-  so the tool name is spraydeservice.
- The user must put three things, username password and target(Here target can be just ip address or domain-name like google.com)
- If  domain-name is given, we first resolve it to ip.For this we will use file resolve-domain.py and create fxn domain_to_ip()
- If Ip is given no issue.
- -H or --host will take target.
- -u or --username will take username
- -p or --password will take password.
- We will map different common services and their default ports name.
- We will try these credentials on all of them.
- We also see that some ports run on different ports like sometimes ssh on 2000 etc.
So to tackle this we will give --port feature too where they can list the port. To list a custom port, the user must also list the service with --service or -s.
- The user may provide more than one service and port, for example: -s ssh,smb --port 2000,20001.
- Ports are mapped by position: the first port is used for the first service, the second port for the second service, and so on.
- If fewer ports than services are provided, services without a custom port use their default port. Extra ports without a matching service are ignored or rejected by argument validation.
- For example, -s ssh,smb --port 2000 maps SSH to port 2000 and SMB to its default port 445.
- The CLI output must report the result separately for each service, including whether the credentials were accepted.
- Connection timeout, connection refusal, unavailable service, and other network errors must be reported separately from invalid credentials.

**Future plans**
- Add a `--shell <service_name>` option so the user can open a shell through a service after finding valid credentials for it.
- Keep authentication checks and shell sessions as separate service operations, so adding shell access does not require redesigning the credential-checking flow.
- Add support for multiple targets later. The first version will support one target only.

**Current scope**
- The current implementation will not include the `--shell` option.
- The current implementation will support one target only; multiple hosts are out of scope.
- The current implementation will focus only on checking credentials and printing per-service results in the CLI.

- 