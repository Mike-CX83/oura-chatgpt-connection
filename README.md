# Oura for ChatGPT

Documentation for a privately operated, single-user Oura MCP connection to personal ChatGPT through an OpenAI Secure MCP Tunnel, independent of any dashboard.

This public repository contains documentation only, never credentials or health records.

## Status

Oura application registration was verified complete on November 6, 2026. Runtime installation, OAuth authorization, a separate Oura tunnel, ChatGPT registration and a live tool read remain incomplete. The application creation screen is not proof of data access. Existing unrelated connections remain unchanged.

The current automation shell cannot download packages or open a local listener. The operator must perform local installation in their own Terminal unless an authorized execution environment becomes available.

## Components

Selected for evaluation: [proscar87/oura-mcp](https://github.com/proscar87/oura-mcp), distribution `mcp-oura`, source version `0.4.1`. PyPI availability of that version has not yet been verified from the installation environment.

The planned route is Oura API to a local MCP service, then an OpenAI Secure MCP Tunnel to personal ChatGPT. No dashboard dependency.

Selection does not constitute an independent security audit. Check the installed artifact, verify synthetic mode, and verify authorization and token refresh before claiming the connection works. Source review found that the OAuth scope list contains eight legacy scopes, while the registration portal exposes eleven categories; reconcile and test scope coverage before claiming all categories are accessible. The new-portal token fallback is explicitly not live-verified by the source project's own comments.

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
