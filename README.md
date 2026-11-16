# Oura for ChatGPT

## Table of Contents

* [Project Description](#project-description)
* [Installation](#installation)
* [Usage / How It Works](#usage-/-how-it-works)
* [Tech Stack](#tech-stack)
* [Verified setup status](#verified-setup-status)
* [Components](#components)
* [Local operation](#local-operation)
* [Registration documentation](#registration-documentation)
* [Author and Credits](#author-and-credits)

## Project Description

A privately operated Oura MCP connection to personal ChatGPT through an OpenAI Secure MCP Tunnel. It is independent of any dashboard application.

This public repository contains documentation and a small configuration adapter only. Credentials, health records, tunnel IDs and private runtime configuration must never be committed here.

## Installation

This adapter targets a local macOS or Linux environment with Python 3.10 or newer, Git, an Oura account, and your own registered Oura application.

For a new checkout:

```bash
git clone https://github.com/Mike-CX83/oura-chatgpt-connection.git
cd oura-chatgpt-connection
python3 -m venv .venv
source .venv/bin/activate
python -m pip install mcp-oura==0.4.0
```

Version 0.4.0 is pinned to match the adapter's documented integration. The upstream server is a separate dependency and is not included in this repository.

Register `http://localhost:9876/callback/` as the redirect for your own Oura application. Then authorize:

```bash
python oura_local.py authorize
```

Enter your own client ID and client secret when prompted, and complete the consent flow. The adapter stores application credentials and tokens outside the checkout under `~/.local/share/oura-chatgpt`.

The existing installation described below already has a dedicated environment and tunnel. Use that installation's environment for normal operation.

## Usage / How It Works

From the checkout with its Python environment active:

```bash
python oura_local.py check
python oura_local.py serve
```

`check` runs the upstream connection check. `serve` starts the upstream MCP service for a compatible client. It does not open a website or automatically connect ChatGPT.

The adapter loads local application credentials, configures separate token storage, and delegates authorization and MCP requests to `mcp-oura`. A ChatGPT connection additionally requires the separately configured Secure MCP Tunnel described in Local operation.

Example requests after connecting a compatible client:

* List the available Oura data collections.
* Retrieve sleep data for an explicit date range.
* Compare activity across two date ranges.

Available records depend on the account and authorized collections.

## Tech Stack

* Python for the configuration adapter.
* The upstream `mcp-oura` package for the MCP service.
* Oura OAuth and API access.
* OpenAI Secure MCP Tunnel for this installation's ChatGPT transport.

## Verified setup status

As of November 6, 2026:

- The Oura application was registered and authorized for all eleven selected data categories.
- Application credentials and OAuth tokens were saved in separate local files with owner-only permissions.
- `mcp-oura==0.4.0` was installed in an isolated environment. Version 0.4.1 existed in the source tree but was not published on PyPI when installation was attempted.
- The synthetic API check succeeded.
- A local MCP initialization and tool-discovery test succeeded with installed MCP SDK 2.3.0.
- Six tools were discovered: `oura_collections`, `oura_query`, `oura_today`, `oura_compare`, `oura_relate`, and `oura_check`.
- A separate OpenAI tunnel was created in the browser and attached with the existing runtime credential. The operator's Terminal reported the Oura runtime ready.
- Oura Personal was added to personal ChatGPT. A separate ChatGPT test conversation reported a successful authenticated API check and completed bounded sleep queries. Health results are intentionally excluded from this public repository.

Limits: this is not an independent security audit. Automatic token refresh is implemented upstream but has not been exercised through a real expiration/refresh cycle in this setup. Startup after a Mac reboot has not been verified. Successful API connectivity does not prove that every data collection contains records or that all historical data is available.

## Components

- Oura API and account-owner OAuth consent.
- Local [proscar87/oura-mcp](https://github.com/proscar87/oura-mcp), PyPI distribution `mcp-oura` version 0.4.0.
- `oura_local.py`, a small adapter for separate local credential storage and authorization requesting all available scopes using Oura's documented blank-scope behavior. It uses Oura's documented developer authorization URL and reuses the package's callback, state verification and token exchange.
- OpenAI Secure MCP Tunnel connecting the local service to personal ChatGPT.

The adapter passed offline checks for credential file and directory permissions, configuration reload, environment isolation, scope handling, redirect URL and rejection of a mismatched OAuth state. Tests used synthetic credentials only.

## Local operation

The selected runtime location is `~/.local/share/oura-chatgpt`. It contains the isolated virtual environment, adapter, protected application and token files, and dedicated tunnel profile. The tunnel alias is `oura`.

Inspect runtime status with `tunnel-client runtimes status oura`. The local computer must remain awake, online and running the service for ChatGPT calls to succeed. Reuse the existing alias and tunnel when restarting; do not recreate the application or disturb unrelated connections.

The browser-created ChatGPT connection uses Tunnel mode without an additional MCP OAuth layer. OpenAI tunnel access controls protect the transport, and separately stored Oura OAuth credentials authorize upstream reads. This is not a publicly exposed unauthenticated HTTP endpoint.

## Registration documentation

[Privacy notice](PRIVACY.md)

[Terms of use](TERMS.md)

The local redirect registered for this implementation is `http://localhost:9876/callback/`.

Do not post account identifiers, credentials, health records or private logs in public issues.

## Author and Credits

**Mike Hankins**  
Local integration, configuration adapter, and project documentation.

[GitHub profile](https://github.com/Mike-CX83)

The upstream MCP server is [oura-mcp by Oscar Pacheco](https://github.com/proscar87/oura-mcp). This repository adapts its configuration and authorization flow; it does not implement a separate Oura API server.
