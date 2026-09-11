## spraydeservice

CLI tool for checking one username and password against common services on one
target. The current implementation scope is credential checking only; shell
access and multiple targets are future features.

### Structure

```text
src/spraydeservice/
├── __main__.py          # Installed CLI entry point
├── cli.py               # Argument parsing and CLI orchestration
├── targets.py           # IP validation and hostname resolution
├── results.py           # Normalized per-service result types
└── services/
	├── base.py          # Service checker interface
	└── registry.py      # Supported services and default ports
```

Service-specific authentication code belongs in `services/`. Each checker
should return a `ServiceResult` so invalid credentials, timeouts, unavailable
services, and other connection errors remain distinguishable.
