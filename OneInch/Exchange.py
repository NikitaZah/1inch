import requests
from .AggregationProtocol import AggregationProtocol
from .LimitOrderProtocol import LimitOrderProtocol


ETHEREUM = 1
BINANCE = 56
POLYGON = 137
OPTIMISM = 10
ARBITRUM = 42161
GNOSIS = 100
AVALANCHE = 43114


class Exchange:

    def __init__(self, network: str):
        """
        :param network: 'ethereum', 'binance', 'polygon', 'optimism', 'arbitrum', 'gnosis' or 'avalanche'
        """
        self._session = requests.Session()
        self._network = network.lower()
        try:
            self._chain_id = globals()[self._network.upper()]
        except KeyError:
            raise KeyError(f'You have chosen network {self._network} which is not supported yet')

        self.agg_protocol = AggregationProtocol(self._session, self._chain_id)
        self.limit_protocol = LimitOrderProtocol(self._session, self._chain_id)

