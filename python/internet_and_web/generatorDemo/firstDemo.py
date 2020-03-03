#!/usr/bin/python
# -*- coding: utf-8 -*-

print('****************斐波那契********************')
# 斐波那契
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

g = fib(10)
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print('****************斐波那契********************')



print('****************杨辉三角********************')
# 杨辉三角
def triangles():
    a = [1]
    while True:
        yield a
        a = [sum(i) for i in zip([0] + a, a + [0])]
g = triangles()

for i in range(10):
    print(next(g))

print('****************杨辉三角********************')


print('****************生产者消费者协程实现********************')
import time
import queue


def consumer(name):
    print("--->starting eating baozi...")
    while True:
        new_baozi = yield
        print("[%s] is eating baozi %s" % (name, new_baozi))


def producer():
    r = con.__next__()
    r = con2.__next__()
    n = 0
    while n < 5:
        n += 1
        con.send(n)
        con2.send(n)
        time.sleep(1)
        print("\033[32;1m[producer]\033[0m is making baozi %s" % n)



con = consumer("c1")
con2 = consumer("c2")
p = producer()

print('****************生产者消费者协程实现********************')




print('****************gevent********************')
from urllib import request
import gevent, time
from gevent import monkey

monkey.patch_all()  # 把当前程序的所有的io操作给我单独的做上标记


def f(url):
    print('GET: %s' % url)
    resp = request.urlopen(url)
    data = resp.read()
    print('%d bytes received from %s.' % (len(data), url))
    page = open('url.html', 'wb')
    page.write(data)
    page.close()


urls = ['https://www.python.org/',
        'https://www.yahoo.com/',
        'https://github.com/']
time_start = time.time()
for url in urls:
    f(url)
print("同步cost", time.time() - time_start)
async_time_start = time.time()
gevent.joinall([
    gevent.spawn(f, 'https://www.python.org/'),
    gevent.spawn(f, 'https://www.yahoo.com/'),
    gevent.spawn(f, 'https://github.com/'),
])
print("异步cost", time.time() - async_time_start)

print('****************gevent********************')
print('****************笔试题********************')
print('****************笔试题********************')



