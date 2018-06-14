from multiprocessing import Process
from time import sleep
import os

def func1():
    while True:
        print("嘿 in %s--%s"%(os.getpid(), os.getppid()))
        sleep(0.5)

def func2():
    while True:
        print("嘻 in %s--%s"%(os.getpid(), os.getppid()))
        sleep(0.5)

if __name__ == "__main__":
    p1 = Process(target=func1)
    p2 = Process(target=func2)

    p1.start()
    p2.start()

    while True:
        print("哈 in %s"%(os.getpid()))
        sleep(0.5)
