from itertools import combinations_with_replacement
from typing import List


def find_fewest_coins(coins: List[int], total_change: int) -> List:
    if not total_change:
        return []

    if total_change < 0:
        raise ValueError('Change can\'t be negative')

    if not coins:
        raise ValueError('No coins left.')

    if total_change < min(coins):
        raise ValueError('No suitable coins for change.')

    for i in range(1, total_change + 1):
        for combination in combinations_with_replacement(coins, i):
            if sum(combination) == total_change:
                return sorted(list(combination))

    raise ValueError('No suitable coins for change.')
