from threading import Thread, Semaphore, current_thread
from time import sleep

num = 0

# you can use BoundedSemaphore to prevent having negative value (release too many times error)
lock = Semaphore(value=2)


def add():
    global num
    lock.acquire()
    # with lock:  --use Semaphore with context manager
    print(current_thread().getName())
    sleep(2)
    num += 1
    lock.release()


t1 = Thread(target=add)
t2 = Thread(target=add)
t3 = Thread(target=add)
t4 = Thread(target=add)
t5 = Thread(target=add)
t6 = Thread(target=add)
t7 = Thread(target=add)
t8 = Thread(target=add)

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
t7.start()
t8.start()

t1.join()
t2.join()
t3.join()
t4.join()
t5.join()
t6.join()
t7.join()
t8.join()
