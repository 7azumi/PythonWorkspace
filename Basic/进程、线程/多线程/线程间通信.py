import threading,time

def func():
    event = threading.Event()
    def run():
        for i in range(5):
            event.wait()
            event.clear()
            print(i)
    t = threading.Thread(target=run).start()
    return event

e = func()

for i in range(6):
    time.sleep(0.5)
    e.set()