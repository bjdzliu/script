
from threading import Thread
def hello(name):
    print('hello world'+' '+name)
t = Thread(target=hello, args=("dz",))

t.start()



# 创建一个类，必须要继承Thread
class MyThread(Thread):
    # 继承Thread的类，需要实现run方法，线程就是从这个方法开始的
    def run(self):
        # 具体的逻辑
        hello(self.parameter1)
    def __init__(self, parameter1):
        # 需要执行父类的初始化方法
        Thread.__init__(self)
        # 如果有参数，可以封装在类里面
        self.parameter1 = parameter1
# 如果有参数，实例化的时候需要把参数传递过去
t = MyThread('dezhao')
# 同样使用start()来启动线程
t.start()


thread_list=[]
for i in range(1,11):
    t=MyThread("multipile process")
    thread_list.append(t)
    t.start()
for t in    thread_list:
    t.join()