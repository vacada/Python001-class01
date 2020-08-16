"""
__author__:'vacada'
__description__:自定义一个 python 函数，实现 map() 函数的功能。
__mtime__:2020/8/16
"""


def my_map(func, *iterables):
    try:
        its = [iter(it) for it in iterables]
        n = min([len(it) for it in iterables])
        while n > 0:
            args = [next(it) for it in its]
            yield func(*args)
            n -= 1
    except Exception as e:
        print(f'{e}')


if __name__ == "__main__":
    print(f'自定义map函数')
    print(list(my_map(lambda x,y: x+y, [1,2,3,4,5],range(4))))
    print(list(my_map(lambda x: x*2, [1,2,3,4])))
    print(f'系统map函数')
    print(list(map(lambda x,y: x+y, [1,2,3,4,5],range(4))))
    print(list(map(lambda x: x*2, [1,2,3,4])))

    

    