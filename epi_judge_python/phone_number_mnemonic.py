from test_framework import generic_test, test_utils


def phone_mnemonic(phone_number):
    # TODO - you fill in here.
    MAPPING = ['0', '1', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
    if not phone_number:
        return ['']

    ret = []
    stuff = phone_mnemonic(phone_number[:-1])
    chars = MAPPING[int(phone_number[-1])]
    for shit in stuff:
        for char in list(chars):
            ret.append(shit + char)
    
            
    return ret


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "phone_number_mnemonic.py",
            'phone_number_mnemonic.tsv',
            phone_mnemonic,
            comparator=test_utils.unordered_compare))
