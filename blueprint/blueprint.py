class Blueprint:

    @staticmethod
    def multiply_ints(xx: int, yy: int) -> int:
        if not isinstance(xx, int) or not isinstance(yy, int):
            raise TypeError("Input arguments must be of type integer.")
        return xx * yy
