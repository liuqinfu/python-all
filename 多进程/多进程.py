from multiprocessing import Process
import time
# 启动进程的两种方式
# 1 使用Process启动进程
def task(name:str,sleepSeconds:int):
    print('%s 开始启动' % name)
    time.sleep(sleepSeconds)
    print('%s 结束' % name)

class MyProcess(Process):


    def run(self) -> None:
        print(' 开始启动')
        print(' 结束')


if __name__ == '__main__':
    start = time.time()
    '''
    p1 = Process(target=task, args=('egon', 2))
    p2 = Process(target=task, args=('tank', 1))
    p3 = Process(target=task, args=('leon', 3))
    '''
    p1 = MyProcess()
    p2 = MyProcess()
    p3 = MyProcess()
    p1.start()
    p2.start()
    p3.start()
    p1.join()
    p2.join()
    p3.join()
    print('主进程 %d' % (time.time()-start))