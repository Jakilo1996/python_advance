> # threading模块介绍：
#
# threading模块是python中专门提供用来做多线程编程的模块。
# threading模块中最常用的类是Thread。以下看一个简单的多线程程序：
# 查看线程数：
#       使用threading.enumerate()函数便可以看到当前线程的数量。
#
# 查看当前线程的名字：
#        使用threading.current_thread()可以看到当前线程的信息。
<
```python
import threading
import time
from decorator.time_fuc_dec import timeit


def coding():
    for x in range(3):
        print(f'{x}正在写代码')
        time.sleep(1)


def drawing():
    for x in range(3):
        print(f'{x}正在画图')
        time.sleep(1)


@timeit()
def single_thread():
    coding()
    drawing()


@timeit()
def multi_threading():
    t1 = threading.Thread(target=coding)
    t2 = threading.Thread(target=drawing)
    t1.start()
    t2.start()
    print(threading.enumerate(),'\n', threading.current_thread())
    # # [<_MainThread(MainThread, started 4655588864)>, <Thread(Thread-1, started 123145550004224)>, <Thread(Thread-2, started 123145555259392)>]
    #    <_MainThread(MainThread, started 4655588864)>

if __name__ == '__main__':
    # single_thread()
    # 0正在写代码
    # 1正在写代码
    # 2正在写代码
    # 0正在画图
    # 1正在画图
    # 2正在画图
    # None_single_thread duration 6.0214128494262695
    multi_threading()  # 主线程执行完 直接退出了  等子线程完成

```
--- 
# 继承自threading.Thread类：
# 为了让线程代码更好的封装。可以使用threading模块下的Thread类，继承自这个类，然后实现run方法，
# 线程就会自动运行run方法中的代码。示例代码如下：
```python
import threading
import time
from decorator.time_fuc_dec import timeit


class CodingThread(threading.Thread):
    @timeit()
    def run(self):
        for x in range(3):
            print(f'{threading.current_thread()}正在编码')
            time.sleep(1)


class DrawingThread(threading.Thread):
    @timeit()
    def run(self):
        for x in range(3):
            print(f'{threading.current_thread()}正在画图')
            time.sleep(1)


@timeit()
def multi_threading():
    coding = CodingThread()
    drawing = DrawingThread()
    coding.start()
    drawing.start()
    coding.join()
    drawing.join()
    print(f'{__name__}执行完成')


if __name__ == '__main__':
    multi_threading()


    # output
    # <CodingThread(Thread-1, started 123145452445696)>正在编码
    # <DrawingThread(Thread-2, started 123145457700864)>正在画图
    # <CodingThread(Thread-1, started 123145452445696)>正在编码<DrawingThread(Thread-2, started 123145457700864)>正在画图
    #
    # <DrawingThread(Thread-2, started 123145457700864)>正在画图<CodingThread(Thread-1, started 123145452445696)>正在编码
    #
    # _run duration 3.006542205810547
    # _run duration 3.0065767765045166
    # __main__执行完成
    # _multi_threading duration 3.00705623626709
```
--- 
# 多线程共享全局变量的问题：
# 多线程都是在同一个进程中运行的。因此在进程中的全局变量所有线程都是可共享的。
# 这就造成了一个问题，因为线程执行的顺序是无序的。有可能会造成数据错误。比如以下代码：
```python
import threading
from decorator.time_fuc_dec import timeit
tickets = 0


def get_ticket():
    global tickets
    for x in range(10000000):
        tickets += 1
    print(f'ticket:{tickets}')

@timeit()
def main_threading():
    for x in range(2):
        t = threading.Thread(target=get_ticket)
        t.start()
        # t.join()


if __name__ == '__main__':
    main_threading()
    print(tickets)   #  主线程执行完成时， 全局变量是多少 就打印什么
#

# import threading
#
# tickets = 0
#
# def get_ticket():
#     global tickets
#     for x in range(1000000):
#         tickets += 1
#     print('tickets:%d'%tickets)
#
# def main():
#     for x in range(2):
#         t = threading.Thread(target=get_ticket)
#         t.start()
#
# if __name__ == '__main__':
#     main()
```

