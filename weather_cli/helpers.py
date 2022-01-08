from typing import Iterable


def kelvin_to_fahrenheit(kelvin_temp: int) -> int:
    """
    Helper to convert Kelvin to Fahrenheit.

    Formula:
    (0K − 273.15) × 9/5 + 32
    """
    return int(((kelvin_temp - 273.15) * 9 / 5) + 32)


def print_lines(iterable: Iterable):
    """
    Helper to print all values in an iterable object.
    """
    for line in iterable:
        print(line)
