from pie.file_utils import read_lines

snafu_decimal = {"2": 2, "1": 1, "0": 0, "-": -1, "=": -2}


def snafu_to_decimal(snafu: str) -> int:
    snafu_reversed = snafu[::-1]
    decimal = 0
    for idx, snafu_char in enumerate(snafu_reversed):
        dec_modifier = snafu_decimal[snafu_char]
        decimal += dec_modifier * (5**idx)

    return decimal


def decimal_to_snafu(decimal: int) -> str:
    snafu = ""
    while decimal > 0:
        remainder = decimal % 5
        decimal //= 5
        if remainder in {0, 1, 2}:
            snafu = str(remainder) + snafu
        elif remainder == 3:
            snafu = "=" + snafu
            decimal += 1
        else:
            snafu = "-" + snafu
            decimal += 1

    return snafu


if __name__ == "__main__":
    decimals = [snafu_to_decimal(line) for line in read_lines("twentyfive/input.txt")]
    target = sum(decimals)
    print(f"snafu of {target} is {decimal_to_snafu(target)}")
