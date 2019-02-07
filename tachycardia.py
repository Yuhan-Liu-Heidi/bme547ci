import re


def is_tachycardic(instr):
    """Interpret whether a string contains "tachycardic"

    This function decides if an input from OCR record contains
    the word 'tachycardic'. Input string might contain upper
    case, lower case or both. The function shall allows up to
    2 typo or missing character and space/punctuation.

    Args:
        instr (string): string from the OCR record

    Returns:
        result (boolean): whether the string contains the word

    """
    instr = "".join(re.findall(r'[A-Za-z]', instr))
    instr = instr.lower()
    expected = "tachycardic"
    result = False
    if instr == expected:
        result = True
    return result


def take_input():
    """Take user input and call is_tachycardic

    Args:
        None

    Returns:
        String (str): Inputed string
    """
    instr = input("Input OCR record: ")
    result = is_tachycardic(instr)
    return result


def main():
    result = take_input()
    print(result)


if __name__ == "__main__":
    main()
