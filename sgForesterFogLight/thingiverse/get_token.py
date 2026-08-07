"""Thingiverse OAuth helper (implicit flow — no client secret needed).

Thingiverse has no non-browser auth flow, so getting a token is a two-step dance:

    1) py -3 get_token.py url  <CLIENT_ID>
       Prints the authorization URL. Open it in a browser where you are logged in
       as SMITHtRONiC and click Authorize.

    2) You land on your callback URL with "#access_token=..." in the address bar.
       Copy the WHOLE address and run:

       py -3 get_token.py token "<pasted-url>"

       This extracts the token, verifies it against /users/me, and prints the
       token so it can be passed to publish_thing.py.

The token is password-equivalent: it can act on your Thingiverse account. Don't
commit it, and delete the app at thingiverse.com/apps when you're done publishing.
"""
import sys
import urllib.parse
import requests

AUTH = 'https://www.thingiverse.com/login/oauth/authorize'
API = 'https://api.thingiverse.com'


def build_url(client_id, redirect_uri=None):
    params = {'client_id': client_id, 'response_type': 'token'}
    if redirect_uri:
        params['redirect_uri'] = redirect_uri
    return AUTH + '?' + urllib.parse.urlencode(params)


def extract_token(pasted):
    pasted = pasted.strip().strip('"').strip("'")
    if 'access_token=' not in pasted:
        return None
    # the token arrives in the URL fragment, e.g. https://site/#access_token=abc&token_type=bearer
    frag = pasted.split('access_token=', 1)[1]
    return frag.split('&')[0].split('#')[0].strip()


def verify(token):
    r = requests.get(f'{API}/users/me',
                     headers={'Authorization': f'Bearer {token}'}, timeout=45)
    if r.status_code != 200:
        print(f'  token REJECTED (HTTP {r.status_code}): {r.text[:200]}')
        return False
    me = r.json()
    print(f'  token OK — authenticated as: {me.get("name")}  ({me.get("public_url", "")})')
    return True


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        return
    mode, arg = sys.argv[1], sys.argv[2]
    if mode == 'url':
        redirect = sys.argv[3] if len(sys.argv) > 3 else None
        print('\nOpen this in your browser (logged in as SMITHtRONiC):\n')
        print('  ' + build_url(arg, redirect) + '\n')
        print('Click Authorize. You will be redirected to your callback URL with')
        print('"#access_token=..." in the address bar — copy the whole address.\n')
    elif mode == 'token':
        tok = extract_token(arg)
        if not tok:
            print('Could not find access_token= in that text.')
            print('Paste the FULL address bar contents after authorizing.')
            return
        print(f'\naccess token: {tok}\n')
        if verify(tok):
            print('\nNext:')
            print(f'  py -3 publish_thing.py --token {tok} --dry-run')
    else:
        print(__doc__)


if __name__ == '__main__':
    main()
