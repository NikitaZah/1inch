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

    def address(self, address: str, **kwargs) -> list:
        """
        :param address: address (str) \\ Address of limit orders creator
        :param kwargs: {
                        'page': int, \\ Pagination step, default: 1 (page = offset / limit),
                        'limit': int, \\ Number of limit orders to receive (default: 100, max: 500)
                        'statuses': list[int], \\ JSON an array of statuses by which limit orders will be
                        filtered: 1 - valid limit orders, 2 - temporary invalid limit orders, 3 - invalid limit orders
                        'sortBy': str, \\ 'createDateTime', 'takerRate', 'makerRate', 'makerAmount' or 'takerAmount'
                        'takerAsset': address (str), \\ Address of the taker asset
                        'makerAsset': address (str), \\ Address of the maker asset

        :return: Array of queried limit orders
        """
        return self._get(f'address/{address}', **kwargs)

    def all(self, **kwargs) -> list:
        """
        :param kwargs: {
                        'page': int, \\ Pagination step, default: 1 (page = offset / limit),
                        'limit': int, \\ Number of limit orders to receive (default: 100, max: 500)
                        'statuses': list[int], \\ JSON an array of statuses by which limit orders will be
                        filtered: 1 - valid limit orders, 2 - temporary invalid limit orders, 3 - invalid limit orders
                        'sortBy': str, \\ 'createDateTime', 'takerRate', 'makerRate', 'makerAmount' or 'takerAmount'
                        'takerAsset': address (str), \\ Address of the taker asset
                        'makerAsset': address (str), \\ Address of the maker asset
        :return: Array of queried limit orders
        """
        return self._get('all', **kwargs)

    def count(self, statuses: list[int]) -> int:
        """
        :param statuses: orders statuses
        :return: amount of orders
        """

        params = {
            'statuses': statuses
        }

        return self._get('all', **params)

    def events(self, order_hash: Optional[str] = None, limit: Optional[int] = None) -> list[dict]:
        """
        :param order_hash: order hash (str)
        :param limit: limit (int)
        :return: dict = {
                        'id': int,
                        'network': int,
                        'logId': str,
                        'version': int,
                        'action': str,
                        'orderHash': str,
                        'taker': str,
                        'remainingMakerAmount': str,
                        'transactionHash': str,
                        'blockNumber': int,
                        'createDateTime': str
                        }
        """
        if order_hash:
            return self._get(f'events/{order_hash}')

        elif limit:
            params = {
                'limit': limit
            }
            return self._get('events', **params)
