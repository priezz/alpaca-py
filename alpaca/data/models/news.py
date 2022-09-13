"""Base models for the News object."""
from datetime import datetime
from typing import Optional, Dict, List

import pandas as pd

from alpaca.common import ValidateBaseModel as BaseModel
from alpaca.common import RawData
from alpaca.data.models import BaseDataSet
from alpaca.data.models import TimeSeriesMixin

class News(BaseModel):
    """Represents one bar/candlestick of aggregated trade data over a specified interval.

    Attributes:
        id: (str): The ID of the object.
        headline: (str): The headline or title of the article.
        author: (str): The author of the article.
        created_at: (datetime): The datetime article was created.
        updated_at: (datetime): The datetime article was updated.
        summary: (str): The .
        content: (Optional[str]): The .
        images: (List[Dict[str, str]]): The .
        symbols: (List[str]): The .
        source: (str): The .
    """

    id: str
    headline: str
    author: str
    created_at: datetime
    updated_at: datetime
    summary: str
    content: Optional[str]
    images: List[Dict[str, str]]
    symbols: List[str]
    source: str

class NewsSet(BaseDataSet, TimeSeriesMixin):
    """A collection of News.

    Attributes:
        data (Dict[str, List[News]]): The collection of News keyed by ID.
    """
    data: List[News]

    def __init__(
        self,
        raw_data: RawData,
    ) -> None:
        """A collection of Bars.

        Args:
            raw_data (RawData): The collection of raw news data from API keyed by ID.
        """

        super().__init__(data=raw_data)

    @property
    def df(self) -> pd.DataFrame:
        """
        Convert news to pandas DataFrame.
        
        Returns:
            df: The data in DataFrame form.
        """
        return pd.DataFrame([dict(_news) for _news in self.data]).set_index("created_at")