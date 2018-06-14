import threading,time,random,queue

def productor(id,q):
    while True:
        num = random.randint(0,100)
        q.put(num)
        print("生产者%d生产了%d"%(id,num))
        time.sleep(3)
    q.task_done()


def customer(id,q):
    while True:
        num = q.get()
        if num is None:
            break
        print("消费者%d消费了%d"%(id,num))
        time.sleep(2)
    q.task_done()




if __name__ == "__main__":
    # 消息队列
    q = queue.Queue()

    # 启动生产者
    for i in range(4):
        threading.Thread(target=productor,args=(i,q)).start()


    # 启动消费者
    for i in range(3):
        threading.Thread(target=customer,args=(i,q)).start()
