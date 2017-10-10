# help 함수
# help(print)


def plus(a, b):
    """
    return the sum of parameter a, b
    :param a:
    :param b:
    :return: sum
    """
    return a+b


# plus.__doc__ = 'return the sum of parameter a, b'

help(plus)
print(plus.__doc__)

