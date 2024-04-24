## 多任务编程——进程
### 什么是进程：
- 操作系统在运行过程中，一个程序运行起来就是一个进程。在Python中，多进程编程可以让我们的程序运行效率更高。同一时刻可以做更多的事情。因此多进程编程显得十分重要。

- multiprocessing模块介绍：
- multiprocessing是Python中一个专门用来创建创建多进程的库，multiprocessing提供了一个Process类来创建进程。
```python
from multiprocessing import Process

import time

def zhiliao():
    print('zhiliao process')


if __name__ == '__main__':
    # 开启一个子进程  ，如果需要参数 一定要用  args = () 的方式传入
    p = Process(target=zhiliao)
    p.start()

    while True:
        print('main process')
        time.sleep(3)

```

### 获取进程号：
- 在Python中可以通过os模块的一个函数getpid()可以获取到当前进程的进程号。通过getppid()可以获取到这个进程的父进程的进程号。示例代码如下：
```python
from multiprocessing import Process
import os


def zhiliao():
    print('===子进程===')
    print(f'子进程id:{os.getpid()}')
    print(f'父进程id:{os.getppid()}')
    print('===子进程===')


if __name__ == '__main__':
     p = Process(target=zhiliao)
     p.start()
     print(f'主进程id：{os.getpid()}')

```

### 父进程会等待子进程执行完毕后再退出：
- 如果在父进程中执行完所有代码后，还有子进程在执行，那么父进程会等待子进程执行完所有代码后再退出。

### Process对象的join方法：
- 使用Process创建了子进程，调用start方法后，父子进程会在各自的进程中不断的执行代码。
- 有时候如果想等待子进程执行完毕后再执行下面的代码，那么这时候可以调用join方法。示例代码如下：
```python
import time
from multiprocessing import Process


def zhiliao():
    for x in range(5):
        print(f'子进程中的代码{x}')
        time.sleep(1)


if __name__ == '__main__':
    p = Process(target=zhiliao)
    p.start()
    # 主进程阻塞 等待子进程完成才执行下面的代码  join方法还可以传一个timeout，用来指定等待的最长时间。
    p.join(2)
    print('父进程中的代码')

# output   如果不设置等待时间  父进程要等待所有子进程执行完成 才会执行 join之后的代码
# 子进程中的代码0
# 子进程中的代码1
# 子进程中的代码2
# 子进程中的代码3
# 子进程中的代码4
# 父进程中的代码

# output  设置了超时等待时间，等待2秒后  父进程代码执行 等待子进程执行完成后 才会才会执行join之后的打印语句
# 子进程中的代码0
# 子进程中的代码1
# 子进程中的代码2
# 父进程中的代码
# 子进程中的代码3
# 子进程中的代码4
```

### 使用类的方式创建子进程：
- 有些时候，你想以类的形式定义子进程的执行代码。那么你可以自定义一个类，让他继承自Process，
- 然后在这个类中实现run方法，以后这个子进程在执行的时候就会调用这个run方法中的代码。示例代码如下：
```python
from multiprocessing import Process

import os

import time


class MyProcess(Process):
    def run(self):
        for x in range(5):
            print(f'子进程：{x}')
            time.sleep(1)


if __name__ == '__main__':
    p = MyProcess()
    p.start()
    print(f'主进程id:{os.getpid()}')
```

### 进程池
multiprocessing模块中有一个类Pool，这个类相当于一个池，专门用来存储进程。
Pool的__init__可以传递一个参数，这个参数指定这个进程池中同一时刻最多只能拥有多少个进程。
并且，在使用进程池，父进程不会等待子进程池中的子进程执行完毕后退出，
而是当父进程中的代码执行完毕以后会立即退出。相关的示例代码如下：


1、apply() — 该函数用于传递不定参数，主进程会被阻塞直到函数执行结束（不建议使用，并且3.x以后不在出现），函数原型如下
apply(func, args=(), kwds={})

2、apply_async — 与apply用法一致，但它是非阻塞的且支持结果返回后进行回调，函数原型如下：
apply_async(func[, args=()[, kwds={}[, callback=None]]])

3、map() — Pool类中的map方法，与内置的map函数用法基本一致，它会使进程阻塞直到结果返回，函数原型如下：

map(func, iterable, chunksize=None)

4、map_async() — 与map用法一致，但是它是非阻塞的。其有关事项见apply_async，函数原型如下：

map_async(func, iterable, chunksize, callback)

5、close() — 关闭进程池（pool），使其不在接受新的任务。

6、terminal() — 结束工作进程，不在处理未处理的任务。

7、join() — 主进程阻塞等待子进程的退出， join方法要在close或terminate之后使用。

```python
from multiprocessing import Process, Pool
import os
import time


def worker(num):
    for x in range(5):
        print(f'num:{num},pid:{os.getpid()}')
        time.sleep(1)


if __name__ == '__main__':
    # 这个池子中同一时刻最多只有3个进程
    pool = Pool(3)
    for x in range(10):
        pool.apply_async(worker,(x,))

    # 关闭进程池，不能再添加新进程了
    pool.close()
    # 主进程把子进程添加到进程池后，不会等待进程池中其他的子进程都执行完毕后再退出
    # 而是当主进程的代码执行完毕后会立刻退出，因此如果这个地方没有join，那么子进程将得不到执行   不join()  不执行子进程
    pool.join()

    # output
    # 有3个子进程同时执行打印语句
    # 老进程执行的时候，新进程进入执行
```

