# Privacy notice

Updated November 6, 2026.

## Purpose and scope

This is a privately operated, single-user integration for reading the operator's own Oura data in their personal ChatGPT account. It is independent of any health dashboard. This repository contains public documentation only. It is not a public health-data service and is not operated or endorsed by Oura or OpenAI.

## Data flow

When configured and authorized, a local instance of the open-source proscar87/oura-mcp service retrieves requested information from the Oura API. An OpenAI Secure MCP Tunnel delivers tool requests and responses between that local service and ChatGPT. Information returned by a tool is therefore disclosed to OpenAI for use in ChatGPT. The requested scopes may include account information, sleep, activity, readiness, heart rate, workouts, sessions, tags, blood oxygen, stress, heart health and ring configuration. Available records depend on Oura permissions and API availability.

## Credentials and storage

Oura credentials and tunnel credentials belong in local protected configuration or a credential store, never in this repository, public documents, chat messages, or committed files. The selected MCP project's documentation describes in-memory health-data caching and local OAuth token storage. Those upstream statements are not an independent security audit. Local diagnostics must avoid recording tokens or health records. ChatGPT conversations and provider logs may retain data according to account settings and the relevant providers' policies; this integration does not promise that no data is retained outside the local process.

## Recipients and controls

Oura supplies the authorized data; OpenAI receives requested tool responses through the tunnel and ChatGPT. GitHub hosts this documentation and is not an intended recipient of health records or credentials. No additional analytics, advertising, or resale service is part of this integration's design. Adding another processor requires revising this notice before use.

The operator can stop the local service or tunnel, disconnect the ChatGPT app, and revoke Oura authorization. Revocation stops future access but does not delete information already included in ChatGPT conversations. Manage or delete those conversations using ChatGPT's account controls, and remove local credentials separately.

## Provider policies and contact

Oura: https://ouraring.com/privacy-policy

OpenAI: https://openai.com/policies/privacy-policy/

Source project: https://github.com/proscar87/oura-mcp

For documentation corrections, use this repository's issues. Do not post health records, credentials, account identifiers, or other private information in public issues.
