#!/usr/bin/env python3
"""
Module conatains an index_range funtion"""


import csv
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """Functon calculates starting index and end inde of page
    """
    start_index = (page - 1) * page_size
    end_index = page_size + start_index
    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Returns the Page
        """
        self.__dataset = self.dataset()
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        data = index_range(page, page_size)
        names = self.__dataset[data[0]:data[1]]
        if (names):
            return names
        return []
