from multiprocessing import Process, Queue
import os,time

def write(q):
    print("启动写进程：%s"%(os.getpid()))
    for chr in ['A','B','C','D']:
        q.put(chr)
        time.sleep(1)
    print("结束写进程" )

def read(q):
    print("启动读进程：%s" % (os.getpid()))
    while True:
        value = q.get(True)
        print("value:"+value)
    print("结束读进程")

if __name__ == '__main__':
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))

    pw.start()
    pr.start()

    pw.join()
    pr.terminate()

    print("父进程结束")

