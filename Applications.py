def area_of_triangle(side1: float, side2: float) -> float:
    return 0.5 * float(side1) * float(side2)


def max_side_of_triangle(side1: float, side2: float) -> float:
    return side1 + side2 - 1


def convert_to_seconds(hours=0, minutes=0):
    return hours * 360 + minutes * 60


def recursive_string_repeat(string: str, repetitions: int) -> str:
    if repetitions < 0:
        return 'Invalid number of repeats'

    if not repetitions:
        return ''

    def repeat_helper(string_repeated, repetitions_remaining, string_formed):

        if repetitions_remaining == 0:
            return ''

        repetitions_remaining -= 1
        string_formed = string_repeated + repeat_helper(string_repeated, repetitions_remaining, string_formed)

        return string_formed

    output = repeat_helper(string, repetitions, '')

    return output
