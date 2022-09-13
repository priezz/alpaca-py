from datetime import datetime
from typing import Dict

import pandas as pd

from alpaca.data.historical import NewsHistoricalDataClient
from alpaca.data.requests import NewsRequest
from alpaca.data.models import NewsSet


def test_get_news(reqmock, news_client: NewsHistoricalDataClient):
    """Test to get news historical data."""

    symbols = ["AAPL", "TSLA"]
    start = datetime(2021, 12, 30)
    limit = 2
    _start_in_url = start.isoformat("T") + "Z"
    reqmock.get(
        f"https://data.alpaca.markets/v1beta1/news?start={_start_in_url}&limit={limit}&symbols={','.join(symbols)}",
        text="""
        {
            "news": [
                {
                    "author": "Charles Gross",
                    "content": "",
                    "created_at": "2022-09-12T17:04:52Z",
                    "headline": "Ten Stocks Trending on Discord for Monday September 12, 2022: PXMD, INM, RGLS, AVCT, NRBO, SPPI, AAPL, BBIG, IFBD, RMED",
                    "id": 28834187,
                    "images": [],
                    "source": "benzinga",
                    "summary": "",
                    "symbols": [
                        "AAPL",
                        "AVCT",
                        "BBIG",
                        "IFBD",
                        "INM",
                        "NRBO",
                        "PXMD",
                        "RGLS",
                        "RMED",
                        "SPPI"
                    ],
                    "updated_at": "2022-09-12T17:04:53Z",
                    "url": "https://www.benzinga.com/news/22/09/28834187/ten-stocks-trending-on-discord-for-monday-september-12-2022-pxmd-inm-rgls-avct-nrbo-sppi-aapl-bbig-i"
                },
                {
                    "author": "Benzinga Insights",
                    "content": "",
                    "created_at": "2022-09-12T16:38:15Z",
                    "headline": "Check Out What Whales Are Doing With AAPL",
                    "id": 28833719,
                    "images": [
                        {
                            "size": "large",
                            "url": "https://cdn.benzinga.com/files/imagecache/2048x1536xUP/images/story/2022/movers_image_16763.jpeg"
                        },
                        {
                            "size": "small",
                            "url": "https://cdn.benzinga.com/files/imagecache/1024x768xUP/images/story/2022/movers_image_16763.jpeg"
                        },
                        {
                            "size": "thumb",
                            "url": "https://cdn.benzinga.com/files/imagecache/250x187xUP/images/story/2022/movers_image_16763.jpeg"
                        }
                    ],
                    "source": "benzinga",
                    "summary": "A whale with a lot of money to spend has taken a noticeably bearish stance on Apple.\nLooking at options history for Apple (NASDAQ:AAPL) we detected 210 strange trades.",
                    "symbols": [
                        "AAPL"
                    ],
                    "updated_at": "2022-09-12T16:38:15Z",
                    "url": "https://www.benzinga.com/markets/options/22/09/28833719/check-out-what-whales-are-doing-with-aapl"
                }
            ],
            "next_page_token": "MTY2MzAwMDY5NTAwMDAwMDAwMHwyODgzMzcxOQ=="
        }
        """)
    request = NewsRequest(
        symbol_or_symbols=symbols, start=start, limit=limit
    )
    news_set = news_client.get_news(request_params=request)

    assert isinstance(news_set, NewsSet)
    assert isinstance(news_set.df, pd.DataFrame)
