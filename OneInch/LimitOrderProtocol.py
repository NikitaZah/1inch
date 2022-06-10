from requests import Session
from typing import Optional

from .AbstractProtocol import AbstractProtocol


class LimitOrderProtocol(AbstractProtocol):
    _version = 2.0
    _API_URL = 'https://limit-orders.1inch.io'

    def __init__(self, session: Session, chain_id: int):
        super(LimitOrderProtocol, self).__init__(session, chain_id)
        self._base_url += 'limit-order/'

    def post(self):
        pass

    def address(self, address: str, **kwargs):
        return self._get(f'address/{address}', **kwargs)

    def all(self, **kwargs):
        return self._get('all', **kwargs)

    def count(self, statuses: list[str]):

        params = {
            'statuses': statuses
        }

        return self._get('all', **params)

    def events(self, order_hash: Optional[str] = None, limit: Optional[int] = None):
        if order_hash:
            return self._get(f'events/{order_hash}')

        elif limit:
            params = {
                'limit': limit
            }
            return self._get('events', **params)
