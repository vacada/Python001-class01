week08学习笔记
+ 变量
    + 可变数据类型
        + 列表 list
        + 字典 dict
    + 不可变数据类型
        + 整型 int
        + 浮点型 float
        + 字符串 string
        + 元组 tuple
+ 序列
    + 序列分类
        + 容器序列：list、tuple、collections.deque(对列)等，能存放不同类型的数据
        + 扁平序列：str、tytes、bytearry、memoryview(内存视图)、array.array等，存放单一类型的数据类型
    + 浅拷贝和深拷贝
        + 只对容器序列有效
        + 浅拷贝使用copy.copy()，深拷贝使用copy.deepcopy()
        + 浅拷贝只拷贝父对象，引用子对象；深拷贝完全拷贝
+ collections
    + from collections import namedtuple 命名元组
    + from collections import Counter 计数器
        + most_common(n) 获取数量最多的前n个
    + from collections import deque 双向队列
+ 标准库
    + functools
    + itertools
        + itertools.count() 无限计数器
        + itertools.cycle() 把传入的一个序列无限重复下去
        + itertools.repeat() 负责把一个元素无限重复下去，不过如果提供第二个参数就可以限定重复次数
        + itertools.chain() 可以把一组迭代对象串联起来，形成一个更大的迭代器
            ```python
            >>> for c in itertools.chain('ABC', 'XYZ'):
            ...     print(c)
            # 迭代效果：'A' 'B' 'C' 'X' 'Y' 'Z'
            ```
+ 闭包
    + 在一个内部函数中，对外部作用域的变量进行引用，(并且一般外部函数的返回值为内部函数)，那么内部函数就被认为是闭包
+ 装饰器
    + 装饰器是可调用对象，参数一般是另一个函数。装饰器可以以某种方式增强被装饰函数的行为，然后返回被装饰的函数或者将其替换成一个新的函数。
+ 对象协议
    + 常用魔术方法
        + 容器类型协议
            + \_\_str__ 打印对象时，默认输出该方法的返回值
            + \_\_getitem__、\_\_setitem__、\_\_delitem__ 字典索引操作
            + \_\_iter__ 迭代器
            + \_\_call__ 可调用对象协议
        + 比较大小的协议
            + \_\_eq__ 相等
            + \_\_gt__ 大于
            + \_\_lt__ 小于
        + 描述符协议和属性交互协议
            + \_\_get__
            + \_\_set__
        + 可哈希对象
            + \_\_hash__ 
        + 上下文管理器
            + with上下文表达式的用法，使用\_\_enter__()和__exit__()实现上下文管理器
+ 生成器
    + 在函数中使用yield关键字，可以实现生成器
    + 生成器可以让函数返回可迭代对象
    + return返回后，函数会中止，yield保持函数的执行状态，返回后，函数回到之前保存的状态继续执行
    + 函数被yield会暂停，局部变量也会保存
    + 迭代器终止后，会抛出StopIteration异常
    + 生成器和迭代器
        + iterables（可迭代） 包含\_\_getitem__()或__iter__()方法的容器对象
        + iterator（迭代器） 包含next()和__iter__方法
        + Generator（生成器） 包含yield语句的函数
    + 判断对象是否有这个功能
        ```python
        alist = [1, 2, 3, 4, 5]
        hasattr(alist, '__iter__')
        ```
+ 协程和线程的区别
    + 协程是异步的，线程是同步的
    + 协程是非抢占式的，线程是抢占式的
    + 线程是被动调度的，协程是主动调度的
    + 协程可以暂停函数的执行，保留上一次调用时的状态，是增强型生成器
    + 协程是用户级的任务调度，线程是内核级的任务调度
    + 协程适用于IO密集型程序，不适用于CPU密集型程序的处理