#!/usr/bin/env python3
import csv
from typing import List

"""
Module that contains the implementation of a simple pagination system.
It provides an index_range function to calculate pagination indices and a
Server class to handle fetching a paginated dataset of popular baby names.
"""


def index_range(page: int, page_size: int) -> tuple:
    """Function calculates the starting index and end index of a page

    Args:
        page (int): The page number
        page_size (int): The size of the page

    Returns:
        tuple: Returns a tuple containing the start and end index of the page
    """
    start_index = (page - 1) * page_size
    end_index = page_size + start_index
    return start_index, end_index


class Server:
    """Server class to paginate a database of popular baby names.
    """

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initializes the server with an empty dataset."""
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Fetches dataset of baby names, caching it after the first load."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Skip the header
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Returns a page of data from the dataset.

        Args:
            page (int): The page number to be shown.
            page_size (int): The size of the page to show.

        Returns:
            List[List]: A list representing the page of results.
        """
        # Validate inputs
        if not isinstance(page, int) or page <= 0:
            raise ValueError("page must be a positive integer")
        if not isinstance(page_size, int) or page_size <= 0:
            raise ValueError("page_size must be a positive integer")

        # Get the dataset
        dataset = self.dataset()

        # Get the indices for the page
        start_idx, end_idx = index_range(page, page_size)

        # Get the data for the requested page
        page_data = dataset[start_idx:end_idx]

        return page_data
