import threading
from time import sleep


def func():
    print("子线程（%s）启动"%(threading.current_thread().name))
    sleep(1)
    print("子线程调度中")
    sleep(1)
    print("子线程（%s）结束"%(threading.current_thread().name))

if __name__ == "__main__":
    print("主线程（%s）启动"%(threading.current_thread().name))

    t = threading.Thread(target=func, name='tttt')
    t.start()

    t.join()


    print("主线程（%s）结束"%(threading.current_thread().name))



