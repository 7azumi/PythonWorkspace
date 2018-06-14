from multiprocessing import pool
import os, time, random

def fun(name):
    start = time.time()
    print("%s号进程开始 pid为：%s"%(name,os.getpid()))
    time.sleep(random.choice([1,2,3]))
    end = time.time()
    print("%s号进程结束 持续时间为 %0.2f"%(name,end-start))

if __name__ == "__main__":
    print("父进程启动")
    start = time.time()

    # Pool的默认大小为cpu核心数
    pp = pool.Pool()
    for i in range(14):
        # 创建进程，在进程池中统一管理
        pp.apply_async(fun,args=(i,))

    pp.close()
    pp.join()

    end = time.time()
    print("父进程结束，耗时%0.2f秒"%(end-start))