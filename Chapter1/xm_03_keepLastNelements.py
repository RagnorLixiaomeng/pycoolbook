# -*- coding: utf-8 -*-
# @Time : 2021/1/7 10:45 PM
# @Author: lixiaomeng_someday
# @Email : 131xxxx119@163.com
# @File : xm_03_keepLastNelements.py


from collections import deque

"""队列：先进先出，老的被挤掉"""
q = deque(maxlen=3)
q.append(1)
q.append(2)
q.append(3)

print(q)

q.append(4)

print(q)


"""yield:一个带有 yield 的函数就是一个 generator，它和普通函数不同，生成一个 generator 看起来像函数调用，但不会执行任何函数代码，直到对其调用 next()（在 for 循环中会自动调用 next()）才开始执行。虽然执行流程仍按函数的流程执行，但每执行到一个 yield 语句就会中断，并返回一个迭代值，下次执行时从 yield 的下一个语句继续执行。看起来就好像一个函数在正常执行的过程中被 yield 中断了数次，每次中断都会通过 yield 返回当前的迭代值。

yield 的好处是显而易见的，把一个函数改写为一个 generator 就获得了迭代能力，比起用类的实例保存状态来计算下一个 next() 的值，不仅代码简洁，而且执行流程异常清晰。

"""


def test_yield(n):
    print("ragnor")
    for i in range(n):
        yield(i*i)
        print("====i*i====", i*i)


for i in test_yield(5):
    print("-------i-------", i)
    print("test")


"""文件句柄可迭代对象：<class '_io.TextIOWrapper'>"""
with open(r"./somefile") as f:
    print(f)
    print(type(f))
    for line in f:
        print(line)
        print(type(line))
        if "python" in line:
            print("nb")

