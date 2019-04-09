#! -*- coding: utf-8 -*-
import  threading,time
def loop():
    # 输出进程的 mainthread。该线程是进程自动生成的第一个.
    print('main thread\'s children %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('main thread\'s children  %s ended.' % threading.current_thread().name)


print('thread(1) %s is running...' % threading.current_thread().name)

t = threading.Thread(target=loop, name='LoopThread')
t.start()
#主进程等待线程结束后，再结束
t.join()
print('thread %s ended.' % threading.current_thread().name)
