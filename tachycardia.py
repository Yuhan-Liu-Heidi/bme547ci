def is_tachycardic():
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
    instr = input("Input OCR record: ")
    instr = instr.lower()
    result = False
    if instr == 'tachycardic':
        result = True
    else:
        pass    
    return result


def main():
    result = is_tachycardic()
    print(result)


if __name__ == "__main__":
    main()
