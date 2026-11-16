# Oura for ChatGPT

## Project Description

A personal integration that makes authorized Oura data available to a compatible MCP client, including the owner's ChatGPT connection. A small Python adapter configures the existing `mcp-oura` server with separate local credential storage.

The project is independent of CX83 Fit. This repository contains the adapter and public documentation; it does not contain the upstream MCP server, account credentials, or personal health records.

## Contents

* [Usage](#usage)
* [Installation](#installation)
* [How It Works](#how-it-works)
* [Tech Stack](#tech-stack)
* [Verification and Limits](#verification-and-limits)
* [Author and Credits](#author-and-credits)

## Usage

The adapter has three commands:

* `authorize`: load or create the local application configuration and run the upstream Oura authorization flow.
* `check`: run the upstream connection check.
* `serve`: start the upstream MCP service for a configured client.

Once the service and client connection are configured, example requests include:

* List the available Oura collections.
* Retrieve sleep information for a specific date range.
* Compare activity across two date ranges.

The records returned depend on Oura authorization and data availability. These examples are client requests, not additional command line options implemented by this adapter.

## Installation

### Prerequisites

* Git and Python 3.10 or newer on macOS or Linux.
* An Oura account and an application registered for your own use.
* The registered redirect `http://localhost:9876/callback/`.
* A compatible MCP client. The documented ChatGPT installation additionally uses a separately configured Secure MCP Tunnel.

The adapter uses POSIX ownership and permission checks such as `os.getuid()`; native Windows support is not implemented.

### Set up the adapter

```bash
git clone https://github.com/Mike-CX83/oura-chatgpt-connection.git
cd oura-chatgpt-connection
python3 -m venv .venv
source .venv/bin/activate
python -m pip install mcp-oura==0.4.0
```

The version is pinned because the adapter imports functions from that package's implementation. An upstream upgrade needs a compatibility review.

### Authorize and check

```bash
python oura_local.py authorize
python oura_local.py check
```

On first authorization, enter your own client ID and secret at the prompts, then complete the consent flow. The secret prompt is hidden.

The adapter uses these paths outside the checkout:

* `~/.local/share/oura-chatgpt/application.json`: application credentials.
* `~/.local/share/oura-chatgpt/tokens.json`: token location passed to the upstream server.

If configuration already exists, the adapter loads it instead of prompting for replacement credentials. Do not overwrite an existing working installation.

### Start the service

```bash
python oura_local.py serve
```

Starting the process does not register a ChatGPT app or create a tunnel. Attach it through your compatible client's configuration. The previously documented owner installation uses tunnel alias `oura`; that is an installation detail, not an alias created by this repository.

## How It Works

`oura_local.py` performs four jobs:

1. Checks ownership and permissions for its application configuration, refusing symbolic links at the configured directory and application file.
2. Sets Oura environment variables and a dedicated token path while clearing conflicting client settings.
3. Adjusts the upstream authorization URL and requests its blank scope behavior.
4. Delegates authorization, checking, and serving to `oura_mcp`.

The application directory is set to mode `700`, and `application.json` must have mode `600`. Token handling and API collection behavior are implemented upstream.

Oura supplies authorized records. The MCP client receives tool responses. In the documented ChatGPT setup, those responses pass through the configured OpenAI tunnel into ChatGPT; they do not automatically become CX83 Fit records.

## Tech Stack

* Python standard library for configuration and command handling.
* `mcp-oura==0.4.0` for Oura and MCP behavior.
* Oura OAuth and API access.
* A separately configured MCP client and, for the documented ChatGPT setup, Secure MCP Tunnel.

## Verification and Limits

This repository has no checked-in automated test suite. `check` is a live upstream diagnostic, so run it only with your own authorized account. Its output should not be pasted into public issues.

Earlier setup observations are retained in the [historical checkpoint](docs/README_CHECKPOINT_2026_11_16.md). They do not prove that a service is running now, that every collection has data, or that restart and token refresh work in a new installation.

This documentation review inspected the complete adapter. It did not reauthorize Oura, query health records, or change the running connection.

[Privacy notice](PRIVACY.md) · [Terms of use](TERMS.md)

## Author and Credits

**Mike Hankins**, CX83 Labs. Local integration, configuration adapter, and documentation.

[GitHub](https://github.com/Mike-CX83)

The upstream MCP server is [oura-mcp by Oscar Pacheco](https://github.com/proscar87/oura-mcp). This project adapts that server rather than implementing a separate Oura API service.
