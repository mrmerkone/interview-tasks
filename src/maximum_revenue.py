"""
Given an array of a hourly market stock cost during one day, find a maximum possible revenue
if you can buy and sell stock only once per day.

If no potential revenue return None.
"""
from typing import List, Optional


def maximum_revenue(stock_costs: List[float]) -> Optional[float]:
    """Implement me!"""
    raise NotImplementedError


def main():
    cases = (
        ([44.2, 43.1, 46.5, 47.8, 47.2, 46.9, 46.8, 47.0, 47.6, 47.9, 48.2, 48.7], 5.6),
        ([31.2, 30.9, 30.1, 31.0, 31.2, 32.4, 31.9, 30.4, 29.9, 31.0, 31.8, 33.7], 3.8),
        ([63.2, 63.1, 62.6, 62.5, 62.2, 61.9, 61.5, 60.4, 60.0, 59.8, 59.0, 58.4], None)
    )

    for stock_costs, expected in cases:
        output = maximum_revenue(stock_costs)
        assert output == expected, f"Input: {stock_costs} Output: {output} Expected: {expected}"

    print("All tests passed!")


if __name__ == '__main__':
    main()
