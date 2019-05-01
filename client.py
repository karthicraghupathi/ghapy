import requests

class GitHub(object):
    _api_url = 'https://api.github.com'
    _s = None

    def __init__(self, token):
        self._s = requests.Session()
        self._s.headers.update({
            'Accept': 'application/vnd.github.v3+json',
            'Authorization': 'token {}'.format(token),
            'User-Agent': 'https://github.com/karthicraghupathi/ghapy'
        })
        print(self._s.headers)
    
    def _get_api_url(self, path=''):
        return f'{self._api_url}{path}'

    def get_repos(self, **kwargs):
        """GET /user/repos"""
        api_url = self._get_api_url('/user/repos')
        if kwargs:
            r = self._s.get(api_url, params=kwargs)
        else:
            r = self._s.get(api_url)
        r.raise_for_status()
        return r.json()

    def get_repo(self, owner, repo):
        """GET /repos/:owner/:repo"""
        api_url = self._get_api_url('/repos/{}/{}'.format(owner, repo))
        r = self._s.get(api_url)
        r.raise_for_status()
        return r.json()

    def star_repo(self, owner, repo):
        """PUT /user/starred/:owner/:repo"""
        # Also set Content-Length to 0
        api_url = self._get_api_url('/user/starred/{}/{}'.format(owner, repo))
        r = self._s.put(api_url, headers={'Content-Length': '0'})
        r.raise_for_status()

    def delete_repo(self, owner, repo):
        """DELETE /repos/:owner/:repo"""
        api_url = self._get_api_url('/repos/{}/{}'.format(owner, repo))
        r = self._s.delete(api_url)
        r.raise_for_status()