### 进程间数据不共享：
- 在一个程序中，如果创建了一个子进程，那么这个子进程会拷贝一份当前进程所有的资源作为子进程的运行环境。
- 也就是说，子进程中的变量可能跟父进程一样，但其实是另外一个块内存区域了。他们之间的数据是不共享的。以下代码演示一下：
```python
from multiprocessing import Process
import os

AGE = 1


def child_func(names):
    global AGE
    AGE += 1
    names.append('ketang')
    print('=' * 8, '子进程', '=' * 8)
    print(f'AGE:{AGE}，id:{id(AGE)}')
    print(f'names:{names}')
    print(f'pid:{os.getpid()}')
    print('=' * 8, '子进程', '=' * 8)


if __name__ == '__main__':
    names = ['qiujie', ]
    p = Process(target=child_func,args=(names,))
    p.start()
    p.join()
    print('=' * 8, '父进程', '=' * 8)
    print(f'AGE:{AGE}，id:{id(AGE)}')
    print(f'names:{names}')
    print(f'pid:{os.getpid()}')
    print('=' * 8, '父进程', '=' * 8)
    # output
    # ======== 子进程 ========
    # AGE:2，id:4381551424
    # names:['qiujie', 'ketang']
    # pid:69484
    # ======== 子进程 ========
    # ======== 父进程 ========
    # AGE:1，id:4381551392  与子进程不同
    # names:['qiujie']      与子进程不同
    # pid:69483             与子进程不同
    # ======== 父进程 ========

```
### queue用法及进程通信
进程之间数据都是不共享的，因此想要在两个进程之间使用相同的数据，那么这时候就需要使用进程间的通信，

进程间通信有多种方式。两种，第一种是管道（Pipe）、第二种是队列（Queue）。以下讲解下使用Queue的通信。

Queue的一些常用方法的   详解在threading模块

Queue(n)：初始化一个消息队列，并指定这个队列中最多能够容纳多少条消息。

put(obj,[block[,timeout]])：推入一条消息到这个队列中。默认是阻塞的，也就是说如果这个消息队列中已经满了，那么会会一直等待，将这个消息添加到消息队列中。

timeout可以指定这个阻塞最长的时间，如果超过这个时间还是满的，就会抛出异常。 queue.full
put_nowait() ：非阻塞的推入一条消息，如果这个队列已经满了，那么会立马抛出异常。

qsize()：获取这个消息队列消息的数量。

full()：判断这个消息队列是否满了。

empty()：判断这个消息队列是否空了。

get([block[,timeout]])：获取队列中的一条消息，然后将其从队列中移除，block默认为True。如果设置block为False，那么如果没值，会立马抛出异常。
timeout指定如果多久没有获取到值后会抛出异常。
```python
# 使用Queue给Process进程做进程间通信
#  在进程中使用queue  只能使用包中自带的类  使用自带的Queue不生效
from multiprocessing import Process,Queue
import time


def read_func(q):
    # 已阻塞的方式获得数据
    value = q.get(True)
    print(f'read value {value}')
    time.sleep(1)


def write_func(q):
    for x in ['m1', 'm2', 'm3', 'm4']:
        # 最好设置等待时间，不然 写不进去了也会一直等待
        q.put(x,timeout=3)
        time.sleep(1)


if __name__ == '__main__':
    #  如果小于4  由于数据写不进去 会一直等待
    q = Queue(4)
    process_w = Process(target=write_func,args=(q,))
    process_r = Process(target=read_func,args=(q,))

    process_w.start()
    process_w.join()
    process_r.start()
```

### 使用Queue给Process进程做进程间通信
```python
# 如果要使用Pool创建进程，就需要使用multiprocessing.Manager()中的Queue()，
# 而不是multiprocessing.Queue()，否则会报错。RuntimeError: Queue objects should only be shared between processes through inheritance。
# 下面代码演示进程池中的进程通信：

from multiprocessing import Pool, Queue, Process, Manager


def read_fuc(q):
    while not q.empty():
        # 按照先进先出的原则 读取数据
        print(f'读到的值:{q.get()}')


def write_func(q):
    for x in ['m1', 'm2', 'm3']:
        q.put(x)


if __name__ == '__main__':
    q = Manager().Queue()
    pool = Pool(2)
    pool.apply(write_func, args=(q,))
    pool.apply(read_fuc, args=(q,))
    pool.close()

    pool.join()

```

#### 小案列
- 1、计算1~100000000之间所有偶数的和。（提示：可以使用内置的sum函数计算和。如list=[1, 2];sum(list))。然后思考以下问题：
```python
from multiprocessing import Manager, Pool
import time
from decorator.time_fuc_dec import timeit

@timeit()
def sum_data(start_position, end_position, queue2):
    queue2.put(sum(range(start_position, end_position, 2)))


if __name__ == '__main__':
    start_time = time.time()
    pool = Pool(10)
    queue1 = Manager().Queue(10)
    for x in range(1, 1000000001, 100000000):
        print(x)
        pool.apply_async(
            sum_data, args=(x, x + 100000000, queue1)
        )

    pool.close()
    pool.join()
    sum3 = 0
    for _ in range(10):
        sum3 += queue1.get(block=False)

    print(f'{time.time() - start_time}:{sum3}')
```