---
# 锁机制：
# 为了解决以上使用共享全局变量的问题。
# threading提供了一个Lock类，这个类可以在某个线程访问某个变量的时候加锁，
# 其他线程此时就不能进来，直到当前线程处理完后，把锁释放了，其他线程才能进来处理。示例代码如下
```python
import threading
from decorator.time_fuc_dec import timeit

value = 0

glock = threading.Lock()


def add_value():
    global value
    for x in range(10000000):
        glock.acquire()
        value += 1
        glock.release()
    print(f'value:{value}')

def add_value2():
    global value
    glock.acquire()
    for x in range(10000000):

        value += 1
    glock.release()
    print(f'value:{value}')

@timeit()
def main_threading():
    for x in range(3):
        # t = threading.Thread(target=add_value)
        # 大量的加锁释放锁 导致实际处理速度偏慢
        t = threading.Thread(target=add_value2)
        # 类似于线性处理3次加运算
        t.start()


if __name__ == '__main__':
    main_threading()


# import threading
#
# tickets = 0
#
# def get_ticket():
#     global tickets
#     for x in range(1000000):
#         tickets += 1
#     print('tickets:%d'%tickets)
#
# def main():
#     for x in range(2):
#         t = threading.Thread(target=get_ticket)
#         t.start()
#
# if __name__ == '__main__':
#     main()
```
---
Lock版本生产者和消费者模式：
生产者和消费者模式是多线程开发中经常见到的一种模式。生产者的线程专门用来生产一些数据，然后存放到一个中间的变量中。
消费者再从这个中间的变量中取出数据进行消费。但是因为要使用中间变量，中间变量经常是一些全局变量，因此需要使用锁来保证数据完整性。
以下是使用threading.Lock锁实现的“生产者与消费者模式”的一个例子：
```python
import threading
import random
import time

gMoney = 1000
gLock = threading.Lock()
# 记录生产者生产的次数，达到10次就不再生产
gTimes = 0


class Producer(threading.Thread):
    def run(self):
        global gLock
        global gTimes
        global gMoney
        while 1:
            gLock.acquire()
            if gTimes <= 10:
                money = random.randint(100, 1000)

                gMoney += money
                print(f'{threading.current_thread()}_produce_money:{money},current_money:{gMoney}')
                time.sleep(1)
                gTimes += 1
                gLock.release()
            else:
                gLock.release()
                print('10次生产完成')
                break


class Consumer(threading.Thread):
    def run(self):
        global gLock
        global gTimes
        global gMoney
        while 1:
            money = random.randint(100,1000)
            gLock.acquire()
            if money <= gMoney:

                gMoney -= money
                print(f'{threading.current_thread()}_consumer_money:{money},current_money:{gMoney}')
                time.sleep(1)
            else:
                if gTimes >= 10:
                    gLock.release()
                    print(f'全部消费,剩余{gMoney},想花费{money}')
                    break
            gLock.release()

def main():
    for x in range(5):
        Consumer(name='消费者线程').start()

    for x in range(5):
        Producer(name='消费者线程').start()


if __name__ == '__main__':
    main()
```
`# Queue线程安全队列：
# 在线程中，访问一些全局变量，加锁是一个经常的过程。如果你是想把一些数据存储到某个队列中，那么Python内置了一个线程安全的模块叫做queue模块。
# Python中的queue模块中提供了同步的、线程安全的队列类，包括FIFO（先进先出）队列Queue，LIFO（后入先出）队列LifoQueue。
# 这些队列都实现了锁原语（可以理解为原子操作，即要么不做，要么都做完），能够在多线程中直接使用。可以使用队列来实现线程间的同步。相关的函数如下：
#
# 初始化Queue(maxsize)：创建一个先进先出的队列。
# qsize()：返回队列的大小。
# empty()：判断队列是否为空。
# full()：判断队列是否满了。
# get()：从队列中取最后一个数据。
# put()：将一个数据放到队列中。`
```python
import threading
import requests
from lxml import etree
from urllib import request
import os
import re
from queue import Queue

class Producer(threading.Thread):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
    }
    def __init__(self,page_queue,img_queue,*args,**kwargs):
        super(Producer, self).__init__(*args,**kwargs)
        self.page_queue = page_queue
        self.img_queue = img_queue


    def run(self):
        while True:
            if self.page_queue.empty():
                break
            url = self.page_queue.get()
            self.parse_page(url)

    def parse_page(self,url):
        response = requests.get(url,headers=self.headers)
        text = response.text
        html = etree.HTML(text)
        imgs = html.xpath("//div[@class='page-content text-center']//a//img")
        for img in imgs:
            if img.get('class') == 'gif':
                continue
            img_url = img.xpath(".//@data-original")[0]
            suffix = os.path.splitext(img_url)[1]
            alt = img.xpath(".//@alt")[0]
            alt = re.sub(r'[，。？?,/\\·]','',alt)
            img_name = alt + suffix
            self.img_queue.put((img_url,img_name))

class Consumer(threading.Thread):
    def __init__(self,page_queue,img_queue,*args,**kwargs):
        super(Consumer, self).__init__(*args,**kwargs)
        self.page_queue = page_queue
        self.img_queue = img_queue

    def run(self):
        while True:
            if self.img_queue.empty():
                if self.page_queue.empty():
                    return
            img = self.img_queue.get(block=True)
            url,filename = img
            request.urlretrieve(url,'images/'+filename)
            print(filename+'  下载完成！')

def main():
    page_queue = Queue(100)
    img_queue = Queue(500)
    for x in range(1,101):
        url = "http://www.doutula.com/photo/list/?page=%d" % x
        page_queue.put(url)

    for x in range(5):
        t = Producer(page_queue,img_queue)
        t.start()

    for x in range(5):
        t = Consumer(page_queue,img_queue)
        t.start()

if __name__ == '__main__':
    main()
```
---

