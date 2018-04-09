#! -*- coding: utf-8 -*-

import _thread
from time import sleep, time

loops = [4, 2]

def loop(nloop, nsec, lock):
    print('start loop %s at: %s' % (nloop, time()))
    sleep(nsec)
    print('loop %s done at: %s' % (nloop, time()))
    # 每个线程都会被分配一个事先已经获得的锁，在 sleep()的时间到了之后就释放 相应的锁以通知主线程，这个线程已经结束了。
    lock.release()


def main():
    print('starting at:', time())
    locks = []
    nloops = range(len(loops))

    for i in nloops:
        # 调用 thread.allocate_lock()函数创建一个锁的列表
        lock = _thread.allocate_lock()
        # 分别调用各个锁的 acquire()函数获得, 获得锁表示“把锁锁上”
        lock.acquire()
        locks.append(lock)

    for i in nloops:
        # 创建线程，每个线程都用各自的循环号，睡眠时间和锁为参数去调用 loop()函数
        _thread.start_new_thread(loop, (i, loops[i], locks[i]))

    for i in nloops:
        # 在线程结束的时候，线程要自己去做解锁操作
        # 当前循环只是坐在那一直等(达到暂停主 线程的目的)，直到两个锁都被解锁为止才继续运行。
        while locks[i].locked(): pass

    print('all DONE at:', time())

if __name__ == '__main__':
    main()
