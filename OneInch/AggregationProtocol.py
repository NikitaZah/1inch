from typing import Optional

from .AbstractProtocol import AbstractProtocol


class AggregationProtocol(AbstractProtocol):
    _version = 4.0
    _API_URL = 'https://api.1inch.io'

    def health_check(self) -> dict:
        """
        :return: {status: 'OK'} if API is stable
        """
        return self._get('healthcheck')

    def approve_spender(self):
        """
        :return: {address: str} address of 1inch router that must be trusted to spend funds for the exchange
        """
        return self._get('approve/spender')

    def approve_transaction(self, token_address: str, amount: Optional[str] = None):
        """
        :param token_address: Token address you want to exchange
        :param amount: The number of tokens that the 1inch router is allowed to spend.
        If not specified, it will be allowed to spend an infinite amount of tokens.
        :return:
        """
        params = {
            'tokenAddress': token_address,
        }
        if amount:
            params['amount'] = amount

        return self._get('approve/transaction', **params)

    def approve_allowance(self, token_address: str, wallet_address: str):
        params = {
            'tokenAddress': token_address,
            'walletAddress': wallet_address
        }
        return self._get('approve/allowance', **params)

    def liquidity_sources(self):
        return self._get('liquidity-sources')

    def tokens(self) -> list:
        return self._get('tokens')

    def presets(self):
        return self._get('presets')

    def quote(self, from_token: str, to_token: str, amount: int, **kwargs):
        params = {
            'fromTokenAddress': from_token,
            'toTokenAddress': to_token,
            'amount': amount
        }
        if kwargs:
            params.update(kwargs)

        return self._get('quote', **params)

    def swap(self, from_token: str, to_token: str, amount: int, from_address: str, slippage: float, **kwargs):

        params = {
            'fromTokenAddress': from_token,
            'toTokenAddress': to_token,
            'amount': amount,
            'fromAddress': from_address,
            'slippage': slippage
        }

        if kwargs:
            params.update(kwargs)

        return self._get('swap', **params)

