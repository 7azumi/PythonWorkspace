import threading,time

cond = threading.Condition()

def fuc1():
    with cond:
        for i in range(0,50,2):
            print(threading.current_thread().name,i)
            time.sleep(0.1)
            cond.wait()
            cond.notify()

def fuc2():
    with cond:
        for i in range(1,50,2):
            print(threading.current_thread().name,i)
            time.sleep(0.1)
            cond.notify()
            cond.wait()

threading.Thread(target=fuc1).start()
threading.Thread(target=fuc2).start()




