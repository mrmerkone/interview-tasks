"""
Reverse an input positive integer number without using any type conversion.
"""


def reverse_int(number: int) -> int:
    """Implement me!"""
    raise NotImplementedError


def main():
    cases = (
        (1, 1),
        (54, 45),
        (123456, 654321),
        (7824, 4287)
    )

    for number, expected in cases:
        output = reverse_int(number)
        assert output == expected, f"Input: {number} Output: {output} Expected: {expected}"

    print("All tests passed!")


if __name__ == '__main__':
    main()
