import logging
from typing import Union

logger = logging.getLogger("run")


class Blueprint:

    def __init__(self):
        logger.debug("Creating Blueprint.")

    @staticmethod
    def multiply_numbers(xx: Union[float, int], yy: Union[float, int]) -> float:
        """Compute and return the product of two numbers.

        :param xx: Multiplier
        :param yy: Multiplicand
        :return: Product of multiplication.

        TODO: Can Union[] be used to simplify TypeError catch?
        if not isinstance(xx, Union[float, int]) or not isinstance(yy, Union[float, int]):
            raise TypeError("Input arguments must be of type float or int.")

        """
        if (not isinstance(xx, float) and not isinstance(xx, int)) or (not isinstance(yy, float) and not
           isinstance(yy, int)):
            raise TypeError("Input arguments must be of type float or int.")
        return float(xx * yy)
