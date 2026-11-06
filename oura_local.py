"""Private configuration adapter for mcp-oura 0.4.0; no custom MCP server."""
import argparse
import asyncio
import functools
import getpass
import json
import os
from pathlib import Path
import stat
import sys

ROOT = Path.home() / '.local/share/oura-chatgpt'
APP = ROOT / 'application.json'


def prepare_environment(config):
    # Isolate this connection from other Oura clients and shell configuration.
    for name in ('OURA_SANDBOX', 'OURA_PAT', 'OURA_PAT_FILE',
                 'OURA_API_BASE_URL', 'XDG_CONFIG_HOME'):
        os.environ.pop(name, None)
    os.environ['OURA_CLIENT_ID'] = config['client_id']
    os.environ['OURA_CLIENT_SECRET'] = config['client_secret']
    os.environ['OURA_CREDENTIALS'] = str(ROOT / 'tokens.json')
    os.environ['OURA_NO_KEYCHAIN'] = '1'


def configure_authorization(module):
    # Official Oura documentation: a blank scope requests all available scopes.
    # Reuse upstream state verification, callback handling and token exchange.
    module.AUTORIZAR_URL = 'https://developer.ouraring.com/authorize'
    module.authorization_url = functools.partial(module.authorization_url, scopes=())


def load_application(create=False):
    if ROOT.is_symlink() or APP.is_symlink():
        raise RuntimeError('Refusing symbolic links for credential storage.')
    ROOT.mkdir(mode=0o700, parents=True, exist_ok=True)
    if ROOT.stat().st_uid != os.getuid():
        raise RuntimeError('The Oura directory is not owned by this user.')
    ROOT.chmod(0o700)
    if APP.exists():
        info = APP.stat()
        if info.st_uid != os.getuid() or stat.S_IMODE(info.st_mode) != 0o600:
            raise RuntimeError('application.json must be owned by you with permissions 600.')
        config = json.loads(APP.read_text())
    elif create:
        config = {
            'client_id': input('Paste the Oura Client ID, then press Return: ').strip(),
            'client_secret': getpass.getpass('Paste the Oura Client Secret (hidden), then press Return: ').strip(),
        }
        if not all(config.values()):
            raise RuntimeError('Both values are required. Nothing was saved.')
        fd = os.open(APP, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
        with os.fdopen(fd, 'w') as handle:
            json.dump(config, handle)
    else:
        raise RuntimeError('Authorize this connection first.')
    if not all(isinstance(config.get(k), str) and config[k].strip()
               for k in ('client_id', 'client_secret')):
        raise RuntimeError('The local application configuration is incomplete.')
    return config


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('action', choices=('authorize', 'check', 'serve'))
    action = parser.parse_args().action
    config = load_application(create=action == 'authorize')
    prepare_environment(config)
    if action == 'authorize':
        from oura_mcp import authorize
        configure_authorization(authorize)
        result = authorize.authorize()
        print(json.dumps(result, indent=2))
    elif action == 'check':
        from oura_mcp.server import check
        print(json.dumps(check(), indent=2))
    else:
        from oura_mcp.server import main as serve
        asyncio.run(serve())


if __name__ == '__main__':
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print('Setup stopped.', file=sys.stderr)
        sys.exit(1)
    except Exception as error:
        # Do not expose upstream HTTP bodies, authorization codes or credentials.
        if isinstance(error, RuntimeError):
            print(str(error), file=sys.stderr)
        else:
            print(f'Setup did not complete ({type(error).__name__}). Keep the browser page open for diagnosis.', file=sys.stderr)
        sys.exit(1)
