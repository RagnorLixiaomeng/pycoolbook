# -*- coding: utf-8 -*-
# @Time : 2021/1/13 9:23 PM
# @Author: lixiaomeng_someday
# @Email : 131xxxx119@163.com
# @File : xm_04_getMaxOrMinNnums.py

"""怎样从一个集合中获得最大或者最小的 N 个元素列表？"""

import heapq

nums = [4, 1, 7, 9, -1, 19]

print(heapq.nlargest(3, nums))
print(heapq.nsmallest(3, nums))


portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]

cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])

print(cheap)
print(expensive)


nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
heap = list(nums)
heapq.heapify(heap)
print(heap)
print(heap[0])

"""堆数据结构最重要的特征是 heap[0] 永远是最小的元素。
并且剩余的元素可以很容易的通过调用 heapq.heappop() 方法得到， 
该方法会先将第一个元素弹出来，然后用下一个最小的元素来取代被弹出元素（这种操作时间复杂度仅仅是 O(log N)，N 是堆大小）。 
比如，如果想要查找最小的 6 个元素，你可以这样做："""
for i in range(6):
    small_num = heapq.heappop(heap)
    print(small_num)
