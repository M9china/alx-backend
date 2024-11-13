#!/usr/bin/env python3
"""
Module contains an index_range function
"""

import csv
import math
from typing import List, Dict, Any


def index_range(page: int, page_size: int) -> tuple:
    """Function calculates the starting index and end index of the page."""
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Skip the header row
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Returns the page."""
        self.__dataset = self.dataset()
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        data = index_range(page, page_size)
        names = self.__dataset[data[0]:data[1]]
        if names:
            return names
        return []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """Returns hypermedia pagination data."""
        if page_size <= 0:
            return {
                'page_size': page_size,
                'page': page,
                'data': [],
                'next_page': None,
                'prev_page': None,
                'total_pages': 0,
            }

        min_val, max_val = index_range(page, page_size)
        items = len(self.dataset())
        total_pages = math.ceil(items / page_size)

        # Ensure that we don't request more pages than available
        page = min(page, total_pages)

        # Handle page data
        hyper_data: Dict[str, Any] = {}
        hyper_data['page_size'] = page_size
        hyper_data['page'] = page
        hyper_data['data'] = self.get_page(page, page_size)

        # Handle next_page and prev_page
        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        hyper_data['next_page'] = next_page
        hyper_data['prev_page'] = prev_page
        hyper_data['total_pages'] = total_pages

        return hyper_data