GIL全局解释器锁：
Python自带的解释器是CPython。CPython解释器的多线程实际上是一个假的多线程（在多核CPU中，只能利用一核，不能利用多核）。同一时刻只有一个线程在执行，为了保证同一时刻只有一个线程在执行，在CPython解释器中有一个东西叫做GIL（Global Intepreter Lock），叫做全局解释器锁。这个解释器锁是有必要的。因为CPython解释器的内存管理不是线程安全的。当然除了CPython解释器，还有其他的解释器，有些解释器是没有GIL锁的，见下面：

Jython：用Java实现的Python解释器。不存在GIL锁。更多详情请见：https://zh.wikipedia.org/wiki/Jython
IronPython：用.net实现的Python解释器。不存在GIL锁。更多详情请见：https://zh.wikipedia.org/wiki/IronPython
PyPy：用Python实现的Python解释器。存在GIL锁。更多详情请见：https://zh.wikipedia.org/wiki/PyPy
GIL虽然是一个假的多线程。但是在处理一些IO操作（比如文件读写和网络请求）还是可以在很大程度上提高效率的。在IO操作上建议使用多线程提高效率。在一些CPU计算操作上不建议使用多线程，而建议使用多进程。
```python
import requests
from lxml import etree
import threading
from queue import Queue
import csv


class BSSpider(threading.Thread):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
    }
    def __init__(self,page_queue,joke_queue,*args,**kwargs):
        super(BSSpider, self).__init__(*args,**kwargs)
        self.base_domain = 'http://www.budejie.com'
        self.page_queue = page_queue
        self.joke_queue = joke_queue

    def run(self):
        while True:
            if self.page_queue.empty():
                break
            url = self.page_queue.get()
            response = requests.get(url, headers=self.headers)
            text = response.text
            html = etree.HTML(text)
            descs = html.xpath("//div[@class='j-r-list-c-desc']")
            for desc in descs:
                jokes = desc.xpath(".//text()")
                joke = "\n".join(jokes).strip()
                link = self.base_domain+desc.xpath(".//a/@href")[0]
                self.joke_queue.put((joke,link))
            print('='*30+"第%s页下载完成！"%url.split('/')[-1]+"="*30)

class BSWriter(threading.Thread):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
    }

    def __init__(self, joke_queue, writer,gLock, *args, **kwargs):
        super(BSWriter, self).__init__(*args, **kwargs)
        self.joke_queue = joke_queue
        self.writer = writer
        self.lock = gLock

    def run(self):
        while True:
            try:
                joke_info = self.joke_queue.get(timeout=40)
                joke,link = joke_info
                self.lock.acquire()
                self.writer.writerow((joke,link))
                self.lock.release()
                print('保存一条')
            except:
                break

def main():
    page_queue = Queue(10)
    joke_queue = Queue(500)
    gLock = threading.Lock()
    fp = open('bsbdj.csv', 'a',newline='', encoding='utf-8')
    writer = csv.writer(fp)
    writer.writerow(('content', 'link'))

    for x in range(1,11):
        url = 'http://www.budejie.com/text/%d' % x
        page_queue.put(url)

    for x in range(5):
        t = BSSpider(page_queue,joke_queue)
        t.start()

    for x in range(5):
        t = BSWriter(joke_queue,writer,gLock)
        t.start()

if __name__ == '__main__':
    main()
```