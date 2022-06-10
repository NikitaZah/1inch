from requests import Session


class AbstractProtocol:
    _version: float
    _API_URL: str

    def __init__(self, session: Session, chain_id: int):
        self._session = session
        self._base_url = f'{self._API_URL}/v{str(self._version)}/{chain_id}/'

    def _get(self, endpoint: str, **params):
        with self._session as s:
            response = s.get(self._base_url + endpoint, params=params)
            return response.json()

    def _post(self, endpoint: str, **params):
        with self._session as s:
            response = s.post(self._base_url + endpoint, params=params)
            return response.json()
