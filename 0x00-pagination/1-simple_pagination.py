#!/usr/bin/env python3
import csv
from typing import List

"""
Module conatains an index_range funtion
"""


def index_range(page: int, page_size: int) -> tuple:
    """Functon calculates the starting index and end inde of page

    Args:
        page (int): The page number
        page_size (int): The size of the page

    Returns:
        (tuple): Returns a tuple containing the start and end index of
        the page
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

        Args:
            page (int): The page to be showed
            page_size (int): Size of the page

        Returns:
            Returns the page as a list
        """
        self.__dataset = self.dataset()
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        data = index_range(page, page_size)
        names = self.__dataset[data[0]:data[1]]
        if (names):
            return names
        return []
