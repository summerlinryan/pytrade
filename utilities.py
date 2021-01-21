from typing import List


def partition(l: List, n: int) -> List[List]:
    """
    Partition l into lists of size n (or less than n if less than n are
    remaining for the last partition).
    :param l List to partition
    :param n Size of partitions
    :returns List of partitions (lists), each of size n (or less for the last partition)
    """
    for i in range(0, len(l), n):
        yield l[i:i + n]
