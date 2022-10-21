#!/usr/bin/python
# ! encoding=utf-8

def to_str(bytes_or_str):
    """
    convert byte to str
    :param bytes_or_str:
    :return:
    """
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode('utf-8')
    else:
        value = bytes_or_str
    return value
