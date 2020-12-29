# -*- coding: utf-8 -*-
# @Time : 2020/12/29 9:06 PM
# @Author: lixiaomeng_someday
# @Email : 131xxxx119@163.com
# @File : xm_02_starUnpackSequence.py


"""
let nature take its course
"""
import numpy as np


def drop_first_last(grades):
    first, *middle, last = grades
    return np.average(middle)


result = drop_first_last([1, 3, 5, 7, 9])
print(result)

