"""Publish the SG Forester vented headlight caps to Thingiverse via the developer API.

Usage:
    py -3 publish_thing.py --token <USER_TOKEN> --dry-run   # verify token, show plan
    py -3 publish_thing.py --token <USER_TOKEN>             # create draft + upload everything
    py -3 publish_thing.py --token <USER_TOKEN> --publish   # ...and publish it live

The token is a USER OAuth token obtained via the browser implicit flow — see
get_token.py in sgForesterFogLight/thingiverse/. (The read-only "App Token" shown
on the app page cannot publish.) Requires: pip install requests

API contract (verified live against api.thingiverse.com): Bearer auth; file upload
is a three-step dance — POST /things/<id>/files {filename} -> multipart POST the
returned S3 action+fields WITHOUT following redirects (the storage endpoint answers
200 {"ok":"ok"}) -> POST fields.success_action_redirect with Bearer auth to
finalize. Images uploaded this way become the gallery; the first becomes the cover.
The API accepts a category on create but silently ignores it — set "Automotive" in
the web UI after publishing.
"""
import argparse, os, sys, time
import requests

API = 'https://api.thingiverse.com'
HERE = os.path.dirname(os.path.abspath(__file__))
PROJ = os.path.dirname(HERE)

TITLE = 'Vented Headlight Bulb Caps for LED Bulbs - 2006-2008 Subaru Forester (SG)'
LICENSE = 'cc-nc-sa'          # Creative Commons - Attribution - Non-Commercial - Share Alike
CATEGORY = 'Automotive'
TAGS = ['subaru', 'forester', 'sg', 'fxt', 'headlight', 'led', 'bulb_cap',
        'vented', 'louver', 'asa', 'automotive', 'car_mod']

FILES = [
    'models/stl/headlight_cap.stl',
    'models/3mf/cap_pair_ASA.3mf',
]
IMAGES = [  # first upload becomes the cover
    'gallery/cap_installed_closeup.jpg',
    'gallery/cap_product.png',
    'gallery/cap_oring_fan.jpg',
    'gallery/cap_installed_wide.jpg',
]

def description_text():
    """The listing body = everything after the divider in description.md."""
    with open(os.path.join(HERE, 'description.md'), encoding='utf-8') as f:
        text = f.read()
    marker = '## Description'
    body = text.split(marker, 1)[1]
    return body.split('\n', 1)[1].strip()

def die(msg, res=None):
    print(f'ERROR: {msg}')
    if res is not None:
        print(f'  status: {res.status_code}')
        print(f'  x-error: {res.headers.get("x-error")}')
        print(f'  body: {res.text[:2000]}')
    sys.exit(1)

def req(session, method, url, expect=(200, 201, 202), **kw):
    if url.startswith('/'):
        url = API + url
    res = session.request(method, url, timeout=120, **kw)
    if res.status_code not in expect:
        die(f'{method} {url} failed', res)
    return res

def upload(session, thing_id, path):
    name = os.path.basename(path)
    size_kb = os.path.getsize(path) // 1024
    print(f'  uploading {name} ({size_kb} KB) ... ', end='', flush=True)
    r = req(session, 'POST', f'/things/{thing_id}/files', json={'filename': name})
    info = r.json()
    action, fields = info['action'], info['fields']
    finalize = fields.get('success_action_redirect')
    with open(path, 'rb') as f:
        up = requests.post(action, data=fields, files={'file': (name, f)},
                           allow_redirects=False, timeout=900)
    if up.status_code not in (200, 201, 204, 303):
        die(f'storage upload of {name} failed', up)
    finalize = up.headers.get('Location') or finalize
    if not finalize:
        die(f'no finalize URL for {name}', up)
    req(session, 'POST', finalize)
    print('done')

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--token', default=os.environ.get('THINGIVERSE_TOKEN'))
    ap.add_argument('--dry-run', action='store_true')
    ap.add_argument('--publish', action='store_true')
    ap.add_argument('--thing-id', help='upload into an existing draft instead of creating one')
    args = ap.parse_args()
    if not args.token:
        die('no token (use --token or THINGIVERSE_TOKEN)')

    s = requests.Session()
    s.headers.update({'Authorization': f'Bearer {args.token}',
                      'Accept': 'application/json'})

    me = req(s, 'GET', '/users/me').json()
    print(f'Authenticated as: {me.get("name")} ({me.get("public_url")})')
    if me.get('name', '').lower() != 'smithtronic':
        print('  WARNING: expected account SMITHtRONiC — continuing anyway')

    desc = description_text()
    missing = [p for p in FILES + IMAGES if not os.path.exists(os.path.join(PROJ, p))]
    print(f'Plan: create "{TITLE}"')
    print(f'  license={LICENSE}  category={CATEGORY}  tags={",".join(TAGS)}')
    print(f'  {len(FILES)} files, {len(IMAGES)} images, description {len(desc)} chars')
    for p in missing:
        print(f'  MISSING: {p}')
    if missing:
        die('missing inputs')
    if args.dry_run:
        print('Dry run complete — token valid, no thing created.')
        return

    if args.thing_id:
        thing = req(s, 'GET', f'/things/{args.thing_id}').json()
        thing_id = thing['id']
        existing = {f['name'] for f in req(s, 'GET', f'/things/{thing_id}/files').json()}
        print(f'Using existing thing {thing_id}: {thing.get("public_url")}')
        if existing:
            print(f'  already uploaded ({len(existing)}): {", ".join(sorted(existing))}')
    else:
        r = req(s, 'POST', '/things/', json={
            'name': TITLE, 'license': LICENSE, 'category': CATEGORY,
            'description': desc, 'tags': TAGS, 'is_wip': False,
        })
        thing = r.json()
        thing_id = thing['id']
        existing = set()
        print(f'Created thing {thing_id}: {thing.get("public_url")}')

    for rel in IMAGES + FILES:
        p = os.path.join(PROJ, rel)
        if os.path.basename(p) in existing:
            print(f'  already present, skipping {os.path.basename(p)}')
            continue
        upload(s, thing_id, p)
        time.sleep(1)

    if args.publish:
        req(s, 'POST', f'/things/{thing_id}/publish')
        print('PUBLISHED.')
    else:
        print('Draft complete (not published). Re-run with --publish, or hit '
              'Publish on the thing page.')
    print(f'Thing URL: {thing.get("public_url")}')

if __name__ == '__main__':
    main()
