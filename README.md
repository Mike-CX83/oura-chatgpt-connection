# Oura for ChatGPT

Documentation for a privately operated, single-user Oura MCP connection to personal ChatGPT through an OpenAI Secure MCP Tunnel, independent of any dashboard.

This public repository contains documentation only, never credentials or health records.

## Status

Setup is in progress. The local MCP runtime and dedicated Oura tunnel are not yet configured or tested. No live ChatGPT data read has been verified. Existing unrelated connections remain unchanged.

## Components

Oura API supplies authorized data to a local instance of [proscar87/oura-mcp](https://github.com/proscar87/oura-mcp), packaged as `mcp-oura`. A separate OpenAI Secure MCP Tunnel carries requests and responses between this service and personal ChatGPT.

The implementation is selected for evaluation, not independently security-audited. Inspect and pin the installed version, verify with synthetic data, then authorize Oura and verify a minimal live read.

## Registration

Display name: Oura for ChatGPT

Website: https://github.com/Mike-CX83/oura-chatgpt-connection

Privacy: https://github.com/Mike-CX83/oura-chatgpt-connection/blob/main/PRIVACY.md

Terms: https://github.com/Mike-CX83/oura-chatgpt-connection/blob/main/TERMS.md

Callback for this implementation: `http://localhost:9876/callback/`

## Documents

[Privacy notice](PRIVACY.md)

[Terms of use](TERMS.md)

Do not post private information in public issues.
