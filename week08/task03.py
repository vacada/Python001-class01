"""
__author__:'vacada'
__description__:
实现一个 @timer 装饰器，记录函数的运行时间，注意需要考虑函数可能会接收不定长参数。
__mtime__:2020/8/16
"""

import time
from functools import wraps


def timer(func):
    @wraps(func)
    def inner(*args, **kwargs):
        start_time = time.time()
        ret = func(*args, **kwargs)
        end_time = time.time()
        print(f'total time: {end_time - start_time}')
        return ret
    return inner


@timer
def my_list(number):
    result = 0
    for i in range(number):
        result += i
    return result

print(my_list(100000))
