#!/usr/bin/env python3

"""Module conatains an index_range funtion"""


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
