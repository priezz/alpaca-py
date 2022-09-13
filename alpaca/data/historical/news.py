"""This module handles News API Historical section."""
from typing import List, Optional, Union, Dict

from alpaca.common.enums import BaseURL
from alpaca.common.rest import RESTClient
from alpaca.data.models import NewsSet
from alpaca.data.requests import NewsRequest


class NewsHistoricalDataClient(RESTClient):
    """
    The REST client for interacting with Alpaca Market Data API stock data endpoints.

    Learn more on https://alpaca.markets/docs/market-data/
    """

    def __init__(
        self,
        api_key: Optional[str] = None,
        secret_key: Optional[str] = None,
        oauth_token: Optional[str] = None,
        raw_data: bool = False,
        url_override: Optional[str] = None,
    ) -> None:
        """
        Instantiates a News Historical Data Client.

        Args:
            api_key (Optional[str], optional): Alpaca API key. Defaults to None.
            secret_key (Optional[str], optional): Alpaca API secret key. Defaults to None.
            oauth_token (Optional[str]): The oauth token if authenticating via OAuth. Defaults to None.
            raw_data (bool, optional): If true, API responses will not be wrapped and raw responses will be returned from
              methods. Defaults to False. This has not been implemented yet.
            url_override (Optional[str], optional): If specified allows you to override the base url the client points
              to for proxy/testing.
        """
        super().__init__(
            api_key=api_key,
            secret_key=secret_key,
            oauth_token=oauth_token,
            api_version="v1beta1",
            base_url=url_override if url_override is not None else BaseURL.DATA,
            sandbox=False,
            raw_data=raw_data,
        )

    def get_news(self, request_params: NewsRequest) -> NewsSet:
        """
        Returns historical news data for an equity or list of equities over a given
        time period and timeframe.

        Args:
            request_params (GetStockBarsRequest): The request object for retrieving stock bar data.

        Returns:
            Union[BarSet, RawData]: The bar data either in raw or wrapped form.
        """
        params = request_params.to_request_fields()

        # paginated get request for market data api
        raw_news = self._data_get(
            endpoint_data_type="news",
            api_version=self._api_version,
            **params,
        )

        if self._use_raw_data:
            return raw_news

        return NewsSet(raw_news)