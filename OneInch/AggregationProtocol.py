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

    def approve_spender(self) -> dict:
        """
        :return: {address: str} address of 1inch router that must be trusted to spend funds for the exchange
        """
        return self._get('approve/spender')

    def approve_transaction(self, token_address: str, amount: Optional[str] = None) -> dict:
        """
        :param token_address: Token address you want to exchange
        :param amount: The number of tokens that the 1inch router is allowed to spend.
        If not specified, it will be allowed to spend an infinite amount of tokens.
        :return: {'data': transaction hash (str),
                  'gasPrice': amount (str),
                  'to': address (str),
                  'value': value (str),
                  }
        """
        params = {
            'tokenAddress': token_address,
        }
        if amount:
            params['amount'] = amount

        return self._get('approve/transaction', **params)

    def approve_allowance(self, token_address: str, wallet_address: str) -> dict:
        """
        :param token_address: Token address you want to exchange
        :param wallet_address: Wallet address for which you want to check
        :return: {'allowance': str}
        """
        params = {
            'tokenAddress': token_address,
            'walletAddress': wallet_address
        }
        return self._get('approve/allowance', **params)

    def liquidity_sources(self) -> dict:
        """
        :return: {'protocols': list[dict]}
        dict = {'id': str, 'title': str, 'img': link (str), 'img_color': link (str)}
        """
        return self._get('liquidity-sources')

    def tokens(self) -> dict:
        """
        :return: {'tokens': dict}
        dict = {address (str): {
                                'symbol': str,
                                'name': str,
                                'decimals': int,
                                'address': str,
                                'logoURI': link (str),
                                'tags': list[str]
                                }
                }
        """
        return self._get('tokens')

    def presets(self) -> dict:
        """
        :return: {
                  'MAX_RESULT': list[dict],
                  'LOWEST_GAS': list[dict].
                  }
        dict = {
                'complexityLevel': int,
                'mainRouteParts': int,
                'parts': int,
                'virtualParts': int
                }
        """
        return self._get('presets')

    def quote(self, from_token: str, to_token: str, amount: int, **kwargs) -> dict:
        """
        :param from_token: token address
        :param to_token: token address
        :param amount: amount
        :param kwargs: {
                        'protocols': list, \\ default: all
                        'fee': int, \\ Min: 0; max: 3; Max: 0; max: 3; default: 0; !should be the same for quote and swap!;
                        'gasLimit': int,
                        'connectorTokens': list, \\ max: 5; !should be the same for quote and swap!;
                        'complexityLevel': int, \\ min: 0; max: 3; default: 2; !should be the same for quote and swap!;
                        'mainRouteParts': int, \\ default: 10; max: 50 !should be the same for quote and swap!;
                        'parts': int, \\ split parts. default: 50; max: 100!should be the same for quote and swap!;
                        'gasPrice': int, \\ default: fast from network;
                        }
        :return: {
                  'fromToken': token (dict),
                  'toToken': token (dict),
                  'toTokenAmount': amount (str),
                  'fromTokenAmount': amount (str),
                  'protocols': list[list[list[dict]]],
                  'estimatedGas': int
        """
        params = {
            'fromTokenAddress': from_token,
            'toTokenAddress': to_token,
            'amount': amount
        }
        if kwargs:
            params.update(kwargs)

        return self._get('quote', **params)

    def swap(self, from_token: str, to_token: str, amount: int, from_address: str, slippage: float, **kwargs) -> dict:
        """
        :param from_token: address (str)
        :param to_token: address (str)
        :param amount: amount (int)
        :param from_address: address (str) \\ The address that calls the 1inch contract
        :param slippage: int \\ min: 0; max: 50;
        :param kwargs: {
                        'protocols': list, \\ default: all;
                        'destReceiver': address (str)\\ Receiver of destination currency. default: fromAddress;
                        'referrerAddress' address (str);
                        'fee': int, \\ Min: 0; max: 3; Max: 0; max: 3; default: 0; !should be the same for quote and swap!;
                        'gasPrice': int, \\ default: fast from network;
                        'disableEstimate': bool,
                        'permit': str \\ https://eips.ethereum.org/EIPS/eip-2612
                        'burnChi': bool \\ default: false; Suggest to check user's balance and allowance before set this
                                           flag; CHI should be approved to spender address
                        'allowPartialFill': bool,
                        'parts': int, \\ split parts. default: 50; max: 100!should be the same for quote and swap
                        'mainRouteParts': int, \\ default: 10; max: 50 !should be the same for quote and swap!
                        'connectorTokens': list, \\ max: 5; !should be the same for quote and swap!
                        'complexityLevel': int, \\ min: 0; max: 3; default: 2; !should be the same for quote and swap!
                        'gasLimit': int
        :return: {
                 'fromToken': token (dict),
                 'toToken': token (dict),
                 'toTokenAmount': str,
                 'fromTokenAmount': str,
                 'protocols': list[str],
                 'tx': {
                       'from': str,
                       'to': str,
                       'data': str,
                       'value': str,
                       'gasPrice': str,
                       'gas': str,
                       }
                 }

        """
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
