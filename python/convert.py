def delete_char(text):
    text = text.replace(' ', '')
    text = text.replace('from', ' ')
    text = text.replace('to', ' ')
    text_list = text.split(' ')

    return(text_list)


def convert_from_text(text):
    data = delete_char(text)

    if len(data) == 1:
        return(convert_by_norminate(data[0], 10, 2))
    elif len(data) == 2:
        return(convert_by_norminate(data[0], int(data[1]), 2))
    else:
        return(convert_by_norminate(data[0], int(data[1]), int(data[2])))


def convert_by_norminate(num, from_base, to_base):
    is_minus = ''
    if isinstance(num, int):
        num = str(num)

    if num[0] == '-':
        num = num[1:]
        is_minus = '-'

    return is_minus + convert(num, from_base, to_base)


def convert(num, from_base, to_base):
    n = int(num, from_base)
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if n < to_base:
        return alphabet[n]
    else:
        return convert(str(n // to_base), 10, to_base) + alphabet[n % to_base]
